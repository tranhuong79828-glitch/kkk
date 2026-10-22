"""
Module cài đặt thuật toán Liệt kê tập con có tổng bằng S
Mã đề tài: DT032 - INT13185 Nhóm 03
Sinh viên thực hiện: Trần Minh Khang - MSSV: N24DCDT036
Giảng viên hướng dẫn: ThS. Hồ Nhựt Minh
"""

from typing import List, Tuple, Dict, Any


def kiem_tra_hop_le(n: int, S: int) -> None:
    """
    Kiểm tra tính hợp lệ của dữ liệu đầu vào theo đặc tả đề tài DT032:
    - 1 <= n <= 18
    - 0 <= S <= n * (n + 1) // 2 + 1
    Ném ra ngoại lệ ValueError nếu dữ liệu không hợp lệ.
    """
    if not isinstance(n, int) or not isinstance(S, int):
        raise TypeError(f"Tham số n và S phải là số nguyên, nhận được: n={type(n)}, S={type(S)}")
    if n < 1 or n > 18:
        raise ValueError(f"Giá trị n={n} không nằm trong phạm vi hợp lệ [1, 18]")
    max_S = n * (n + 1) // 2 + 1
    if S < 0 or S > max_S:
        raise ValueError(f"Giá trị S={S} không nằm trong phạm vi hợp lệ [0, {max_S}] với n={n}")


def tong_tap(x: List[int]) -> int:
    """
    Tính tổng các phần tử của tập con ứng với cấu hình nhị phân x.
    Quy ước: bit thứ i (chỉ số 0-based là i-1) đại diện cho phần tử i.
    Nếu x[i-1] == 1 thì phần tử i được chọn vào tập.
    
    Ví dụ: x = [1, 0, 0, 1] với n=4 -> tổng = 1*1 + 0*2 + 0*3 + 1*4 = 5.
    """
    total = 0
    for idx, bit in enumerate(x, start=1):
        if bit == 1:
            total += idx
    return total


def tap_tu_bit(x: List[int]) -> List[int]:
    """
    Trích xuất danh sách các phần tử được chọn từ cấu hình bit x.
    Phần tử trong tập con tự động được sắp xếp tăng dần.
    
    Ví dụ: x = [1, 0, 0, 1] -> [1, 4].
    """
    return [idx for idx, bit in enumerate(x, start=1) if bit == 1]


def sinh_ke_tiep(x: List[int]) -> bool:
    """
    Thuật toán sinh xâu nhị phân kế tiếp theo thứ tự từ điển (Giáo trình Mục 3.2.2).
    - Duyệt từ cuối dãy (n-1) về đầu dãy (0).
    - Tìm vị trí i đầu tiên có x[i] == 0:
        + Đặt x[i] = 1
        + Đặt toàn bộ các bit phía sau từ i+1 đến n-1 thành 0
        + Trả về True (sinh thành công cấu hình mới)
    - Nếu toàn bộ là 1 (cấu hình 11...1): cấu hình cuối cùng, trả về False.
    """
    n = len(x)
    i = n - 1
    while i >= 0 and x[i] == 1:
        i -= 1
    if i < 0:
        return False  # Đã đạt cấu hình cuối cùng
    x[i] = 1
    for j in range(i + 1, n):
        x[j] = 0
    return True


def liet_ke_tap(n: int, S: int) -> Tuple[List[List[int]], Dict[str, Any]]:
    """
    Thuật toán chính theo phiếu giao đề tài:
    Sinh toàn bộ 2^n cấu hình nhị phân và lọc các tập con có tổng đúng bằng S.
    
    Đầu vào:
        n: số phần tử (1 <= n <= 18)
        S: tổng cần đạt
    Đầu ra:
        (cac_tap, thong_ke):
            cac_tap: danh sách các tập con có tổng bằng S
            thong_ke: thông tin số cấu hình đã duyệt, số phép tính, số nghiệm
    """
    kiem_tra_hop_le(n, S)
    
    cac_tap: List[List[int]] = []
    x = [0] * n  # Bắt đầu từ cấu hình đầu tiên: [0, 0, ..., 0] (tập rỗng)
    so_cau_hinh = 0
    
    while True:
        so_cau_hinh += 1
        val = tong_tap(x)
        if val == S:
            cac_tap.append(tap_tu_bit(x))
        if not sinh_ke_tiep(x):
            break

    # Sắp xếp các tập theo thứ tự từ điển chuẩn hóa theo yêu cầu đề tài
    cac_tap.sort()
            
    thong_ke = {
        "n": n,
        "S": S,
        "so_cau_hinh_da_duyet": so_cau_hinh,
        "tong_so_cau_hinh_ly_thuyet": 1 << n,
        "so_tap_tim_duoc": len(cac_tap),
        "phuong_phap": "Sinh kế tiếp xâu nhị phân"
    }
    return cac_tap, thong_ke


def liet_ke_tap_quay_lui(n: int, S: int) -> Tuple[List[List[int]], Dict[str, Any]]:
    """
    Thuật toán nâng cao (Yêu cầu thêm sau khi cơ bản đúng):
    Liệt kê tập con bằng phương pháp Quay lui (Backtracking) có cắt nhánh:
    - Nhánh 1: Thử chọn phần tử i nếu tổng hiện tại + i <= S.
    - Nhánh 2: Thử không chọn i nếu tổng hiện tại + tổng tối đa còn lại >= S.
    
    Vì mọi phần tử đều dương, cắt nhánh giúp giảm đáng kể không gian tìm kiếm.
    """
    kiem_tra_hop_le(n, S)
    
    cac_tap: List[List[int]] = []
    current_subset: List[int] = []
    so_nut_duyet = [0]
    
    # Tính trước tổng hậu tố để hỗ trợ cắt nhánh bên dưới
    # suffix_sum[i] = tổng các số từ i đến n
    suffix_sum = [0] * (n + 2)
    for i in range(n, 0, -1):
        suffix_sum[i] = suffix_sum[i + 1] + i

    def backtrack(i: int, current_sum: int) -> None:
        so_nut_duyet[0] += 1
        if current_sum == S:
            cac_tap.append(list(current_subset))
            # Vì các phần tử tiếp theo đều dương (>0), nếu đã bằng S thì không thể chọn thêm số nào nữa
            return
        if i > n:
            return
            
        # Cắt nhánh: nếu tổng hiện tại + tổng tất cả phần tử còn lại < S thì không thể đạt S
        if current_sum + suffix_sum[i] < S:
            return

        # Nhánh 1: Chọn phần tử i (nếu không vượt quá S)
        if current_sum + i <= S:
            current_subset.append(i)
            backtrack(i + 1, current_sum + i)
            current_subset.pop()  # Quay lui

        # Nhánh 2: Không chọn phần tử i
        backtrack(i + 1, current_sum)

    backtrack(1, 0)
    
    # Sắp xếp các tập theo thứ tự từ điển
    cac_tap.sort()
    
    thong_ke = {
        "n": n,
        "S": S,
        "so_nut_da_duyet": so_nut_duyet[0],
        "tong_so_cau_hinh_ly_thuyet": 1 << n,
        "so_tap_tim_duoc": len(cac_tap),
        "phuong_phap": "Quay lui có cắt nhánh"
    }
    return cac_tap, thong_ke
