# Scope and reproducibility status

## Source and packaging

Thirteen source notebooks were selected from read-only copies of the author's
analysis directory obtained on 2026-10-19, yielding fourteen plotting notebooks.
The final combined source `figure8.ipynb` was split into independent Figure 8
(Labrador Sea) and Figure 9 (Southern Ocean) notebooks at the author's request.
Both include source cells 0-4 for loading data; Figure 8 adds source cell 6 and
Figure 9 adds source cell 5 (zero-based). The superseded source `figure9.ipynb`
is not used. Per-file SHA-256 checksums, selected source-cell indices, and code digests
are recorded in `provenance.json`. The original server notebooks were not
modified.

Packaging changes are restricted to:

- Removing stored cell outputs, execution counts, attachments, transient cell
  metadata, and notebook widgets.
- Replacing the custom kernel name with a generic Python 3 kernel.
- Selecting the existing regional plotting cells and duplicating the shared
  data-loading cells to make Figures 8 and 9 independently runnable.
- Adding a short purpose/scope header and an initial shared-configuration cell.
- Replacing input, output, work-directory, and font path literals with calls to
  `configured_path`. The path-location blocks in S2 and S6-S7 are adapted to the
  same configuration.
- Adding documentation, dependency/configuration examples, and static checks.

No scientific calculations, filtering criteria, train/validation assignments,
metrics, coordinate/date processing, smoothing, regional limits, statistical
envelopes, color scales, or figure-export settings were deliberately changed.
Exploratory cells in the other notebooks are retained. Source-code equivalence
for the selected cells outside the documented path substitutions was checked
during packaging. No claim is made that an
unexecuted source notebook is free from analysis or data-dependent errors.

## Verification limits

Static checks cover JSON structure, Python syntax, empty outputs and execution
counts, generic kernel selection, configuration keys, residual server paths,
common credential patterns, file checksums, and the intended file inventory.
They do not execute notebook code or import the scientific packages.

Original notebook metadata reports Python 3.9.18. Package versions from the
environment that generated the final manuscript figures have not been
established. `requirements.txt` lists direct dependencies, plus NetCDF/Dask and
Jupyter support, and is not a tested lockfile. A clean-environment run with the
exact inputs is still needed before describing the release as fully
reproducible.

The final public MLD product has a different scope from the evaluation inputs.
In particular, it does not include the WOD-derived reference, train/validation
membership, station records, third-party climatologies, or profile counts.
Availability of those figure inputs must be resolved separately. No data,
weights, credentials, font files, or manuscript documents are included here.

## Repository and data identifiers

Code repository: https://github.com/haolin111/SJTU-ViT-MLD.
The code is distributed under the MIT License, Copyright (c) 2026 Haolin Xu.

The associated SJTU-ViT MLD data product (version 1.0) is archived at
https://doi.org/10.5281/zenodo.23463931 under the Creative Commons Attribution
4.0 International (CC BY 4.0) licence. This DOI identifies the data product,
not the plotting software. No separate software DOI has been assigned.
Record the exact Git commit used for reproducibility. If a software archive
is created later, its software DOI and citation metadata should be added
separately.

Availability of the additional figure inputs remains distinct from access
to this code and to the public MLD product. Consult DATA_REQUIREMENTS.md
before attempting to reproduce the figures.
