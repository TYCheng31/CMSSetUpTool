@echo off
echo 開始設定 CMS Auto Configurator 環境...

REM 建立虛擬環境
python -m venv cms_env

REM 啟動並安裝套件
call cms_env\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo 設定完成！
echo 請執行 'cms_env\Scripts\activate.bat' 來啟動環境，然後執行 'python auto_config.py'
pause