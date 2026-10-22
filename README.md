# ĐỒ ÁN HỌC PHẦN CẤU TRÚC DỮ LIỆU VÀ GIẢI THUẬT (INT13185 - NHÓM 03)

## ĐỀ TÀI DT032: LIỆT KÊ TẬP CON CÓ TỔNG BẰNG S

* **Sinh viên thực hiện:** Trần Minh Khang
* **Mã số sinh viên (MSSV):** N24DCDT036
* **Lớp:** D24CQDT01-N
* **Giảng viên hướng dẫn:** ThS. Hồ Nhựt Minh
* **Khoa:** Kỹ thuật Điện tử 2 / Viễn thông - Học viện Công nghệ Bưu chính Viễn thông (Cơ sở TP.HCM)
* **Ngôn ngữ & Phiên bản:** Python 3.14.0 (Tương thích Python 3.9+)

---

## 1. GIỚI THIỆU BÀI TOÁN

Cho tập số nguyên $\{1, 2, \dots, n\}$ với $1 \le n \le 18$ và một số nguyên $S$ với $0 \le S \le \frac{n(n+1)}{2} + 1$. 
Mục tiêu là tìm tất cả các tập con của $\{1, 2, \dots, n\}$ sao cho tổng các phần tử trong tập con đúng bằng $S$.

Mỗi phần tử chỉ được lấy tối đa một lần. Kết quả in ra các tập con có phần tử tăng dần, sắp theo thứ tự từ điển, kèm số lượng tập con tìm được.

Chương trình cài đặt hai phương pháp:
1. **Thuật toán chính:** Sinh kế tiếp toàn bộ $2^n$ xâu nhị phân (theo Mục 3.2.2 Giáo trình INT1306) và lọc nghiệm.
2. **Thuật toán mở rộng (Cộng điểm):** Thuật toán Quay lui (Backtracking) có cắt nhánh khi tổng vượt quá $S$ hoặc phần còn lại không đủ bù đắp.

---

## 2. CẤU TRÚC THƯ MỤC DỰ ÁN

```text
N24DCDT036_DT032_TranMinhKhang/
├── src/
│   ├── __init__.py
│   └── subset_sum.py             # Cài đặt thuật toán sinh nhị phân và quay lui cắt nhánh
├── test/
│   ├── __init__.py
│   └── test_subsets.py           # Bộ kiểm thử độc lập 14 ca kiểm thử chi tiết (assert)
├── scripts/
│   ├── run_benchmarks.py         # Khảo sát hiệu năng 3 quy mô Q1, Q2, Q3
│   ├── generate_trace.py         # Bảng lần vết chi tiết n=5, S=5 (32 cấu hình)
│   └── capture_views.py          # Sinh 11 ảnh chụp console A01-A11 và 2 sơ đồ thuật toán
├── docs/
│   ├── anh_ket_qua/              # 11 ảnh minh chứng thực nghiệm view_01.png -> view_11.png
│   └── logs/                     # Toàn bộ tệp log thực thi (tests.log, demo.log, trace.log...)
├── demo.py                       # Chương trình tương tác và chạy mẫu
├── run_all.py                    # Chạy toàn bộ kiểm thử, demo, benchmark và tạo log
├── run_all.ps1                   # Script PowerShell chạy 1 click
└── README.md                     # Tài liệu hướng dẫn sử dụng
```

---

## 3. HƯỚNG DẪN CÀI ĐẶT VÀ CHẠY

Dự án chỉ sử dụng thư viện tiêu chuẩn của Python (`sys`, `os`, `time`, `unittest`, `argparse`). Để sinh ảnh đồ họa cần thêm `Pillow` và `matplotlib`.

### 3.1. Chạy chương trình minh họa (Demo)
```bash
# Chạy mặc định Ví dụ 1 (n=4, S=5) và Ví dụ 2 (n=3, S=3) trên phiếu:
python demo.py

# Chạy một trường hợp bất kỳ:
python demo.py --n 5 --S 8

# Chế độ nhập tương tác từ bàn phím:
python demo.py --interactive
```

### 3.2. Chạy bộ kiểm thử tự động (14 ca độc lập)
```bash
python -m unittest test/test_subsets.py -v
```

### 3.3. Khảo sát hiệu năng 3 quy mô (Q1, Q2, Q3)
```bash
python scripts/run_benchmarks.py
```

### 3.4. Xuất bảng lần vết n=5, S=5 (Bảng 3.3 trong báo cáo)
```bash
python scripts/generate_trace.py
```

### 3.5. Chạy toàn bộ quy trình tự động và xuất log
```bash
python run_all.py
# hoặc trên PowerShell:
.\run_all.ps1
```

---

## 4. BỘ MINH CHỨNG KẾT QUẢ THỬ NGHIỆM

Toàn bộ 11 ảnh minh chứng theo Rubric C4, C5 được lưu tại thư mục `docs/anh_ket_qua/`:
* `view_01.png` (Hình 4.1): A01 - Ví dụ 1 phiếu ($n=4, S=5$).
* `view_02.png` (Hình 4.2): A02 - Ví dụ 2 phiếu ($n=3, S=3$).
* `view_03.png` (Hình 4.3): A03 - Ca tự thiết kế 1 ($n=4, S=6$).
* `view_04.png` (Hình 4.4): A04 - Ca tự thiết kế 2 ($n=5, S=8$).
* `view_05.png` (Hình 4.5): A05 - Ca biên 1 trên phiếu ($n=1, S=0$ - Tập rỗng).
* `view_06.png` (Hình 4.6): A06 - Ca biên 2 trên phiếu ($n=1, S=1$).
* `view_07.png` (Hình 4.7): A07 - Ca biên 3 trên phiếu ($n=3, S=7$ - Vô nghiệm).
* `view_08.png` (Hình 4.8): A08 - Kiểm tra input không hợp lệ (Bắt lỗi `ValueError`).
* `view_09.png` (Hình 4.9): A09 - Tổng kết kiểm thử 14/14 tests pass.
* `view_10.png` (Hình 4.10): A10 - Clone sạch vào thư mục mới và chạy lại độc lập.
* `view_11.png` (Hình 4.11): A11 - Lịch sử Git commit C và commit S.

---

## 5. THÔNG TIN PHIÊN BẢN VÀ COMMIT GIT
* **Commit C (Nguồn thuật toán & Test):** `c8f1e29`
* **Commit S (Phiên bản nộp kèm ảnh & báo cáo):** `e49d21b`
* **GitHub Repository:** `https://github.com/TranMinhKhang-PTIT/DT032_SubsetSum.git`
