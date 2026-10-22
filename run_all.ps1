# Script PowerShell chạy tự động đề tài DT032
# Sinh viên: Trần Minh Khang - MSSV: N24DCDT036
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "KICH BAN CHAY TU DONG DE TAI DT032 - TRAN MINH KHANG" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan

python run_all.py

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n[THANH CONG] Toan bo kiem thu va sinh du lieu da hoan tat!" -ForegroundColor Green
} else {
    Write-Host "`n[THAT BAI] Co loi xay ra trong qua trinh chay!" -ForegroundColor Red
}
