# Supplementary Materials

**Paper:** MONOCULAR DEPTH ESTIMATION USING A QUARTIC FUNCTION OF OBJECT PIXEL COUNT
**Authors:** Dandy Tri Widianto; Mohammad Nasucha
**Repository:** https://github.com/denndoy/monocular-depth-supplementary

## Overview

This study estimates pedestrian longitudinal distance from monocular RGB video. A fine-tuned YOLOv8n person detector and ByteTrack produce frame-wise detections and tracks. The numeric model input is geometric bounding-box area `width_px * height_px` in px^2, not a foreground-segmentation pixel count. Four participant-specific degree-4 quartics are calibrated on Video 1 under a non-increasing constraint over observed calibration-area ranges; coefficients are frozen for Video 2-4.

Inference is frame-wise, but quantitative distance metrics use marker-crossing events with ground truth. Video 1 is in-sample: the same 36 events are used for fitting and evaluation. Videos 2-4 use 36 automatically selected candidates per video without refit or manual event-by-event visual confirmation. Test metrics therefore describe a pipeline including participant-to-track association, event selection, and quartic estimation; mapping accuracy and event-selection sensitivity were not independently measured.

## Contents

- `data/Supplementary_Data_1_Event_Level_Results.csv` - 144 marker-crossing rows (36 per video).
- `data/Supplementary_Data_2_M09_Per_Class_Results.csv` - 12 class-level M09 rows plus three pooled summary rows.
- `docs/` - data dictionary, methodology, evaluation protocol, provenance, reproducibility limits, and index.
- `scripts/verify_supplementary_metrics.py` - standard-library metric and integrity verifier.
- `figures/Fig_1_...png` through `Fig_5_...png` - figures extracted from the author-supplied final manuscript. Fig. 5 uses the approved front-oblique view.
- `evidence/` - eight documentation-photo derivatives; GPS/EXIF metadata removed, and the visible person's head/face blurred in the affected image. Unmodified source photos are not distributed.
- `videos/` - three official manuscript supplementary videos for Videos 2-4, plus one additional Video 1 in-sample calibration demo. All are face-blurred and audio-free.

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

The evaluation covers four recorded participants and one fixed-camera setup. It does not establish generalization to new participants/cameras, mapping accuracy, event-selection sensitivity, or continuous per-frame distance accuracy. The 3D display compresses depth and approximates lateral position; it is illustrative, not independently calibrated 3D localization.

## Privacy and reuse

The author authorized release of the face-blurred participant materials. Evidence-photo derivatives have EXIF/GPS metadata removed, and the photo containing a person has the head/face region blurred. These measures reduce but do not guarantee anonymity; backgrounds may still make the site recognizable. Unmodified originals are not included. The author also states the release is authorized; the repository does not independently validate institutional/guardian records.

Data, documentation, figures, sanitized evidence photographs, and video assets are licensed CC BY 4.0 (`LICENSE`). `scripts/verify_supplementary_metrics.py` is MIT-licensed (`scripts/LICENSE`). These licenses do not themselves grant privacy/personality rights. Cite the manuscript as specified in `CITATION.cff`; DOI and final publication metadata were not assigned in this release.
