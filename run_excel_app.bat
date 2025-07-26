@echo off
echo ================================================================
echo          DAILY COUNTING - EXCEL INTEGRATION
echo ================================================================
echo.
echo 🔗 This app connects directly to your ISSUES.xlsx file
echo 📝 Select material, choose transaction type, enter quantity
echo ✅ Quantities are added to the correct Excel columns
echo.
echo ================================================================
echo.

REM Check if ISSUES.xlsx exists
if not exist "ISSUES.xlsx" (
    echo ❌ ERROR: ISSUES.xlsx file not found!
    echo.
    echo Please make sure ISSUES.xlsx is in this folder:
    echo %cd%
    echo.
    pause
    exit /b 1
)

echo ✅ ISSUES.xlsx found
echo 🚀 Starting Excel Integration Server...
echo.

REM Run the Python Flask app
python excel_app.py

echo.
echo Server stopped.
pause
