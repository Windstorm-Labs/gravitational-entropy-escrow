#!/usr/bin/env python3
"""
sparc_rar_analysis.py
=====================

SPARC radial-acceleration-relation (RAR) reanalysis used in:

    Whitmer, G. L. III (2026). Gravitational Entropy Escrow:
    A Physical Reframing of Thermodynamic Gravity.
    Windstorm Institute Working Paper, draft v0.6.6.

This script reproduces the deep-MOND a_0 estimate quoted in Section 8.4
of the paper. It expects the public SPARC mass-models table
(Lelli, McGaugh & Schombert 2016, AJ 152, 157) -- specifically the
machine-readable file Table2.mrt available from

    http://astroweb.cwru.edu/SPARC/

Place that file in the same directory as this script, named
``sparc_table2.mrt`` (or override INPUT_FILE below).  Then run:

    python3 sparc_rar_analysis.py

Outputs:

  - per_galaxy_a0.csv : per-galaxy deep-MOND a_0 values
  - rar_plot.png      : the SPARC radial acceleration relation
  - a0_histogram.png  : distribution of per-galaxy a_0 values

The numbers reported in the paper at v0.6.6 are:

  - 175 galaxies parsed (matches Lelli 2016 published count)
  - approximately 3,400 radial points after standard cuts
  - approximately 1,400 deep-MOND points across approximately 140 galaxies
  - global deep-MOND a_0 median ~ 1.24 x 10^-10 m s^-2
  - per-galaxy a_0 median        ~ 1.24 x 10^-10 m s^-2
  - DDO 154 spot-check           ~ 1.04 x 10^-10 m s^-2

These should be reproduced exactly by running this script on the
public SPARC table at the time of writing (May 2026).  Differences
at the percent level may arise from updated versions of the SPARC
release; the qualitative conclusions of Section 8.4 are not
affected by such differences.

Methodology follows Lelli, McGaugh & Schombert (2016) and McGaugh,
Lelli & Schombert (2016):

  - Fiducial mass-to-light ratios at 3.6 micron:
      ML_disk = 0.5  (disk component)
      ML_bul  = 0.7  (bulge component)
  - Baryonic acceleration:
      g_bar = (V_gas^2 + ML_disk * V_disk^2 + ML_bul * V_bul^2) / R
  - Observed acceleration:
      g_obs = V_obs^2 / R
  - Deep-MOND regime selection:
      g_bar < a_0_Milgrom / 10, with a_0_Milgrom = 1.20e-10 m s^-2
  - Per-galaxy a_0 estimator:
      median of g_obs^2 / g_bar over deep-MOND points,
      requiring at least 3 deep-MOND points per galaxy
  - Global a_0 estimator:
      median of g_obs^2 / g_bar over all deep-MOND points across all galaxies

License: MIT.  Redistribution and modification freely permitted
provided this attribution is preserved.
"""

import re
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

KPC_TO_M = 3.085677581e19          # m per kpc
KM_TO_M  = 1000.0                  # m per km
CONV     = (KM_TO_M ** 2) / KPC_TO_M   # ~ 3.241e-14 m s^-2 per (km/s)^2/kpc

A0_MILGROM = 1.20e-10              # m s^-2  (Milgrom canonical fiducial)

ML_DISK = 0.5
ML_BUL  = 0.7

INPUT_FILE = "sparc_table2.mrt"
EXPECTED_GALAXIES = 175

HEADER_PREFIXES = (
    "Title:", "Authors:", "Table:", "====", "----",
    "Byte-by-byte", "Format", "Units", "Label", "Explanations", "Note (",
)

GALAXY_NAME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9\-\+_\.]*$")


# ---------------------------------------------------------------------------
# Parser for the SPARC MRT file
# ---------------------------------------------------------------------------

def parse_sparc(filename):
    """Parse Lelli/McGaugh/Schombert SPARC Table2.mrt format.

    Columns (in order, as documented in the SPARC MRT byte-by-byte description):
        ID    : galaxy identifier
        D     : assumed distance, Mpc
        R     : galactocentric radius, kpc
        Vobs  : observed circular velocity, km/s
        eVobs : random error on Vobs, km/s
        Vgas  : gas velocity contribution, km/s (includes 1.33 He factor)
        Vdisk : disk velocity contribution, km/s (at M/L = 1)
        Vbul  : bulge velocity contribution, km/s (at M/L = 1)
        SBdisk: disk surface brightness, solLum/pc^2  (not used)
        SBbul : bulge surface brightness, solLum/pc^2 (not used)
    """
    rows = []
    with open(filename) as fh:
        for line in fh:
            stripped = line.strip()
            if not stripped:
                continue
            if any(stripped.startswith(p) for p in HEADER_PREFIXES):
                continue
            if stripped[0] in ("=", "-") and len(stripped) > 1:
                continue
            parts = stripped.split()
            if len(parts) < 9:
                continue
            if not GALAXY_NAME_RE.match(parts[0]):
                continue
            try:
                rows.append({
                    "galaxy": parts[0],
                    "D_Mpc":  float(parts[1]),
                    "R_kpc":  float(parts[2]),
                    "Vobs":   float(parts[3]),
                    "eVobs":  float(parts[4]),
                    "Vgas":   float(parts[5]),
                    "Vdisk":  float(parts[6]),
                    "Vbul":   float(parts[7]) if len(parts) > 7 else 0.0,
                })
            except ValueError:
                continue
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Acceleration computations
# ---------------------------------------------------------------------------

def compute_accelerations(df):
    """Add g_bar and g_obs columns (in SI m s^-2) using the Lelli/McGaugh
    fiducial mass-to-light ratios.
    """
    df = df.copy()
    df["g_bar"] = (
        df["Vgas"]  ** 2
        + ML_DISK * df["Vdisk"] ** 2
        + ML_BUL  * df["Vbul"]  ** 2
    ) * CONV / df["R_kpc"]
    df["g_obs"] = df["Vobs"] ** 2 * CONV / df["R_kpc"]
    # standard cuts
    df = df[(df["g_bar"] > 0) & (df["R_kpc"] > 0) & (df["Vobs"] > 0)].copy()
    return df


def per_galaxy_a0(deep_df, min_points=3):
    """For each galaxy with at least min_points deep-MOND radial points,
    return the median of g_obs^2 / g_bar in m s^-2.
    """
    def _med(g):
        if len(g) < min_points:
            return np.nan
        return np.median(g["g_obs"] ** 2 / g["g_bar"])
    return deep_df.groupby("galaxy").apply(_med).dropna()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    df_raw = parse_sparc(INPUT_FILE)
    n_galaxies_raw = df_raw["galaxy"].nunique()
    print(f"Parsed {len(df_raw)} radial points across "
          f"{n_galaxies_raw} galaxies from {INPUT_FILE}.")
    if n_galaxies_raw != EXPECTED_GALAXIES:
        print(f"  WARNING: galaxy count differs from SPARC's published "
              f"{EXPECTED_GALAXIES}. Investigate parser cuts.")
    print()

    df = compute_accelerations(df_raw)
    print(f"After standard cuts (g_bar > 0, R > 0, Vobs > 0): "
          f"{len(df)} points across {df['galaxy'].nunique()} galaxies.")

    # Deep-MOND regime
    deep = df[df["g_bar"] < A0_MILGROM / 10].copy()
    print(f"Deep-MOND points (g_bar < a_0_Milgrom / 10): "
          f"{len(deep)} from {deep['galaxy'].nunique()} galaxies.")

    a0_per = per_galaxy_a0(deep)
    print(f"Galaxies with >= 3 deep-MOND points: {len(a0_per)}")
    print()

    # Global and per-galaxy a_0 estimators
    global_med = (deep["g_obs"] ** 2 / deep["g_bar"]).median()
    global_mn  = (deep["g_obs"] ** 2 / deep["g_bar"]).mean()
    per_med    = a0_per.median()
    per_mn     = a0_per.mean()
    per_std    = a0_per.std()

    print(f"Global deep-MOND a_0 (median over all deep points): "
          f"{global_med:.3e} m s^-2")
    print(f"Global deep-MOND a_0 (mean   over all deep points): "
          f"{global_mn:.3e} m s^-2")
    print(f"Per-galaxy   a_0 (median across galaxies):           "
          f"{per_med:.3e} m s^-2")
    print(f"Per-galaxy   a_0 (mean +/- std across galaxies):    "
          f"{per_mn:.3e} +/- {per_std:.3e} m s^-2")
    print()

    # DDO 154 spot-check
    ddo_keys = [n for n in a0_per.index
                if n.upper().replace("-", "").replace("_", "")
                in ("DDO154", "DDO0154", "D154")]
    if ddo_keys:
        v = a0_per[ddo_keys[0]]
        print(f"DDO 154 spot-check: a_0 = {v:.3e} m s^-2  "
              f"(literature range ~ 1.0 - 1.5 e-10)")
    print()

    # Save per-galaxy table
    a0_per.sort_values().to_csv("per_galaxy_a0.csv", header=["a0_m_per_s2"])
    print("Saved: per_galaxy_a0.csv")

    # RAR plot
    plt.figure(figsize=(8, 6))
    plt.loglog(df["g_bar"], df["g_obs"], "o", color="gray", alpha=0.30,
               label="All radial points")
    plt.loglog(deep["g_bar"], deep["g_obs"], "o", color="C0", alpha=0.60,
               label="Deep-MOND")
    gb = np.logspace(-13, -8, 200)
    plt.loglog(gb, np.sqrt(gb * A0_MILGROM), "--", color="C3",
               label=fr"$\sqrt{{g_{{\rm bar}}\,a_0}}$, "
                     fr"$a_0$={A0_MILGROM:.2e}")
    plt.loglog(gb, gb, ":", color="k", alpha=0.5, label="Newton")
    plt.xlabel(r"$g_{\rm bar}$ (m s$^{-2}$)")
    plt.ylabel(r"$g_{\rm obs}$ (m s$^{-2}$)")
    plt.title("SPARC radial acceleration relation "
              f"(fiducial M/L = {ML_DISK} / {ML_BUL})")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("rar_plot.png", dpi=150)
    plt.close()
    print("Saved: rar_plot.png")

    # a_0 histogram
    plt.figure(figsize=(7, 4.5))
    a0_per.hist(bins=25, color="steelblue", edgecolor="black")
    plt.axvline(A0_MILGROM, color="C2", linestyle="--",
                label=f"$a_0$ = {A0_MILGROM:.2e} (Milgrom)")
    plt.axvline(global_med, color="C3", linestyle="-",
                label=f"global median = {global_med:.2e}")
    plt.xlabel(r"per-galaxy $a_0$ (m s$^{-2}$)")
    plt.ylabel("number of galaxies")
    plt.title("SPARC per-galaxy deep-MOND $a_0$")
    plt.legend()
    plt.tight_layout()
    plt.savefig("a0_histogram.png", dpi=150)
    plt.close()
    print("Saved: a0_histogram.png")


if __name__ == "__main__":
    main()
