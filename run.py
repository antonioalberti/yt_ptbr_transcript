@echo off
set "PYTHON_EXECUTABLE=python"

%PYTHON_EXECUTABLE% -V >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not found in the system PATH.
    echo Please install Python and make sure it's added to the system PATH.
    pause
    exit /b 1
)

echo Running the YouTube Transcription script...
%PYTHON_EXECUTABLE% main.py
pause