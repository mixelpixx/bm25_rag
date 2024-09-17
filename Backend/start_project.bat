@echo off
REM Navigate to the Backend directory
cd /d %~dp0

REM Activate the virtual environment
call env\Scripts\activate

REM Set the FLASK_APP environment variable
set FLASK_APP=main.py

REM Run the Flask server
start cmd /k "flask run"

REM Wait for the server to start
timeout /t 5 /nobreak >nul

REM Open the default web browser to the local server
start http://127.0.0.1:5000

REM Pause to keep the command window open
pause
