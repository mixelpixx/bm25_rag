@echo off
REM Navigate to the Backend directory
cd /d %~dp0

REM Check if virtual environment exists, create if not
if not exist env (
    echo Creating virtual environment...
    python -m venv env
)

REM Activate the virtual environment
call env\Scripts\activate

REM Install or upgrade required packages
echo Installing/upgrading required packages...
pip install -r requirements.txt

REM Set the FLASK_APP environment variable
set FLASK_APP=main.py

REM Set the OPENAI_API_KEY environment variable
set /p OPENAI_API_KEY=Enter your OpenAI API key: 

REM Run the Flask server
echo Starting Flask server...
start cmd /k "flask run"

REM Wait for the server to start
echo Waiting for server to start...
timeout /t 5 /nobreak >nul

REM Open the default web browser to the frontend
echo Opening frontend in default browser...
start ..\Frontend\index.html

echo Setup complete. Press any key to exit.
pause
