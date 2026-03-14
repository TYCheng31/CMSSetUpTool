#!/bin/bash
echo "開始設定 CMS Auto Configurator 環境..."

# 檢查是否安裝了 python3-venv (Ubuntu 常需要手動裝這個)
if ! dpkg -l | grep -q python3-venv; then
    echo "正在安裝 python3-venv..."
    sudo apt update
    sudo apt install -y python3-venv
fi

# 建立名為 cms_env 的虛擬環境
python3 -m venv cms_env

# 啟動虛擬環境並安裝套件
source cms_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "設定完成！請輸入 'source cms_env/bin/activate' 來啟動環境，然後執行 'python auto_config.py'"