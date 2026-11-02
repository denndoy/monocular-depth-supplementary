# Supplementary videos

Four face-blurred, audio-free MP4s are provided. The manuscript's Supplementary Videos 1-3 correspond to inference Videos 2-4. An additional Video 1 in-sample calibration demo is included separately.

| File | Source video | Duration | Resolution | FPS | Bytes |
|---|---|---:|---:|---:|---:|
| `Supplementary_Video_1_Video_2_Inference.mp4` | Video 2 | 69.32 s | 1920x960 | 25.014 | 30,608,421 |
| `Supplementary_Video_2_Video_3_Inference.mp4` | Video 3 | 50.04 s | 1920x960 | 25.020 | 20,389,706 |
| `Supplementary_Video_3_Video_4_Inference.mp4` | Video 4 | 50.84 s | 1920x960 | 25.020 | 23,722,390 |
| `Additional_Video_Video_1_Calibration_InSample.mp4` | Video 1 | 28.62 s | 1920x960 | 30.017 | 9,795,048 |

The generation pipeline pixelates the upper 45% of detector person boxes on every frame and omits audio. Start/middle/end frames were spot-checked. Face blurring reduces, but does not eliminate, re-identification risk. The demonstrations show frame-wise inference; quantitative ground-truth metrics remain marker-event-level. Depth is compressed and lateral position is schematic. The video assets are CC BY 4.0 under the author's selection; see the root `LICENSE`.
