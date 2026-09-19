@echo off
title AI Detection App - Local Server
color 0A
echo ================================================
echo   AI-Generated Image Detection App
echo   CNN + Grad-CAM + LIME Explainability
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found!
    echo.
    echo Please install Python 3.7.9 from:
    echo https://www.python.org/downloads/release/python-379/
    echo.
    echo Make sure to check Add Python to PATH during install.
    pause
    exit /b 1
)

echo [OK] Python found.
echo.

REM Create virtual environment if it doesn't exist
if not exist venv" (
 echo [SETUP] Creating virtual environment...
 python -m venv venv
 echo [OK] Virtual environment created.
 echo.
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies if not installed
pip show django >nul 2>&1
if errorlevel 1 (
 echo [SETUP] Installing dependencies (first time only - may take 10-15 mins)...
 pip install -r requirements.txt
 echo [OK] Dependencies installed.
 echo.
)

REM Run migrations to create/update database tables
echo [SETUP] Running database migrations...
python manage.py makemigrations --noinput >nul 2>&1
python manage.py migrate --run-syncdb >nul 2>&1
echo [OK] Database ready.
echo.

REM Start Django server
echo ================================================
echo Server starting at: http://127.0.0.1:8000
echo.
echo Open this URL in your browser:
echo http://127.0.0.1:8000/DetectionApp/index.html
echo.
echo Login credentials: admin / admin
echo Sign Up page: /DetectionApp/UserSignup.html
echo.
echo Press CTRL+C to stop the server
echo ================================================
echo.
python manage.py runserver

pause
