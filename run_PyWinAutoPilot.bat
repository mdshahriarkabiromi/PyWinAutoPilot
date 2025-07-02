@echo off
rem Change directory to where the script is located
cd /d "%~dp0"

echo Starting PyWinAutoPilot...
python main.py

echo.
echo PyWinAutoPilot finished. Press any key to exit.
pause > nul
exit /b 0