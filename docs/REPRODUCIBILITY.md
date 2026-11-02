# Reproducibility limits

The released CSVs allow recalculation of headline marker-event metrics with `scripts/verify_supplementary_metrics.py` and Python's standard library. The verifier does not train models, access the network, or write files.

This repository does not include original participant videos, detector/classifier checkpoints, private annotation sources, complete job directories, or environment-specific pipeline inputs. It cannot reproduce YOLO detection, ByteTrack tracking, participant mapping, automatic event selection, or end-to-end frame-wise inference. Mapping accuracy and candidate-selection sensitivity were not independently evaluated. Full end-to-end reproduction is therefore not claimed.

CSV rows are participant-linked through four class/category IDs and frame indices. Evidence photos are metadata-stripped derivatives; one has a blurred head/face. The MP4 demonstrations are face-blurred and audio-free. These measures reduce but do not guarantee anonymity. The author confirms permission to release the face-blurred materials; the repository does not independently validate institutional or guardian records.
