"""
Kịch bản xuất bảng lần vết chi tiết cho ca n=5, S=5 (DT032)
Phục vụ Bảng 3.3 và minh chứng Rubric C2, C3 trong Báo cáo Đồ án.
Sinh viên: Trần Minh Khang - MSSV: N24DCDT036
"""

import sys
import os

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from src.subset_sum import tong_tap, tap_tu_bit, sinh_ke_tiep


def generate_trace():
    n = 5
    S = 5
    x = [0] * n
    step = 0
    
    rows = []
    print("=" * 80)
    print(f"BẢNG LẦN VẾT CHI TIẾT THUẬT TOÁN SINH NHỊ PHÂN VỚI n = {n}, S = {S}")
    print("=" * 80)
    print(f"{'Bước':<5} | {'Cấu hình bit x':<16} | {'Tập con trích xuất':<18} | {'Tổng':<6} | {'Quyết định'}")
    print("-" * 80)

    while True:
        step += 1
        t_val = tong_tap(x)
        subset = tap_tu_bit(x)
        subset_str = str(subset) if subset else "∅ (Tập rỗng)"
        bit_str = str(x)
        
        if t_val == S:
            decision = f"GIỮ (Nghiệm: {subset})"
        else:
            decision = f"BỎ ({t_val} != {S})"

        print(f"{step:<5} | {bit_str:<16} | {subset_str:<18} | {t_val:<6} | {decision}")
        rows.append((step, bit_str, subset_str, t_val, decision))
        
        if not sinh_ke_tiep(x):
            break

    print("=" * 80)
    print(f"Tổng số cấu hình đã duyệt: {step}")
    print(f"Các tập con thỏa mãn tổng bằng {S}:")
    kept = [r[2] for r in rows if "GIỮ" in r[4]]
    for idx, s in enumerate(kept, start=1):
        print(f"  Nghiệm {idx}: {s}")
    print("=" * 80)
    return rows


if __name__ == "__main__":
    generate_trace()
