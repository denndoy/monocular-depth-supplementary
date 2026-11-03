# Reproducibility limits

The released CSVs allow recalculation of headline marker-event metrics with `scripts/verify_supplementary_metrics.py` and Python's standard library. The verifier does not train models, access the network, or write files.

This repository does not include original participant videos, detector/classifier checkpoints, private annotation sources, complete job directories, or environment-specific pipeline inputs. It cannot reproduce YOLO detection, ByteTrack tracking, participant mapping, automatic event selection, or end-to-end frame-wise inference. Mapping accuracy and candidate-selection sensitivity were not independently evaluated. Full end-to-end reproduction is therefore not claimed.

CSV rows are linked to four known participants through study-specific class/category IDs and event frame indices; no names are included. Participant recordings, setup photographs and video-frame figure images are withheld from the current branch. The author reports oral consent for face-blurred use, but unrestricted third-party redistribution rights have not been established. Earlier public Git commits included media; moving this branch forward does not purge the history. A new public repository from a clean history is recommended.
