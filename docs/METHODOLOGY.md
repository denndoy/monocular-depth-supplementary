# Methodology summary

This summary reflects the final manuscript/evaluator scope; it is not a replacement for the private end-to-end pipeline.

## Setup and participants

The study uses four recorded participants represented by study-specific IDs S01-S04 and model IDs `class_0`-`class_3`. A fixed smartphone camera records a lane nominally 6 m wide. Nine longitudinal markers M01-M09 are spaced at nominal 6.6 m intervals, from 6.6 m to 59.4 m. These four participants do not constitute a population sample and do not establish generalization to unseen participants or cameras.

## Detection, tracking, and feature

A fine-tuned YOLOv8n person detector runs with 1280-pixel input and confidence threshold 0.05. ByteTrack associates detections over frames. The numerical feature is geometric bbox area `A_bb_px2 = width_px * height_px` in px^2; detector coordinates can be floating-point. It is a rectangle-area proxy, not foreground segmentation or a discrete raster-pixel count.

Video 1 participant-to-track associations are reviewed. For Videos 2-4, four high-count tracks are associated automatically with the known participants. Videos 2-3 use a near-camera bbox-height fallback; Video 4 uses a gender classifier with near-camera bbox height. The classifier is not a direct quartic input, but can affect participant-model selection in Video 4. Mapping accuracy is not independently evaluated.

## Personal quartic model

Four separate degree-4 polynomials are fit on Video 1, with nine marker events per participant. Each participant's bbox area is normalized by the mean and population standard deviation of their nine Video 1 calibration events. The fitted estimate is constrained to be non-increasing with area over the observed class-specific calibration range. Video 1 is in-sample because the same 36 events are used for fitting and evaluation. Coefficients are frozen for Videos 2-4 without refitting. The evaluator imposes no positivity bound and does not clip negative predictions.

## Inference and event evaluation

Model inference is generated frame-wise for detected/mapped tracks. Ground truth is available only at marker crossings, so reported quantitative distance metrics use those event samples, not continuous per-frame ground truth. Video 1 crossings are visually reviewed. Videos 2-4 use automatically selected candidate events that are not visually confirmed event-by-event. Test metrics therefore describe a pipeline that includes participant association, event selection, and quartic inference; mapping accuracy and candidate-selection sensitivity are not separately measured.

## 3D illustration

The demonstration maps longitudinal estimates to compressed display depth and approximate lateral position. Lateral position is schematic, not an independently calibrated coordinate. Invalid/out-of-domain predictions are not presented as valid 3D placements; raw predictions remain available in the event data.
