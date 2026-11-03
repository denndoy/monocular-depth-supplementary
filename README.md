# Supplementary Materials

**Paper:** MONOCULAR DEPTH ESTIMATION USING A QUARTIC FUNCTION OF OBJECT PIXEL COUNT
**Authors:** Dandy Tri Widianto; Mohammad Nasucha
**Repository:** https://github.com/denndoy/monocular-depth-supplementary

## Overview

This study estimates pedestrian longitudinal distance from monocular RGB video. Four participants (two adults and two young children; one male and one female in each group) were recorded using a fixed POCO F3 smartphone camera on a tripod, with the lens approximately 150 cm above ground. The lane is 6 m wide and nine longitudinal markers span 6.6-59.4 m. A fine-tuned YOLOv8n person detector and ByteTrack produce frame-wise detections and tracks. The numeric model input is geometric bounding-box area `width_px * height_px` in px^2, not a foreground-segmentation pixel count. Four participant-specific degree-4 quartics are calibrated on Video 1 under a non-increasing constraint over observed calibration-area ranges; coefficients are frozen for Video 2-4. No additional participant recruitment criteria are documented; this cohort is not a population sample.

Inference is frame-wise, but quantitative distance metrics use marker-crossing events with ground truth. Video 1 is in-sample: the same 36 events are used for fitting and evaluation. Videos 2-4 use 36 automatically selected candidates per video without refit or manual event-by-event visual confirmation. Test metrics therefore describe a pipeline including participant-to-track association, event selection, and quartic estimation; mapping accuracy and event-selection sensitivity were not independently measured.

## Contents

- `data/Supplementary_Data_1_Event_Level_Results.csv` - 144 marker-crossing rows (36 per video).
- `data/Supplementary_Data_2_M09_Per_Class_Results.csv` - 12 class-level M09 rows plus three pooled summary rows.
- `docs/` - data dictionary, methodology, evaluation protocol, provenance, reproducibility limits, and index.
- `scripts/verify_supplementary_metrics.py` - standard-library metric and integrity verifier.
- `figures/` - non-photographic scientific diagrams and quartic plots (Fig. 1, Fig. 3, Fig. 4 and Fig. 5); photograph/participant-frame images are withheld.
- `evidence/` - documentation only; field photographs have been withheld from the active branch.
- `videos/` - documentation only; Video 1-4 demonstrations have been withheld from the active branch. See the public-release notice below.

## Final personal-quartic results

Metrics are computed on 36 crossing events per video (four participant-specific quartics, nine markers each). Values are in meters except AbsRel and R^2.

| Video | N | MAE | RMSE | Bias | AbsRel | R^2 | <=5 m | <=10 m | Negative predictions |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Video 1 (in-sample) | 36 | 6.220 | 7.109 | 0.000 | 0.266 | 0.826 | 12/36 | 32/36 | 1 |
| Video 2 (frozen inference) | 36 | 6.174 | 7.370 | -1.940 | 0.244 | 0.813 | 18/36 | 30/36 | 0 |
| Video 3 (frozen inference) | 36 | 6.175 | 7.543 | -1.679 | 0.246 | 0.804 | 17/36 | 29/36 | 0 |
| Video 4 (frozen inference) | 36 | 5.901 | 6.766 | -0.618 | 0.247 | 0.842 | 14/36 | 32/36 | 0 |

One Video 1 in-sample prediction is negative and is retained without clipping. At M09, GT is 59.4 m; pooled MAE/RMSE are Video 2: 15.086/15.153 m, Video 3: 14.389/14.572 m, and Video 4: 12.719/12.726 m. Data 2 class predictions are rounded to 0.001 m; pooled metrics use full-precision evaluator outputs.

## Limitations

The evaluation covers four recorded participants and one fixed-camera setup. It does not establish generalization to new participants/cameras, mapping accuracy, event-selection sensitivity, or continuous per-frame distance accuracy. The 3D display compresses depth and approximates lateral position; selected marker-crossing frame/ground-truth pairs anchor avatar depth, with linear interpolation between anchors for display only. This display path is not quartic output, continuous ground truth, a distance metric, or independent 3D localization validation; reported metrics use raw quartic predictions at marker events.

## Privacy, publication and licensing status

**No participant videos, field photographs, or video-frame figure images are included in the current branch tree.** The original research includes two adults and two children. The researcher reports oral consent from adult participants and the children's parents/guardians for use of recordings conditional on blurring faces; blurring was applied. That consent has not been documented as authorization for unrestricted redistribution or third-party reuse, and blurring alone does not guarantee anonymity. Media are withheld from the active branch pending a separate decision.

**IMPORTANT: The original public Git history included four MP4 videos, eight photographs and participant-related figure images, and an agent-applied CC BY 4.0 license. Removing files or license texts from the latest commit does not remove earlier commits, undo downloads, or retroactively revoke licenses potentially relied upon by third parties. This existing repository should be made private, and a new public data-only repository should be created from a clean history. Do not reuse this repository's Git history for that release.**

The earlier CC BY 4.0 and MIT license choices were automatically applied by an AI agent; the researcher has clarified they were not explicitly selected. No replacement open license is being newly offered via this revised branch while authors review licensing. See [LICENSE_STATUS.md](LICENSE_STATUS.md). This notice does not adjudicate previously granted rights.

Cite the associated research using [CITATION.cff](CITATION.cff); a published article DOI has not been assigned. The numerical CSVs and independent metric-verification script remain available for author/reviewer inspection.
