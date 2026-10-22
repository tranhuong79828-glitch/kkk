"""
Chương trình minh họa và chạy thử nghiệm đề tài DT032
Liệt kê tập con có tổng bằng S
Sinh viên: Trần Minh Khang - MSSV: N24DCDT036 - Lớp: D24CQDT01-N
Giảng viên hướng dẫn: ThS. Hồ Nhựt Minh
"""

import sys
import argparse

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from src.subset_sum import liet_ke_tap, liet_ke_tap_quay_lui, kiem_tra_hop_le


def in_ket_qua(n: int, S: int) -> None:
    print(f"\n{'='*60}")
    print(f"KẾT QUẢ CHẠY VỚI n = {n}, S = {S}")
    print(f"{'='*60}")
    
    # Phương pháp 1: Sinh kế tiếp xâu nhị phân
    cac_tap_bin, tk_bin = liet_ke_tap(n, S)
    print(f"1. Thuật toán Sinh kế tiếp xâu nhị phân:")
    print(f"   - Số cấu hình đã duyệt: {tk_bin['so_cau_hinh_da_duyet']} / {tk_bin['tong_so_cau_hinh_ly_thuyet']}")
    print(f"   - Số tập con tìm được : {tk_bin['so_tap_tim_duoc']}")
    print(f"   - Danh sách các tập   : {cac_tap_bin}")
    
    # Phương pháp 2: Quay lui có cắt nhánh
    cac_tap_ql, tk_ql = liet_ke_tap_quay_lui(n, S)
    print(f"\n2. Thuật toán Quay lui có cắt nhánh:")
    print(f"   - Số nút đã duyệt     : {tk_ql['so_nut_da_duyet']} (tiết kiệm {tk_bin['so_cau_hinh_da_duyet'] - tk_ql['so_nut_da_duyet']} nút)")
    print(f"   - Số tập con tìm được : {tk_ql['so_tap_tim_duoc']}")
    print(f"   - Danh sách các tập   : {cac_tap_ql}")
    print(f"{'='*60}\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Chương trình liệt kê tập con có tổng bằng S (DT032)")
    parser.add_argument("--n", type=int, help="Số phần tử n (1 <= n <= 18)")
    parser.add_argument("--S", type=int, help="Tổng cần đạt S")
    parser.add_argument("--interactive", action="store_true", help="Chế độ nhập từ bàn phím")
    args = parser.parse_args()

    if args.interactive:
        print("--- CHẾ ĐỘ NHẬP DỮ LIỆU TỪ BÀN PHÍM ---")
        try:
            n_in = int(input("Nhập n (1 <= n <= 18): ").strip())
            s_in = int(input("Nhập S (0 <= S <= n*(n+1)//2 + 1): ").strip())
            kiem_tra_hop_le(n_in, s_in)
            in_ket_qua(n_in, s_in)
        except Exception as e:
            print(f"Lỗi: {e}")
            sys.exit(1)
        return

    if args.n is not None and args.S is not None:
        try:
            kiem_tra_hop_le(args.n, args.S)
            in_ket_qua(args.n, args.S)
        except Exception as e:
            print(f"Lỗi: {e}")
            sys.exit(1)
        return

    # Mặc định: Chạy cả Ví dụ 1 và Ví dụ 2 trên phiếu giao đề tài
    print(">>> CHẠY VÍ DỤ 1 TRÊN PHIẾU GIAO (n=4, S=5):")
    in_ket_qua(4, 5)

    print(">>> CHẠY VÍ DỤ 2 TRÊN PHIẾU GIAO (n=3, S=3):")
    in_ket_qua(3, 3)


if __name__ == "__main__":
    main()
