# Reproducibility code for the Gravitational Entropy Escrow paper (v0.6.11)

This directory contains the analysis scripts used to produce the empirical claims in:

> Whitmer, G. L. III (2026). *Gravitational Entropy Escrow: An Interpretive Synthesis of Thermodynamic Approaches to Gravity.* Windstorm Institute Working Paper, draft v0.6.11. DOI: [10.5281/zenodo.20032023](https://doi.org/10.5281/zenodo.20032023).

The scripts are mirrored from the Zenodo deposit; the Zenodo archive remains the canonical reproducibility snapshot tied to the paper's quoted version, and this repo will track future revisions.

## Contents

### `sparc_global_a0/` — Section 8.4

- **`sparc_rar_analysis.py`** — full SPARC radial-acceleration-relation re-analysis. Reproduces the global deep-MOND `a_0` estimate (~1.24 × 10⁻¹⁰ m s⁻²), the per-galaxy `a_0` distribution, the DDO 154 spot-check value, the RAR plot, and the per-galaxy histogram.

### `sparc_interpolation/` — Section 10

- **`interpolation_compare.py`** — three-way comparison of the simple-μ, McGaugh-ν, and quadrature interpolation forms. A smoke test on a SPARC subset (no per-galaxy nuisance marginalization) demonstrating that the three forms produce empirically indistinguishable best-fit residuals once `a_0` is allowed to float.
- **`sparc_subset_for_interpolation.txt`** — the SPARC subset used in the interpolation comparison. Approximately 200 radial points across 14 galaxies including NGC 3198, NGC 2403, NGC 2915, and DDO 154. Drawn directly from Lelli et al. 2016 Table 2.

### Section 6.1 (Genzel five-case test)

The five-case test on Genzel et al. (2017) high-redshift galaxies (Table 1 of the paper) was performed inline against the published Genzel Table I values; no standalone script is deposited. The data inputs are reproduced inline in the relevant section of the paper, and the per-row computation can be implemented in a few lines of NumPy by anyone wishing to reproduce.

## Required dependencies

- Python 3.8 or later
- numpy
- pandas
- matplotlib (only required for `sparc_rar_analysis.py`)

Install with:

```bash
pip install numpy pandas matplotlib
```

## How to reproduce the paper's quoted numbers

### Section 8.4 (full SPARC analysis)

1. Download the SPARC mass-models table from <http://astroweb.cwru.edu/SPARC/> — specifically the machine-readable file `Table2.mrt` for *"SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves"* (Lelli, McGaugh & Schombert 2016).

2. Place the file inside `experiments/sparc_global_a0/` and rename it `sparc_table2.mrt`.

3. Run:

   ```bash
   cd experiments/sparc_global_a0
   python3 sparc_rar_analysis.py
   ```

The script will print summary statistics matching those quoted in Section 8.4 and will produce two figures (`rar_plot.png`, `a0_histogram.png`) and one CSV (`per_galaxy_a0.csv`).

### Section 10 (interpolation smoke test)

The SPARC subset used in the smoke test is bundled inline. Run:

```bash
cd experiments/sparc_interpolation
python3 interpolation_compare.py
```

The script will print best-fit `a_0` values and RMS residuals for each of the three interpolation forms. All three should produce RMS values within ~0.001 dex of each other, demonstrating empirical indistinguishability at the available precision.

## Notes on reproducibility

The full SPARC table is the canonical public dataset used in McGaugh et al. (2016), Lelli et al. (2016), and Li et al. (2018). We do not redistribute the full table here — it is freely available from the SPARC project at the URL above and should be obtained directly to ensure use of the latest revision.

The subset bundled with this distribution is sufficient to reproduce the smoke test of Section 10 but **not** the global statistics of Section 8.4; for those the full table is required.

Methodology follows Lelli, McGaugh & Schombert (2016) exactly, including the fiducial mass-to-light ratios (`ML_disk = 0.5`, `ML_bul = 0.7` at 3.6 µm) and the standard deep-MOND regime selection (`g_bar < a_0_Milgrom / 10`).

## Reproducibility caveats (applicable to both scripts)

The scripts pin Milgrom's canonical fiducial `a_0_Milgrom = 1.20 × 10⁻¹⁰ m s⁻²` for the deep-MOND regime cut. Differences at the percent level may arise from updated SPARC table revisions; the qualitative conclusions of Section 8.4 are not affected.

The interpolation comparison is explicitly a smoke test, not a publication-grade analysis — real interpolation comparisons (e.g. Li et al. 2018) marginalize over per-galaxy distance, inclination, and mass-to-light ratio nuisance parameters. Without that marginalization, the residual scatter is dominated by per-galaxy systematics (~0.25 dex) rather than the intrinsic RAR scatter (~0.034 dex). The point of the script is to demonstrate that the three forms are empirically interchangeable at the precision available without nuisance marginalization, not to characterize the absolute fit quality of any one interpolation.

## License

MIT for code, CC BY 4.0 for data. See repo root [`LICENSE`](../LICENSE).

## Contact

For questions about the analysis or to report discrepancies between script output and paper text, open an issue on this repo or contact the author at the address listed in the paper.
