# Data provenance

The released CSV files are byte-identical copies of the final supplementary project files. No row, field, precision, or value was changed.

| Released file | Source path relative to research project | Rows excluding header | SHA-256 |
|---|---|---:|---|
| `data/Supplementary_Data_1_Event_Level_Results.csv` | `docs/Supplementary_Data_1_Event_Level_Results.csv` | 144 | `ad22dd9b13afe7d1f6fffa9b5b44c414ae107cbfd00038c064903d0644e920eb` |
| `data/Supplementary_Data_2_M09_Per_Class_Results.csv` | `docs/Supplementary_Data_2_M09_Per_Class_Results.csv` | 15 | `0e810f56bc87c82459977dfc67b683907359bae8e6ef64d1269107e803a9002a` |

Cross-checks used the final evaluator artifacts in `outputs/distance_polynomial/v2_final_monotone_quartics/` and source `scripts/04_distance_evaluation/evaluate_final_monotone_quartics.py`. The full evaluator, fitted model bundle, and raw job directories are not included. All eight evidence photos were copied to `evidence/public/` as sanitized derivatives; GPS/EXIF was stripped and the one visible person's head/face was blurred. Their originals remain private and are not distributed.
