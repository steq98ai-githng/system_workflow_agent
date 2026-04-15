@echo off
:: G-Assist 中文外掛 V2 安裝腳本
:: 以管理員身分執行此檔案

net session >nul 2>&1
if %errorLevel% neq 0 (
    powershell -Command "Start-Process '%~dpnx0' -Verb RunAs"
    exit /b
)

echo =====================================================
echo   G-Assist 中文外掛 V2 安裝中...
echo =====================================================

set "SRC=%~dp0"
set "DST=C:\ProgramData\NVIDIA Corporation\nvtopps\rise\plugins\ai_chinese_mode"

:: 確保目標目錄存在
if not exist "%DST%" mkdir "%DST%"

:: 複製核心檔案
echo 正在複製 plugin.py ...
copy /Y "%SRC%plugin.py" "%DST%\plugin.py"

echo 正在複製 manifest.json ...
copy /Y "%SRC%manifest.json" "%DST%\manifest.json"

echo 正在複製 SDK (libs) ...
if not exist "%DST%\libs" mkdir "%DST%\libs"
xcopy /E /I /Y "%SRC%libs" "%DST%\libs"

:: 清除舊版 exe
if exist "%DST%\ai-chinese-plugin.exe" (
    echo 正在移除舊版 exe ...
    del /F /Q "%DST%\ai-chinese-plugin.exe"
)

:: 清除錯誤的子目錄
if exist "%DST%\ai_chinese_mode" (
    echo 正在清除錯誤的子目錄 ...
    rmdir /S /Q "%DST%\ai_chinese_mode"
)

echo =====================================================
echo   安裝完成！請重啟 NVIDIA App / G-Assist。
echo =====================================================
pause
