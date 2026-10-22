"""
Kịch bản chạy tự động toàn bộ quy trình kiểm thử, demo, benchmark và ghi log (DT032)
Sinh viên: Trần Minh Khang - MSSV: N24DCDT036
"""

import sys
import os
import subprocess

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(base_dir, "docs", "logs")
os.makedirs(log_dir, exist_ok=True)


def run_command_log(cmd: list, log_name: str) -> None:
    log_path = os.path.join(log_dir, log_name)
    print(f"-> Đang chạy: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=base_dir, capture_output=True, text=True, encoding="utf-8", errors="replace")
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(result.stdout)
        if result.stderr:
            f.write("\n--- STDERR ---\n")
            f.write(result.stderr)
    print(f"   Đã lưu log: {log_name} (Exit code: {result.returncode})")


def main() -> None:
    print("=" * 70)
    print("BẮT ĐẦU CHẠY TOÀN BỘ QUY TRÌNH TỰ ĐỘNG - ĐỀ TÀI DT032")
    print("Sinh viên: Trần Minh Khang - MSSV: N24DCDT036")
    print("=" * 70)

    # 1. Chạy bộ kiểm thử 14 ca
    run_command_log([sys.executable, "-m", "unittest", "test/test_subsets.py", "-v"], "tests.log")

    # 2. Chạy Demo Ví dụ 1 & Ví dụ 2
    run_command_log([sys.executable, "demo.py", "--n", "4", "--S", "5"], "demo_01.log")
    run_command_log([sys.executable, "demo.py", "--n", "3", "--S", "3"], "demo_02.log")

    # 3. Chạy Khảo sát hiệu năng 3 quy mô Q1, Q2, Q3
    run_command_log([sys.executable, "scripts/run_benchmarks.py"], "benchmarks.log")

    # 4. Chạy Bảng lần vết chi tiết n=5, S=5
    run_command_log([sys.executable, "scripts/generate_trace.py"], "trace.log")

    # 5. Sinh 11 ảnh minh chứng
    run_command_log([sys.executable, "scripts/capture_views.py"], "capture_views.log")

    print("=" * 70)
    print("HOÀN THÀNH TOÀN BỘ QUY TRÌNH TỰ ĐỘNG THÀNH CÔNG RỰC RỠ!")
    print(f"Các tệp log chi tiết được lưu trữ tại: {log_dir}")
    print("=" * 70)


if __name__ == "__main__":
    main()
