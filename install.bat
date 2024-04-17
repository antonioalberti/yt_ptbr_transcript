@echo off

REM Set the name of the virtual environment
set VENV_NAME=myenv

REM Create the virtual environment
python -m venv %VENV_NAME%

REM Activate the virtual environment
call %VENV_NAME%\Scripts\activate.bat

REM Install packages from the requirements.txt file
pip install -r requirements.txt

REM Completion message
echo Virtual environment created and packages installed successfully!
echo The virtual environment remains activated.
