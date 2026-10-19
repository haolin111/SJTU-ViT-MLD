# Data requirements

No data are bundled with this candidate code repository. Paths are configured
in `config.json`, using `config.example.json` as a template. Each dataset must
be obtained under its own access and reuse terms; pointing to a file in the
configuration does not grant redistribution rights.

## Evaluation and gridded comparisons

| Configuration key | Expected file or content | Used by |
| --- | --- | --- |
| `training_pairs_file` | Original `mld_preds_80train.nc`, containing `MLD_true` and `MLD_pred` | Fig. 2 |
| `validation_pairs_file` | Original `mld_preds_20val.nc`, containing `MLD_true` and `MLD_pred` | Fig. 2 |
| `paired_mld_file` | Analysis `mld_preds_final10.nc`, containing paired `MLD_pred` and `MLD_true` fields on the original analysis coordinates | Figs. 3-9; S3-S5 |
| `reccap_mask_file` | `RECCAP2_region_masks_all.nc`, with the `open_ocean` field | Gridded map/regional analyses |
| `argo_climatology_file` | `Argo_mixedlayers_monthlyclim_04142022.nc`, density-threshold climatology selected by the notebook | Fig. 5 |
| `de_boyer_climatology_file` | `mld_dr003_ref10m.nc`, with `mld_dr003` | Figs. 5-6 |
| `iap_mld_file` | `IAP_mld003.nc`, MLD derived from the IAP temperature/salinity product | Figs. 7-9 |
| `oras_mld_pattern` | Original ORAS5-derived MLD files selected by a glob | Figs. 7-9 |
| `wod_monthly_mld_file` | `obs_MLD_d003_monthly_grid_1982_2023.nc`, with `MLD_d003` | S1, S6-S7 |
| `wod_profile_dir` | Monthly `MLD_WOD_griddata_YYYY_MM.nc` files with `longitude`, `latitude`, and `MLD_d003` | S1 profile-count calculation |

The paired analysis file is not interchangeable with the final public NetCDF
that contains only `MLD_pred`. Train/validation subset membership cannot be
recovered from that final product. For independent replotting, the exact paired
evaluation inputs or a documented method to reconstruct them must be made
available separately. These inputs have not been approved for redistribution.

The retained code includes dataset-specific variable selection, coordinate
alignment, and time-coordinate assignment. Use the original analysis inputs;
do not replace them with different releases or renamed variables without
checking these assumptions. The collection does not yet automate downloading
or preprocessing the third-party products.

## Station comparisons

| Configuration key | Expected input | Used by |
| --- | --- | --- |
| `bats_profiles_file` | `BAT_merged_processed.csv`, the BATS temperature/salinity profile table used by the original analysis | Fig. 4; S5 |
| `tao_temperature_file` | `t_xyzt_mon.cdf` with `T_20` | Fig. 4; S5 |
| `tao_salinity_file` | `s_xyzt_mon.cdf` with `S_41` | Fig. 4; S5 |
| `hot_source_file` | `aloha_mld.txt`, HOT source table | Fig. 4 HOT preparation |
| `papa_density_file` | `d50n145w_mon.cdf` with `STH_71` | Fig. 4; S5 |
| `sots_mld_file` | `SOTS_monthly_MLD_sigma0_003_2010_2020.nc` | Fig. 4; S5 |
| `pirata_mld_file` | `PIRATA_10S10W_MLD_sigma0_003_monthly_2010_2020.nc` | Fig. 4; S5 |

`figure4.ipynb` writes `HOT_MLD_clean.csv` and `HOT_MLD_clean.nc` to `work_dir`.
`s5figure.ipynb` reads that same generated NetCDF. Run the preparation first, or
provide the verified precomputed file at that location. Both notebooks retain
the source-specific station workflows and four-neighbor sampling as written.
They do not establish that station records are independent of the WOD training
observations.

`s1figure.ipynb` writes `MLD_profile_counts_1982_2023.nc` to `work_dir`.
`s6s7figure.ipynb` reads that file's `profile_count_all` variable. The S1 loop
skips missing monthly profile files, as in the source; complete inputs and the
expected coverage must be checked before interpreting regenerated counts.

## Paths, fonts, and outputs

`font_dir` must contain legally obtained regular and bold Times New Roman TTF
files. They are deliberately not bundled. The original notebooks require these
fonts and check that Matplotlib resolves to them. `output_dir` receives figure
PNGs; `work_dir` receives generated station/profile-count intermediates. These
directories are created when those configuration keys are first requested.
Running the notebooks can overwrite files with the same output names, so use
dedicated output and work directories.
