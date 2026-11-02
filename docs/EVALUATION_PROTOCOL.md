# Evaluation protocol

## Event sample and split

The final personal-quartic results contain 36 marker crossings per video: four study-specific participant models times nine markers. Supplementary Data 1 has 144 rows across Videos 1-4. Video 1 is in-sample; the same 36 events are used for fitting and evaluation. The four participant-specific coefficients are frozen for Videos 2-4; no test-video refit is performed.

Video 1 crossing frames are visually reviewed. Video 2-4 candidate events are selected automatically and are not visually confirmed event-by-event. Their reported errors therefore cover the selected pipeline, including automatic participant-to-track association and event selection. Mapping accuracy and event-selection sensitivity are not independent metrics in the paper.

## Metrics

For event error `e_i = prediction_i - ground_truth_i`:

- MAE = mean(abs(e_i)).
- RMSE = sqrt(mean(e_i^2)).
- Bias = mean(e_i); a negative bias indicates underestimation.
- AbsRel = mean(abs(e_i) / ground_truth_i).
- R^2 = 1 - SSE/SST on the event sample for each video.
- `|e| <= 5 m` and `|e| <= 10 m` counts are descriptive hit-rate summaries, not classifier accuracy or pre-registered acceptance criteria.

## Final personal-model aggregates

| Video | N | MAE (m) | RMSE (m) | Bias (m) | AbsRel | R^2 | <=5 m | <=10 m | Negative predictions |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Video 1 | 36 | 6.220 | 7.109 | 0.000 | 0.266 | 0.826 | 12/36 | 32/36 | 1 |
| Video 2 | 36 | 6.174 | 7.370 | -1.940 | 0.244 | 0.813 | 18/36 | 30/36 | 0 |
| Video 3 | 36 | 6.175 | 7.543 | -1.679 | 0.246 | 0.804 | 17/36 | 29/36 | 0 |
| Video 4 | 36 | 5.901 | 6.766 | -0.618 | 0.247 | 0.842 | 14/36 | 32/36 | 0 |

One Video 1 in-sample prediction is negative. It is retained; negative outputs are not clipped or omitted from the CSV.

## Marker M09

M09 ground truth is 59.4 m. Pooled M09 MAE/RMSE are Video 2: 15.086/15.153 m; Video 3: 14.389/14.572 m; Video 4: 12.719/12.726 m. Data 2 class estimates are rounded to 0.001 m while pooled values use full-precision evaluator outputs. Recalculation from rounded class rows can differ by under 0.001 m and is not a data correction.
