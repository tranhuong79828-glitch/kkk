"""
Kịch bản khảo sát hiệu năng 3 quy mô Q1, Q2, Q3 (DT032)
Phục vụ Bảng 4.4 trong Báo cáo Đồ án.
Sinh viên: Trần Minh Khang - MSSV: N24DCDT036
"""

import sys
import os
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from src.subset_sum import liet_ke_tap, liet_ke_tap_quay_lui


def run_benchmarks():
    configs = [
        {"name": "Q1 (Nhỏ)", "n": 8, "S": 15},
        {"name": "Q2 (Vừa)", "n": 14, "S": 35},
        {"name": "Q3 (Lớn)", "n": 18, "S": 50},
    ]

    print("=" * 85)
    print(f"{'Quy mô':<10} | {'(n, S)':<10} | {'Số nghiệm':<10} | {'Sinh NP (ms)':<14} | {'Quay lui (ms)':<14} | {'Tỷ lệ duyệt QL/NP':<18}")
    print("=" * 85)

    results = []
    for cfg in configs:
        n, S = cfg["n"], cfg["S"]
        
        # Đo thuật toán 1: Sinh kế tiếp xâu nhị phân
        t0 = time.perf_counter()
        cac_tap_bin, tk_bin = liet_ke_tap(n, S)
        t_bin = (time.perf_counter() - t0) * 1000.0  # ms
        
        # Đo thuật toán 2: Quay lui có cắt nhánh
        t0 = time.perf_counter()
        cac_tap_ql, tk_ql = liet_ke_tap_quay_lui(n, S)
        t_ql = (time.perf_counter() - t0) * 1000.0  # ms
        
        # Kiểm tra tính đúng đắn đồng nhất
        assert cac_tap_bin == cac_tap_ql, f"Lỗi không khớp kết quả tại n={n}, S={S}"
        
        so_nghiem = len(cac_tap_bin)
        so_nut_ql = tk_ql["so_nut_da_duyet"]
        so_nut_np = tk_bin["so_cau_hinh_da_duyet"]
        ty_le = (so_nut_ql / so_nut_np) * 100.0

        print(f"{cfg['name']:<10} | ({n}, {S}){' '*(5-len(str(n))-len(str(S)))} | {so_nghiem:<10} | {t_bin:>10.2f} ms | {t_ql:>10.2f} ms | {so_nut_ql}/{so_nut_np} ({ty_le:>5.1f}%)")
        results.append({
            "name": cfg["name"],
            "n": n,
            "S": S,
            "so_nghiem": so_nghiem,
            "t_bin": t_bin,
            "t_ql": t_ql,
            "nut_np": so_nut_np,
            "nut_ql": so_nut_ql,
            "ty_le": ty_le
        })
        
    print("=" * 85)
    return results


if __name__ == "__main__":
    run_benchmarks()
