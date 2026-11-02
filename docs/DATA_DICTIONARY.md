# Data dictionary

The two CSV files are released in `data/`. Column names below are read from the actual files.

## Supplementary Data 1: event-level results

One row is one selected participant/class-marker-video crossing event (144 rows total; 36 per video).

| Column | Meaning | Unit / type |
|---|---|---|
| `video` | Video label, Video 1-4 | categorical string |
| `class_id` | One of four study-specific participant model IDs | categorical string |
| `participant_category` | Category encoded in the source results | participant-linked categorical string |
| `marker_id` | Ground-truth marker M01-M09 | categorical string |
| `frame_idx` | Source inference frame index for the selected crossing event | integer index |
| `gt_distance_m` | Longitudinal marker ground truth | m |
| `N_bb_bbox_pixel_count` | Legacy feature label for the rectangular bbox-area proxy; not foreground segmentation | px^2 |
| `A_bb_px2_source_value` | Geometric bounding-box area from width times height | px^2 |
| `z_normalized` | Participant-specific normalized bbox area | dimensionless |
| `in_calibration_feature_range` | Whether bbox area falls in that class's Video 1 calibration range | boolean |
| `method` | Model-family identifier | categorical string |
| `estimate_distance_m` | Raw quartic output | m |
| `signed_error_m` | Prediction minus ground truth | m |
| `absolute_error_m` | Absolute signed error | m |
| `metric_scope` | In-sample or frozen-test scope recorded for the row | string |

`N_bb_bbox_pixel_count` and `A_bb_px2_source_value` are equal in this CSV and represent the geometric bounding-box rectangle area. It is not a discrete raster-pixel count or segmented foreground area.

## Supplementary Data 2: M09 results

| Column | Meaning | Unit / type |
|---|---|---|
| `Video` | Video 2-4 label | categorical string |
| `Kelas` | Four participant-specific class labels or `pooled across four classes` | categorical string |
| `GT_M09_m` | M09 ground truth; blank in pooled rows | m |
| `Estimated_distance_m` | Participant-specific prediction; blank in pooled rows | m |
| `Absolute_error_m` | Participant-specific absolute error; blank in pooled rows | m |
| `Pooled_MAE_m` | Pooled MAE across the four class predictions at M09 | m |
| `Pooled_RMSE_m` | Pooled RMSE across the four class predictions at M09 | m |

Data 2 contains 12 class rows (four classes times Videos 2-4) and three pooled-summary rows. M09 ground truth is 59.4 m. Class predictions are rounded to 0.001 m; pooled metrics use full-precision evaluator predictions, so recomputing from the displayed class rows can differ by less than 0.001 m.
