@echo off
echo Starting CMS Auto Configurator environment setup...

REM 1. Create virtual environment
echo Creating virtual environment (tool_env)...
python -m venv tool_env

REM 2. Activate environment and install packages
echo Activating virtual environment and installing dependencies...
call tool_env\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo =========================================
echo Setup complete!
echo To start the application, run the following commands:
echo 1. tool_env\Scripts\activate.bat
echo 2. python auto_config.py
echo =========================================
pause