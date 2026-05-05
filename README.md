# Paper 11: Gravitational Entropy Escrow — Experiments & Code

**An Interpretive Synthesis of Thermodynamic Approaches to Gravity**

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20031932-blue)](https://doi.org/10.5281/zenodo.20031932)
[![License: MIT](https://img.shields.io/badge/Code-MIT-green)](https://opensource.org/licenses/MIT)
[![License: CC BY 4.0](https://img.shields.io/badge/Data-CC_BY_4.0-lightgrey)](https://creativecommons.org/licenses/by/4.0/)
[![Track: Entropic Bounds](https://img.shields.io/badge/Track-2_·_Entropic_Bounds-8b5cf6)](https://windstorminstitute.org/#track2)

> **Track 2 of the Windstorm Institute — Entropic Bounds in Analog Systems.** Companion to the paper's empirical sections (§6.1, §8.4, §10).

---

## Published Paper

- **[Windstorm-Institute/gravitational-entropy-escrow](https://github.com/Windstorm-Institute/gravitational-entropy-escrow)** — paper PDF, article HTML, submission scaffolds
- **Website article:** [windstorminstitute.org/articles/gravitational-entropy-escrow.html](https://windstorminstitute.org/articles/gravitational-entropy-escrow.html)
- **Zenodo:** [10.5281/zenodo.20031932](https://doi.org/10.5281/zenodo.20031932) (deposited 2026-05-05)

## What this repo will hold

The paper develops three quantitative empirical analyses. When the analysis scripts and raw output tables are mirrored here from the Zenodo archive, this directory will contain:

| Analysis | Directory | What it does | Paper section |
|----------|-----------|--------------|---------------|
| Genzel five-case test | `experiments/genzel_five_case/` | Residuals over 6 high-z galaxies × 5 `a_0` prescriptions × 2 interpolation functions. Independently disfavors `H(z)`-tracking and `(1+z)^(3/2)`-tracking; confirms constant `a_0`. | §6.1 (Table 1) |
| SPARC global deep-MOND `a_0` | `experiments/sparc_global_a0/` | Median of `g_obs²/g_bar` over ~1,400 deep-MOND points in ~140 SPARC galaxies. Global `a_0 ≈ 1.24 × 10⁻¹⁰ m/s²`. | §8.4 |
| SPARC interpolation comparison | `experiments/sparc_interpolation/` | Smoke test of simple-μ, McGaugh-ν, and quadrature interpolation forms on ~200 radial points across ~14 galaxies (NGC 3198, NGC 2403, NGC 2915, DDO 154, ...). | §10 |

Plots live in `plots/`.

## Code archive (current authoritative source)

> **Note (May 2026):** The full Python analysis source — including the Genzel five-case residuals computation, the SPARC `a_0` reanalysis, and the interpolation smoke test, plus their raw output tables — is archived alongside the paper on **[Zenodo (10.5281/zenodo.20031932)](https://doi.org/10.5281/zenodo.20031932)**. Mirroring to this repo is in progress; until that completes, the Zenodo deposit is the canonical reproducibility archive.

## Data sources

- **SPARC mass-models table** (Lelli, McGaugh & Schombert 2016): publicly available from [astroweb.cwru.edu/SPARC](http://astroweb.cwru.edu/SPARC/). **Not redistributed in this repo.** Download the table directly from the SPARC project before running the analysis scripts.
- **Genzel et al. (2017)** Table I values (V_c, R_(1/2), ζ_(1/2)) for the six high-z disk galaxies are reproduced inline in the deposited Genzel-five-case script.

## Reproduction (when scripts are mirrored)

- **Python:** 3.12+
- **Dependencies:** NumPy, SciPy, pandas, matplotlib (no astrophysics-specific packages required)
- **Total compute:** ~1 minute for the Genzel test, ~10 seconds for the SPARC reanalysis
- **External data:** SPARC mass-models table (download separately per above)

## Posture

The paper is interpretive and the empirical work is **consistency checks rather than distinguishing tests** (per §8.4.3). Standard MOND with `a_0` treated as a fitted constant also passes these checks by construction. The framework's contribution at the SPARC level is the identification of `a_0` with the Gibbons–Hawking temperature of the cosmological horizon and the recovery of `a_0` to within an order-unity coefficient `α ≈ 1.39` without further free parameters. A genuinely distinguishing test requires either a derivation of the transition functional form from horizon thermodynamics or a regime where the Λ-form vs. H(z)-form distinction makes a quantitative difference; the high-redshift Genzel residuals are the closest existing realization of the latter.

---

## The Windstorm Institute

### Track 1 — The Throughput Basin (Papers 1–9, complete arc)

| # | Paper | DOI |
|---|-------|-----|
| 1 | [The Fons Constraint](https://github.com/Windstorm-Institute/fons-constraint) | [10.5281/zenodo.19274048](https://doi.org/10.5281/zenodo.19274048) |
| 2 | [The Receiver-Limited Floor](https://github.com/Windstorm-Institute/receiver-limited-floor) | [10.5281/zenodo.19322973](https://doi.org/10.5281/zenodo.19322973) |
| 3 | [The Throughput Basin](https://github.com/Windstorm-Institute/throughput-basin) | [10.5281/zenodo.19323194](https://doi.org/10.5281/zenodo.19323194) |
| 4 | [The Serial Decoding Basin τ](https://github.com/Windstorm-Institute/serial-decoding-basin) | [10.5281/zenodo.19323423](https://doi.org/10.5281/zenodo.19323423) |
| 5 | [The Dissipative Decoder](https://github.com/Windstorm-Institute/dissipative-decoder) | [10.5281/zenodo.19433048](https://doi.org/10.5281/zenodo.19433048) |
| 6 | [The Inherited Constraint](https://github.com/Windstorm-Institute/inherited-constraint) | [10.5281/zenodo.19432911](https://doi.org/10.5281/zenodo.19432911) |
| 7 | [The Throughput Basin Origin](https://github.com/Windstorm-Institute/throughput-basin-origin) | [10.5281/zenodo.19498582](https://doi.org/10.5281/zenodo.19498582) |
| 8 | [The Vision Basin](https://github.com/Windstorm-Institute/vision-basin) | [10.5281/zenodo.19672827](https://doi.org/10.5281/zenodo.19672827) |
| 9 | [The Hardware Basin](https://github.com/Windstorm-Institute/hardware-basin) | [10.5281/zenodo.19672921](https://doi.org/10.5281/zenodo.19672921) |

### Track 2 — Entropic Bounds in Analog Systems

| # | Paper | DOI |
|---|-------|-----|
| 10 | [Phonon Extraction Bound (BEC Analog Gravity)](https://github.com/Windstorm-Institute/phonon-extraction-bound) | [10.5281/zenodo.20014391](https://doi.org/10.5281/zenodo.20014391) |
| 11 | [Gravitational Entropy Escrow](https://github.com/Windstorm-Institute/gravitational-entropy-escrow) *(this paper)* | [10.5281/zenodo.20031932](https://doi.org/10.5281/zenodo.20031932) |

**Website:** [windstorminstitute.org](https://windstorminstitute.org)

---

*Code: MIT License · Data: CC BY 4.0*
