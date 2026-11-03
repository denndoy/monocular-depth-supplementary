# Data provenance

The released CSVs contain the same rows, fields, precision, and values as the corresponding final supplementary project files. The Data 1 source file uses CRLF line endings while the public release uses LF; after CSV parsing all 144 data rows are identical. Data 2 is byte-identical.

| Released file | Source path relative to research project | Rows excluding header | SHA-256 (public release) | SHA-256 (local source) |
|---|---|---:|---|---|
| `data/Supplementary_Data_1_Event_Level_Results.csv` | `docs/Supplementary_Data_1_Event_Level_Results.csv` | 144 | `062ec3d1e0d4f060ca28dbb97f335a715201b78a5760f59b98ae337872970fbb` | `ad22dd9b13afe7d1f6fffa9b5b44c414ae107cbfd00038c064903d0644e920eb` |
| `data/Supplementary_Data_2_M09_Per_Class_Results.csv` | `docs/Supplementary_Data_2_M09_Per_Class_Results.csv` | 15 | `0e810f56bc87c82459977dfc67b683907359bae8e6ef64d1269107e803a9002a` | `0e810f56bc87c82459977dfc67b683907359bae8e6ef64d1269107e803a9002a` |

Cross-checks used the final evaluator artifacts in `outputs/distance_polynomial/v2_final_monotone_quartics/` and source `scripts/04_distance_evaluation/evaluate_final_monotone_quartics.py`. The full evaluator, fitted model bundle, and raw job directories are not included. Four face-blurred demo MP4s, eight privacy-processed field JPGs and two images containing field/video content were restored as their byte-identical earlier Git blobs after the researcher confirmed oral permission for public download and redistribution of face-blurred versions. No independent full-frame privacy audit was conducted. Original unblurred source footage remains private; see `MEDIA_SHARING.md`.
