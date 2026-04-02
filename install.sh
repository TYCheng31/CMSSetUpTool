#!/bin/bash

echo "Starting CMS Auto Configurator environment setup..."

# 1. 更新系統並安裝基礎依賴 (包含 git, wget, python3-venv, python3-tk)
echo "Updating system and installing base dependencies..."
sudo apt-get update
sudo apt-get install -y git wget python3-venv python3-tk

# 2. 檢查並安裝 Google Chrome
echo "Checking for Google Chrome..."
if ! command -v google-chrome &> /dev/null; then
    echo "Google Chrome is not installed. Downloading and installing..."
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /tmp/google-chrome.deb
    sudo apt-get install -y /tmp/google-chrome.deb
    rm /tmp/google-chrome.deb
    echo "Google Chrome installation completed."
else
    echo "Google Chrome is already installed."
fi

# 3. 下載或更新專案程式碼
echo "Cloning or updating CMSSetUpTool repository..."
if [ -d "CMSSetUpTool" ]; then
    echo "Directory CMSSetUpTool already exists. Pulling latest changes..."
    cd CMSSetUpTool
    git pull
else
    git clone https://github.com/TYCheng31/CMSSetUpTool.git
    cd CMSSetUpTool
fi

# 4. 建立虛擬環境
echo "Creating virtual environment (tool_env)..."
python3 -m venv tool_env

# 5. 啟動虛擬環境並安裝 Python 套件
echo "Activating virtual environment and installing dependencies..."
source tool_env/bin/activate
pip install --upgrade pip
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "Warning: requirements.txt not found!"
fi

# 6. 啟動 GUI
echo "Starting the GUI..."
python3 gui.py