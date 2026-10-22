"""
Bộ kiểm thử độc lập cho đề tài DT032: Liệt kê tập con có tổng bằng S
Sinh viên: Trần Minh Khang - MSSV: N24DCDT036
Bao gồm 14 ca kiểm thử chi tiết, đối chiếu kết quả kỳ vọng và kiểm tra bất biến.
"""

import sys
import os
import unittest

# Đảm bảo đường dẫn import src
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from src.subset_sum import (
    kiem_tra_hop_le,
    tong_tap,
    tap_tu_bit,
    sinh_ke_tiep,
    liet_ke_tap,
    liet_ke_tap_quay_lui
)


class TestSubsetSum(unittest.TestCase):
    
    def test_tc01_vi_du_1(self):
        """TC01 (A01): Ví dụ 1 phiếu giao - n=4, S=5 -> [[1, 4], [2, 3]]"""
        cac_tap, thong_ke = liet_ke_tap(4, 5)
        expected = [[1, 4], [2, 3]]
        self.assertEqual(cac_tap, expected)
        self.assertEqual(thong_ke["so_tap_tim_duoc"], 2)
        self.assertEqual(thong_ke["so_cau_hinh_da_duyet"], 16)
        
        # Kiểm tra tính đồng nhất với bản quay lui
        tap_ql, _ = liet_ke_tap_quay_lui(4, 5)
        self.assertEqual(tap_ql, expected)

    def test_tc02_vi_du_2(self):
        """TC02 (A02): Ví dụ 2 phiếu giao - n=3, S=3 -> [[1, 2], [3]]"""
        cac_tap, thong_ke = liet_ke_tap(3, 3)
        expected = [[1, 2], [3]]
        self.assertEqual(cac_tap, expected)
        self.assertEqual(thong_ke["so_tap_tim_duoc"], 2)
        self.assertEqual(thong_ke["so_cau_hinh_da_duyet"], 8)
        
        tap_ql, _ = liet_ke_tap_quay_lui(3, 3)
        self.assertEqual(tap_ql, expected)

    def test_tc03_tu_thiet_ke_1(self):
        """TC03 (A03): Ca tự thiết kế 1 - n=4, S=6 -> [[1, 2, 3], [2, 4]]"""
        cac_tap, thong_ke = liet_ke_tap(4, 6)
        expected = [[1, 2, 3], [2, 4]]
        self.assertEqual(cac_tap, expected)
        self.assertEqual(thong_ke["so_tap_tim_duoc"], 2)
        
        tap_ql, _ = liet_ke_tap_quay_lui(4, 6)
        self.assertEqual(tap_ql, expected)

    def test_tc04_tu_thiet_ke_2(self):
        """TC04 (A04): Ca tự thiết kế 2 - n=5, S=8 -> [[1, 2, 5], [1, 3, 4], [3, 5]]"""
        cac_tap, thong_ke = liet_ke_tap(5, 8)
        expected = [[1, 2, 5], [1, 3, 4], [3, 5]]
        self.assertEqual(cac_tap, expected)
        self.assertEqual(thong_ke["so_tap_tim_duoc"], 3)
        
        tap_ql, _ = liet_ke_tap_quay_lui(5, 8)
        self.assertEqual(tap_ql, expected)

    def test_tc05_bien_tap_rong(self):
        """TC05 (A05): Ca biên 1 trên phiếu - n=1, S=0 -> [[]], số tập = 1"""
        cac_tap, thong_ke = liet_ke_tap(1, 0)
        expected = [[]]
        self.assertEqual(cac_tap, expected)
        self.assertEqual(thong_ke["so_tap_tim_duoc"], 1)
        self.assertEqual(thong_ke["so_cau_hinh_da_duyet"], 2)
        
        tap_ql, _ = liet_ke_tap_quay_lui(1, 0)
        self.assertEqual(tap_ql, expected)

    def test_tc06_bien_mot_phan_tu(self):
        """TC06 (A06): Ca biên 2 trên phiếu - n=1, S=1 -> [[1]], số tập = 1"""
        cac_tap, thong_ke = liet_ke_tap(1, 1)
        expected = [[1]]
        self.assertEqual(cac_tap, expected)
        self.assertEqual(thong_ke["so_tap_tim_duoc"], 1)
        
        tap_ql, _ = liet_ke_tap_quay_lui(1, 1)
        self.assertEqual(tap_ql, expected)

    def test_tc07_bien_tong_vuot_muc(self):
        """TC07 (A07): Ca biên 3 trên phiếu - n=3, S=7 -> [], không có nghiệm"""
        cac_tap, thong_ke = liet_ke_tap(3, 7)
        expected = []
        self.assertEqual(cac_tap, expected)
        self.assertEqual(thong_ke["so_tap_tim_duoc"], 0)
        
        tap_ql, _ = liet_ke_tap_quay_lui(3, 7)
        self.assertEqual(tap_ql, expected)

    def test_tc08_phieu_ca_4(self):
        """TC08: Ca 4 trên phiếu - n=4, S=10 -> [[1, 2, 3, 4]] (tập toàn phần)"""
        cac_tap, thong_ke = liet_ke_tap(4, 10)
        expected = [[1, 2, 3, 4]]
        self.assertEqual(cac_tap, expected)
        self.assertEqual(thong_ke["so_tap_tim_duoc"], 1)
        
        tap_ql, _ = liet_ke_tap_quay_lui(4, 10)
        self.assertEqual(tap_ql, expected)

    def test_tc09_phieu_ca_5(self):
        """TC09: Ca 5 trên phiếu (ca lần vết) - n=5, S=5 -> [[1, 4], [2, 3], [5]]"""
        cac_tap, thong_ke = liet_ke_tap(5, 5)
        expected = [[1, 4], [2, 3], [5]]
        self.assertEqual(cac_tap, expected)
        self.assertEqual(thong_ke["so_tap_tim_duoc"], 3)
        self.assertEqual(thong_ke["so_cau_hinh_da_duyet"], 32)
        
        tap_ql, _ = liet_ke_tap_quay_lui(5, 5)
        self.assertEqual(tap_ql, expected)

    def test_tc10_bien_rong_n_lon(self):
        """TC10: Ca biên rỗng với n lớn hơn - n=6, S=0 -> [[]]"""
        cac_tap, thong_ke = liet_ke_tap(6, 0)
        expected = [[]]
        self.assertEqual(cac_tap, expected)
        self.assertEqual(thong_ke["so_tap_tim_duoc"], 1)
        
        tap_ql, _ = liet_ke_tap_quay_lui(6, 0)
        self.assertEqual(tap_ql, expected)

    def test_tc11_vuot_tong_toi_da(self):
        """TC11: Ca vượt quá tổng tối đa n=5, S=16 (tổng max 15) -> []"""
        cac_tap, thong_ke = liet_ke_tap(5, 16)
        expected = []
        self.assertEqual(cac_tap, expected)
        self.assertEqual(thong_ke["so_tap_tim_duoc"], 0)
        
        tap_ql, _ = liet_ke_tap_quay_lui(5, 16)
        self.assertEqual(tap_ql, expected)

    def test_tc12_quy_mo_vua(self):
        """TC12: Ca kiểm tra quy mô vừa n=6, S=9 -> 5 tập con"""
        cac_tap, thong_ke = liet_ke_tap(6, 9)
        expected = [[1, 2, 6], [1, 3, 5], [2, 3, 4], [3, 6], [4, 5]]
        self.assertEqual(cac_tap, expected)
        self.assertEqual(thong_ke["so_tap_tim_duoc"], 5)
        
        tap_ql, _ = liet_ke_tap_quay_lui(6, 9)
        self.assertEqual(tap_ql, expected)

    def test_tc13_dong_nhat_hai_phuong_phap(self):
        """TC13: Kiểm tra tính đồng nhất giữa Sinh nhị phân và Quay lui trên n=8, S=12"""
        tap_bin, _ = liet_ke_tap(8, 12)
        tap_ql, _ = liet_ke_tap_quay_lui(8, 12)
        self.assertEqual(tap_bin, tap_ql)
        self.assertGreater(len(tap_bin), 0)
        for subset in tap_bin:
            self.assertEqual(sum(subset), 12)

    def test_tc14_input_khong_hop_le(self):
        """TC14 (A08): Kiểm tra cơ chế bảo vệ đầu vào sai miền giá trị"""
        with self.assertRaises(ValueError):
            liet_ke_tap(0, 5)   # n < 1
        with self.assertRaises(ValueError):
            liet_ke_tap(19, 5)  # n > 18
        with self.assertRaises(ValueError):
            liet_ke_tap(4, -1)  # S < 0
        with self.assertRaises(ValueError):
            liet_ke_tap(4, 12)  # S > n*(n+1)//2 + 1 (10 + 1 = 11)


if __name__ == "__main__":
    unittest.main()
