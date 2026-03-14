# ⚙️ CMS Auto Configurator

A powerful Python Selenium automation tool designed to help developers and system administrators batch update task parameters in the **Contest Management System (CMS)**. 

Instead of manually clicking through dozens of tasks to update time limits or memory limits, this script automatically navigates the CMS admin interface and applies your desired settings across all tasks in seconds.

## ✨ Features

- **Batch Processing**: Automatically fetches and updates all available tasks in the CMS backend.
- **Cross-Platform**: Works seamlessly on both Windows and Linux/Ubuntu.
- **One-Click Setup**: Includes `setup.bat` and `setup.sh` to automatically create virtual environments and install dependencies.
- **Smart Linux Installer**: The Ubuntu setup script (`setup.sh`) automatically installs Google Chrome and `python3-venv` if they are missing.
- **Safe Execution**: Runs in an isolated Python virtual environment (`cms_env`), keeping your global system clean.

---

## 🚀 Getting Started

### 1. Prerequisites
- **Python 3.8** or higher installed.
- (Windows only) Google Chrome browser installed.

### 2. Installation

Clone or download this repository, then run the setup script for your OS:

**For Windows Users:**
Double-click `setup.bat` or run:
```cmd
setup.bat
```

**For Ubuntu / Linux Users:**
Run the following commands (it may ask for `sudo` password to install Chrome):
```bash
chmod +x setup.sh
./setup.sh
```

---

## 💻 Usage

### Step 1: Configuration
Open `auto_config.py` and update the **Configuration Section** at the top:

```python
LOGIN_URL = "[http://192.168.1.5:8889](http://192.168.1.5:8889)"   # Your CMS Admin IP
ADMIN_USERNAME = "admin"                # Your CMS username
ADMIN_PASSWORD = "admin"                # Your CMS password
MIN_SUBMISSION_INTERVAL = "30"          # Interval (seconds)
TIME_LIMIT = "5.0"                      # Time limit (seconds)
MEMORY_LIMIT = "512"                    # Memory limit (MB)
SCORE_PER_TASK = "4"                    # Score parameters
```

### Step 2: Execution
Activate the environment and run the script:

**On Windows:**
```cmd
cms_env\Scripts\activate.bat
python auto_config.py
```

**On Ubuntu / Linux:**
```bash
source cms_env/bin/activate
python auto_config.py
```

---

## 📁 Project Structure

```text
├── auto_config.py      # Main Selenium script
├── requirements.txt    # Python dependencies
├── setup.bat           # Windows setup script
├── setup.sh            # Ubuntu setup script
├── .gitignore          # Git ignore rules
└── README.md           # Documentation
```

## 📝 Notes
- **Headless Mode**: To run without a browser window, uncomment `options.add_argument('--headless')` in `auto_config.py`.
- **UI Interception**: The script uses JavaScript injection for clicks to prevent sidebar occlusion errors.