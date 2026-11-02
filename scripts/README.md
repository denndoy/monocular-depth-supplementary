# Metric verification script

`verify_supplementary_metrics.py` uses only Python's standard library. It reads the two released CSV files, checks headers, event counts, unique keys, prediction/error consistency, bbox-area aliases, and recomputes metrics supported by the files. It does not access the network, run detection/tracking, train models, or write files.

Run from the repository root with `python scripts/verify_supplementary_metrics.py`.
