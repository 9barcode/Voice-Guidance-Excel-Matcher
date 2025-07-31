@echo off
cd /d "%~dp0"

:menu
cls
echo ======menu ======
echo Follow the steps in order: 1, 2, 3.
echo 1. Convert dlt_to_txt
echo 2. Create result.csv 
echo 3. Sentence matching in the test Excel file
echo 0. exit
echo.
set /p choice=Select number: 

if "%choice%"=="2" (
    py sentence_filter_text.py
    pause
    goto menu
)

if "%choice%"=="3" (
    py matching_machine.py
    pause
    goto menu
)

if "%choice%"=="1" (
    py convert_to_txt.py
    pause
    goto menu
)

if "%choice%"=="0" (
    echo exit...
    exit
)

echo error...
pause
goto menu
