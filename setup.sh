#!/bin/bash

echo "Starting CMS Auto Configurator environment setup..."

# 1. Check and install Google Chrome
echo "Checking for Google Chrome..."
if ! command -v google-chrome &> /dev/null; then
    echo "Google Chrome is not installed. Downloading and installing..."
    sudo apt-get update
    sudo apt-get install -y wget
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /tmp/google-chrome.deb
    sudo apt-get install -y /tmp/google-chrome.deb
    rm /tmp/google-chrome.deb
    echo "Google Chrome installation completed."
else
    echo "Google Chrome is already installed."
fi

# 2. Check and install python3-venv
echo "Checking for python3-venv..."
if ! dpkg -l | grep -q python3-venv; then
    echo "Installing python3-venv..."
    sudo apt-get update
    sudo apt-get install -y python3-venv
fi

# 3. Create virtual environment
echo "Creating virtual environment (tool_env)..."
python3 -m venv tool_env

# 4. Activate environment and install dependencies
echo "Activating virtual environment and installing dependencies..."
source tool_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "========================================="
echo "Setup complete!"
echo "First, activate the environment:"
echo "  source tool_env/bin/activate"
echo ""
echo "Then, choose a script to run:"
echo "  python AddContestTask.py  (Only create contest & tasks)"
echo "  python AutoConfig.py      (Only update task parameters)"
echo "  python Auto.py            (Do everything automatically)"
echo "========================================="