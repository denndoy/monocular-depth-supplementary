#!/usr/bin/env python3
"""Verify the two local supplementary CSVs without external dependencies."""
from __future__ import annotations
import csv
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA1 = ROOT / "data" / "Supplementary_Data_1_Event_Level_Results.csv"
DATA2 = ROOT / "data" / "Supplementary_Data_2_M09_Per_Class_Results.csv"
ROUNDING_TOL = 0.00051
M09_ROUNDED_ROW_TOL = 0.0011
EXPECTED = {
    "Video 1": (6.220, 7.109),
    "Video 2": (6.174, 7.370),
    "Video 3": (6.175, 7.543),
    "Video 4": (5.901, 6.766),
}
EXPECTED_M09 = {
    "Video 2": (15.086, 15.153),
    "Video 3": (14.389, 14.572),
    "Video 4": (12.719, 12.726),
}

def read_rows(path: Path):
    if not path.is_file():
        raise FileNotFoundError(f"Local review input missing: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def near(a: float, b: float, tol: float = ROUNDING_TOL) -> bool:
    return abs(a - b) <= tol

def verify_data1():
    rows = read_rows(DATA1)
    required = {
        "video", "class_id", "participant_category", "marker_id", "frame_idx",
        "gt_distance_m", "N_bb_bbox_pixel_count", "A_bb_px2_source_value",
        "z_normalized", "in_calibration_feature_range", "method",
        "estimate_distance_m", "signed_error_m", "absolute_error_m", "metric_scope",
    }
    if not rows or not required.issubset(rows[0]):
        raise ValueError(f"Data 1 header missing: {sorted(required - set(rows[0] if rows else []))}")
    if len(rows) != 144:
        raise ValueError(f"Data 1 has {len(rows)} rows, expected 144")
    groups = defaultdict(list)
    seen = set()
    for row in rows:
        key = (row["video"], row["class_id"], row["marker_id"])
        if key in seen:
            raise ValueError(f"Duplicate event key: {key}")
        seen.add(key)
        gt = float(row["gt_distance_m"])
        pred = float(row["estimate_distance_m"])
        err = float(row["signed_error_m"])
        abs_err = float(row["absolute_error_m"])
        if not near(pred - gt, err, 1.1e-8) or not near(abs(err), abs_err, 1.1e-8):
            raise ValueError(f"Error-field inconsistency at {key}")
        area1 = float(row["N_bb_bbox_pixel_count"])
        area2 = float(row["A_bb_px2_source_value"])
        if not near(area1, area2, 1.1e-8):
            raise ValueError(f"BBox area fields differ at {key}")
        groups[row["video"]].append((gt, pred, err))
    if set(groups) != set(EXPECTED):
        raise ValueError(f"Unexpected video labels: {sorted(groups)}")
    for video, records in groups.items():
        if len(records) != 36:
            raise ValueError(f"{video} has {len(records)} events, expected 36")
        video_rows = [r for r in rows if r["video"] == video]
        if len({r["class_id"] for r in video_rows}) != 4 or len({r["marker_id"] for r in video_rows}) != 9:
            raise ValueError(f"{video} must contain four classes and nine markers")
        gt = [r[0] for r in records]
        pred = [r[1] for r in records]
        err = [r[2] for r in records]
        mae = math.fsum(abs(e) for e in err) / 36
        rmse = math.sqrt(math.fsum(e * e for e in err) / 36)
        bias = math.fsum(err) / 36
        absrel = math.fsum(abs(e) / d for e, d in zip(err, gt)) / 36
        mean_gt = math.fsum(gt) / 36
        sst = math.fsum((d - mean_gt) ** 2 for d in gt)
        r2 = 1.0 - math.fsum(e * e for e in err) / sst
        hit5 = sum(abs(e) <= 5 for e in err)
        hit10 = sum(abs(e) <= 10 for e in err)
        negative = sum(p < 0 for p in pred)
        expected_mae, expected_rmse = EXPECTED[video]
        if not near(mae, expected_mae) or not near(rmse, expected_rmse):
            raise ValueError(f"{video} MAE/RMSE mismatch: {mae:.6f}/{rmse:.6f}")
        print(f"PASS {video}: N=36 MAE={mae:.6f} RMSE={rmse:.6f} Bias={bias:.6f} "
              f"AbsRel={absrel:.6f} R2={r2:.6f} hit5={hit5}/36 hit10={hit10}/36 negative={negative}")

def verify_data2():
    rows = read_rows(DATA2)
    required = {"Video", "Kelas", "GT_M09_m", "Estimated_distance_m", "Absolute_error_m", "Pooled_MAE_m", "Pooled_RMSE_m"}
    if not rows or not required.issubset(rows[0]):
        raise ValueError(f"Data 2 header missing: {sorted(required - set(rows[0] if rows else []))}")
    if len(rows) != 15:
        raise ValueError(f"Data 2 has {len(rows)} rows, expected 15")
    event_rows = [r for r in rows if r["Kelas"] != "pooled across four classes"]
    pooled_rows = [r for r in rows if r["Kelas"] == "pooled across four classes"]
    if len(event_rows) != 12 or len(pooled_rows) != 3:
        raise ValueError(f"Expected 12 class rows and 3 pooled rows, found {len(event_rows)} and {len(pooled_rows)}")
    for video, (expected_mae, expected_rmse) in EXPECTED_M09.items():
        group = [r for r in event_rows if r["Video"] == video]
        if len(group) != 4 or len({r["Kelas"] for r in group}) != 4:
            raise ValueError(f"{video} must contain four unique class rows")
        errors = []
        for r in group:
            gt = float(r["GT_M09_m"])
            estimate = float(r["Estimated_distance_m"])
            abs_error = float(r["Absolute_error_m"])
            if not near(gt, 59.4, 1e-9):
                raise ValueError(f"{video} M09 ground truth is not 59.4 m")
            if not near(abs(estimate - gt), abs_error, 1.1e-3):
                raise ValueError(f"{video} M09 class error inconsistency")
            errors.append(estimate - gt)
        recomputed_mae = math.fsum(abs(e) for e in errors) / 4
        recomputed_rmse = math.sqrt(math.fsum(e * e for e in errors) / 4)
        pooled = next((r for r in pooled_rows if r["Video"] == video), None)
        if pooled is None:
            raise ValueError(f"{video} pooled summary row missing")
        stored_mae = float(pooled["Pooled_MAE_m"])
        stored_rmse = float(pooled["Pooled_RMSE_m"])
        if not near(stored_mae, expected_mae) or not near(stored_rmse, expected_rmse):
            raise ValueError(f"{video} pooled metrics differ from reported M09 values")
        # Class-level estimates are rounded to 0.001 m; pooled evaluator values use full precision.
        if not near(recomputed_mae, stored_mae, M09_ROUNDED_ROW_TOL) or not near(recomputed_rmse, stored_rmse, M09_ROUNDED_ROW_TOL):
            raise ValueError(f"{video} M09 rounded-row recomputation exceeds tolerance")
        print(f"PASS {video} M09: GT=59.4 m pooled MAE={stored_mae:.3f} RMSE={stored_rmse:.3f}; "
              f"rounded-row recomputation={recomputed_mae:.6f}/{recomputed_rmse:.6f}")

def main():
    verify_data1()
    verify_data2()
    print("PASS all supplementary checks; no files written")

if __name__ == "__main__":
    main()
