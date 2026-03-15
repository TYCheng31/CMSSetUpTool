# ⚙️ CMS Auto Configurator

A powerful Python Selenium automation tool suite designed to help developers and system administrators batch manage the **Contest Management System (CMS)**. 

Whether you need to create a new contest from scratch, batch create tasks, or quickly update time/memory limits across all existing tasks, this tool suite has you covered.

## ✨ Features
- **Modular Design**: Choose between creating tasks, updating parameters, or doing both simultaneously.
- **Cross-Platform**: Works seamlessly on both Windows and Linux/Ubuntu.
- **Smart Linux Installer**: Automatically installs Google Chrome and `python3-venv` if missing.
- **Master Reset Script**: Includes a master bash script to wipe the database, initialize it, and run the full Python configuration in one go.
- **Safe Execution**: Runs in an isolated Python virtual environment (`tool_env`), keeping your global system clean.

---

## 📁 Project Structure

```text
├── AddContestTask.py       # Module: Creates contest and tasks only
├── AutoConfig.py           # Module: Updates parameters for existing tasks only
├── Auto.py                 # Module: Integrated (Creates everything, then updates parameters)
├── reset_and_run.sh        # Master Bash Script: Resets DB, creates admin, runs script, and adds users
├── requirements.txt        # Python dependencies
├── setup.bat               # Windows setup script
├── setup.sh                # Ubuntu setup script
└── .gitignore              # Git ignore rules
```

---

## 🚀 Getting Started

### 1. Installation
Clone this repository and run the setup script for your OS:

**For Windows Users:**
Double-click `setup.bat` or run:
```cmd
setup.bat
```

**For Ubuntu / Linux Users:**
```bash
chmod +x setup.sh
./setup.sh
```

### 2. Configuration
Open the Python script you wish to use (`AddContestTask.py`, `AutoConfig.py`, or `Auto.py`) and update the **Configuration Section** at the top:
```python
LOGIN_URL = "http://localhost:8889"
ADMIN_USERNAME = "admin"
CONTEST_NAME = "NCUE"
TASK_NAMES = ["Q1", "Q2", "Q3", "Q4", "Q5"]
TIME_LIMIT = "5.0"
MEMORY_LIMIT = "512"
```

---

## 💻 Usage (Running the Scripts)

First, activate the virtual environment:
- **Windows:** `tool_env\Scripts\activate.bat`
- **Linux:** `source tool_env/bin/activate`

Then, run the script that fits your current needs:

**Option A: Just create a contest and tasks**
```bash
python AddContestTask.py
```

**Option B: Just update parameters for existing tasks**
```bash
python AutoConfig.py
```

**Option C: The Ultimate Integration (Create & Update)**
```bash
python Auto.py
```

---

## 🧹 Master Reset & Run (Linux Only)
If you are deploying CMS from scratch or need to completely wipe your environment, use the master script. This will drop the database, create an admin, run `Auto.py`, and import users from a CSV-like block.
```bash
chmod +x reset_and_run.sh
./reset_and_run.sh
```