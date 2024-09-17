@echo off
REM Navigate to the Backend directory
cd /d %~dp0

REM Activate the virtual environment
call env\Scripts\activate

REM Set the FLASK_APP environment variable
set FLASK_APP=main.py

REM Run the Flask server
flask run

REM Pause to keep the command window open
pause
