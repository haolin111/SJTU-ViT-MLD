# Figure index

Correspondence was checked against the current main manuscript and supplement
captions, and against the notebooks' code and output filenames. This is not a
pixel-level verification of regenerated figures.

## Main text

| Figure | Notebook under `notebooks/main/` | Content | Export |
| --- | --- | --- | --- |
| 2 | `figure2.ipynb` | Training/withheld-validation density scatterplots | `figure2.png` |
| 3 | `figure3.ipynb` | Maximum monthly climatological MLD, difference, and correlation maps | `figure3.png` |
| 4 | `figure4.ipynb` | Six-station MLD time-series comparison | `figure4.png` |
| 5 | `figure5.ipynb` | Seasonal climatologies: SJTU-ViT, Argo, and de Boyer Montegut | `figure5.png` |
| 6 | `figure6.ipynb` | Seasonal meridional profiles in three ocean basins | `figure6.png` |
| 7 | `figure7.ipynb` | Four regional climatological seasonal cycles | `figure7.png` |
| 8 | `figure8.ipynb` | Labrador Sea maps and regional time series | `figure8.png` |
| 9 | `figure9.ipynb` | Southern Ocean maps and regional time series | `figure9.png` |

The final combined source `figure8.ipynb` was split at the author's request.
Each new notebook contains its own configuration and shared data-loading cells,
followed by just its corresponding regional plotting cell. Run either one in
a fresh kernel; neither requires the other notebook to be run first. Figure 8
uses the original source cells 0-4 and 6, and Figure 9 uses cells 0-5 (zero-based).
The separate old source `figure9.ipynb` is not used. Statistical calculations
and plotting parameters in the selected cells are unchanged.

## Supplement

| Figure | Notebook under `notebooks/supplement/` | Content | Export |
| --- | --- | --- | --- |
| S1 | `s1figure.ipynb` | Spatial/annual counts of valid WOD-derived MLD and all profiles | `s1figure.png` |
| S2 | `s2figure.ipynb` | Locations of the six comparison stations | `s2figure.png` |
| S3 | `s3figure.ipynb` | Annual global MLD bias, standard error, and observation counts | `s3figure.png` |
| S4 | `s4figure.ipynb` | Month of maximum climatological MLD | `s4figure.png` |
| S5 | `s5figure.ipynb` | Six-station monthly climatology with standard-deviation envelopes | `s5figure.png` |
| S6 | `s6s7figure.ipynb` | Labrador Sea observational support | `s6figure.png` |
| S7 | `s6s7figure.ipynb` | Southern Ocean observational support | `s7figure.png` |

Run each notebook from top to bottom with a fresh kernel. Some notebooks also
display exploratory or alternative plots before exporting the final figure;
these cells have been retained to avoid changing the source analysis. S5's
last cell exports the version with standard-deviation shading. S6-S7's notebook
exports S7 first and S6 second.
