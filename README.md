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
- `figures/` - six numbered paper figures: workflow, marker measurement, layout, detailed pipeline, quartic curves, and front-oblique camera/3D illustration.
- `evidence/public/` - eight field documentation photograph derivatives; prepared with metadata removal and blurring where a person is visible.
- `videos/` - three face-blurred supplementary inference demos (Videos 2–4) and one additional Video 1 calibration demo; audio-free according to the preparation notes.

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

## Participant privacy and sharing permission

The researcher confirms **oral permission** from adult participants and the parents/guardians of participating children to publish face-blurred research photos/videos on public GitHub, allow downloading, and permit onward redistribution **provided faces remain blurred**. The researcher states that facial blurring was performed. No written/recorded consent evidence was independently reviewed. Blurring reduces, but cannot eliminate, re-identification risk.

The released media are restored as the **identical Git objects** previously published in this repository; unblurred source videos are not provided. Earlier preparation notes describe pixelating the upper 45% of detected person boxes and removing audio. No independent frame-by-frame privacy audit was carried out for this restoration. See [MEDIA_SHARING.md](MEDIA_SHARING.md) for the precise scope and remaining limitations.

## Licensing and repository history

A prior AI coding agent automatically selected CC BY 4.0 for data/media and MIT for code; those were **not explicit final author license decisions**. The license files have been removed from the current branch, but their historical presence and any rights previously granted **cannot be undone retroactively**. No new blanket CC BY 4.0 license is asserted by this update. The reported permission to download and redistribute blurred media does not automatically authorize unblurring, distribution of raw videos, or all other reuse. Licensing for numerical data, documentation and code awaits a conscious author decision. See [LICENSE_STATUS.md](LICENSE_STATUS.md) and [LICENSING.md](LICENSING.md).

Cite the manuscript through [CITATION.cff](CITATION.cff); the paper DOI is not assigned yet.
