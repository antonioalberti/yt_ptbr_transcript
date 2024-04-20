@echo off

REM Set the name of the virtual environment
set VENV_NAME=myenv

REM Create the virtual environment
python -m venv %VENV_NAME%

REM Activate the virtual environment
call %VENV_NAME%\Scripts\activate.bat

REM Install packages from the requirements.txt file
pip install -r requirements.txt

REM Update pip
python.exe -m pip install --upgrade pip

REM Install additional packages
pip install pydub

REM Update pydub
pip install --upgrade pydub

REM Completion message
echo Virtual environment created and packages installed successfully!
echo Please make sure FFmpeg is installed and added to PATH manually.
echo The virtual environment remains activated.


