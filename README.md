# Paper 11: Gravitational Entropy Escrow — Experiments & Code

**An Interpretive Synthesis of Thermodynamic Approaches to Gravity**

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20032023-blue)](https://doi.org/10.5281/zenodo.20032023)
[![License: MIT](https://img.shields.io/badge/Code-MIT-green)](https://opensource.org/licenses/MIT)
[![License: CC BY 4.0](https://img.shields.io/badge/Data-CC_BY_4.0-lightgrey)](https://creativecommons.org/licenses/by/4.0/)
[![Track: Entropic Bounds](https://img.shields.io/badge/Track-2_·_Entropic_Bounds-8b5cf6)](https://windstorminstitute.org/#track2)

> **Track 2 of the Windstorm Institute — Entropic Bounds in Analog Systems.** Companion to the paper's empirical sections (§6.1, §8.4, §10).

---

## Published Paper

- **[Windstorm-Institute/gravitational-entropy-escrow](https://github.com/Windstorm-Institute/gravitational-entropy-escrow)** — paper PDF, article HTML, submission scaffolds
- **Website article:** [windstorminstitute.org/articles/gravitational-entropy-escrow.html](https://windstorminstitute.org/articles/gravitational-entropy-escrow.html)
- **Zenodo:** [10.5281/zenodo.20032023](https://doi.org/10.5281/zenodo.20032023) (deposited 2026-05-05)

## Contents

| Analysis | Directory | What it does | Paper section |
|----------|-----------|--------------|---------------|
| **SPARC global deep-MOND `a_0`** | [`experiments/sparc_global_a0/`](experiments/sparc_global_a0/) | Full SPARC RAR re-analysis. Reproduces global `a_0 ≈ 1.24 × 10⁻¹⁰ m/s²`, the per-galaxy distribution, the DDO 154 spot-check, and the RAR plot. | §8.4 |
| **SPARC interpolation comparison** | [`experiments/sparc_interpolation/`](experiments/sparc_interpolation/) | Three-way smoke test of simple-μ, McGaugh-ν, and quadrature interpolation forms on a ~200-point, ~14-galaxy SPARC subset (NGC 3198, NGC 2403, NGC 2915, DDO 154, …). Bundled subset included; full SPARC table required for §8.4. | §10 |
| Genzel five-case test | *(no standalone script — inline in paper)* | The five-case test on Genzel et al. (2017) high-redshift galaxies (Table 1) was performed inline against the published Genzel Table I values; reproducible in a few lines of NumPy. | §6.1 |

See [`experiments/README.md`](experiments/README.md) for full reproduction instructions, dependencies, and methodology notes.

Output figures and per-analysis plots will be deposited in `plots/` as scripts are run.

## Code archive (canonical version)

The Python analysis scripts in this repo are mirrored from the Zenodo deposit. The Zenodo archive — **[10.5281/zenodo.20032023](https://doi.org/10.5281/zenodo.20032023)** — remains the canonical version-locked reproducibility snapshot tied to the paper's quoted numbers; this repo will track future revisions.

## Data sources

- **SPARC mass-models table** (Lelli, McGaugh & Schombert 2016): publicly available from [astroweb.cwru.edu/SPARC](http://astroweb.cwru.edu/SPARC/). **Not redistributed in this repo** — download `Table2.mrt` directly from the SPARC project, drop it into `experiments/sparc_global_a0/sparc_table2.mrt`, and run.
- **SPARC subset for §10**: bundled inline at `experiments/sparc_interpolation/sparc_subset_for_interpolation.txt` (drawn from Lelli 2016 Table 2, ~200 radial points across 14 galaxies).
- **Genzel et al. (2017) Table I**: the six high-z disk galaxy values used in the §6.1 five-case test are reproduced inline in the paper.

## Reproduction

- **Python:** 3.11 or later
- **Dependencies:** `numpy`, `pandas`, `matplotlib` (matplotlib only required for §8.4)
- **Total compute:** ~10 seconds for the SPARC interpolation comparison; ~30 seconds for the full SPARC RAR re-analysis once the Table2.mrt download is in place
- **External data:** SPARC `Table2.mrt` (download separately per above) for §8.4; bundled subset suffices for §10

## Posture

The paper is interpretive and the empirical work is **consistency checks rather than distinguishing tests** (per §8.4.3). Standard MOND with `a_0` treated as a fitted constant also passes these checks by construction. The framework's contribution at the SPARC level is the identification of `a_0` with the Gibbons–Hawking temperature of the cosmological horizon and the recovery of `a_0` to within an order-unity coefficient `α ≈ 1.39` without further free parameters. A genuinely distinguishing test requires either a derivation of the transition functional form from horizon thermodynamics or a regime where the Λ-form vs. H(z)-form distinction makes a quantitative difference; the high-redshift Genzel residuals are the closest existing realization of the latter.

---

## Discuss this code

- **Bug, reproduction failure, or unexpected output?** → [Open an Issue](../../issues)
- **Q&A — version compatibility, hardware, generalization to other inputs?** → [Start a Discussion](../../discussions)
- **Discuss the paper itself** → [Comments on the website article](https://windstorminstitute.org/articles/gravitational-entropy-escrow.html#comments) or [Issues on the Institute repo](https://github.com/Windstorm-Institute/gravitational-entropy-escrow/issues)

---

## The Windstorm Institute

### Track 1 — The Throughput Basin · 9 papers (Papers 1–9 globally; 1st through 9th in this track; arc complete)

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

### Track 2 — Entropic Bounds in Analog Systems · 7 papers (Papers 10–16 globally; 1st through 7th in this track; line of inquiry active)

| # | Paper | DOI |
|---|-------|-----|
| 10 | [Phonon Extraction Bound (BEC Analog Gravity)](https://github.com/Windstorm-Institute/phonon-extraction-bound) *(1st in track)* | [10.5281/zenodo.20014391](https://doi.org/10.5281/zenodo.20014391) |
| 11 | [Gravitational Entropy Escrow](https://github.com/Windstorm-Institute/gravitational-entropy-escrow) *(this paper — 2nd in track)* | [10.5281/zenodo.20032023](https://doi.org/10.5281/zenodo.20032023) |
| 12 | [C8 Clarification Note](https://github.com/Windstorm-Institute/c8-clarification-note) *(3rd in track; companion to this paper)* | [10.5281/zenodo.20041992](https://doi.org/10.5281/zenodo.20041992) |
| 13 | [Lattice QFT Test of the Static Escrow Postulate](https://github.com/Windstorm-Institute/lattice-qft-test) *(4th in track; supplement to Paper 11)* | [10.5281/zenodo.20057538](https://doi.org/10.5281/zenodo.20057538) |
| 14 | [Spacetime as Escrow Bookkeeping](https://github.com/Windstorm-Institute/escrow-spacetime) *(5th in track; translation of standard GR results into the escrow vocabulary; companion to Paper 11)* | [10.5281/zenodo.20126091](https://doi.org/10.5281/zenodo.20126091) |
| 15 | [The 𝒩<sub>esc</sub> Recipe](https://github.com/Windstorm-Institute/nesc-recipe) *(6th in track; formalizes 𝒩<sub>esc</sub> as a cross-regime function; continuation of Paper 14)* | [10.5281/zenodo.20145106](https://doi.org/10.5281/zenodo.20145106) |
| 16 | [The Compton Corollary](https://github.com/Windstorm-Institute/compton-corollary) | [10.5281/zenodo.20163451](https://doi.org/10.5281/zenodo.20163451) |

**Website:** [windstorminstitute.org](https://windstorminstitute.org)

---

*Code: MIT License · Data: CC BY 4.0*
