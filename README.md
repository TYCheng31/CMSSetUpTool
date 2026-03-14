# ⚙️ CMS Auto Configurator

A powerful Python Selenium automation tool designed to help developers and system administrators batch update task parameters in the **Contest Management System (CMS)**. 

Instead of manually clicking through dozens of tasks to update time limits or memory limits, this script automatically navigates the CMS admin interface and applies your desired settings across all tasks in seconds.

## ✨ Features

- **Batch Processing**: Automatically fetches and updates all available tasks in the CMS backend.
- **Cross-Platform**: Works seamlessly on both Windows and Linux/Ubuntu.
- **One-Click Setup**: Comes with `setup.bat` and `setup.sh` to automatically create virtual environments and install dependencies.
- **Smart Linux Installer**: The Ubuntu setup script (`setup.sh`) automatically checks for and installs Google Chrome if it's missing.
- **Safe Execution**: Runs in an isolated Python virtual environment (`cms_env`), keeping your global system clean.

---

## 🚀 Getting Started

### 1. Prerequisites
- **Python 3.8** or higher installed on your system.
- (Windows only) Google Chrome browser installed.

### 2. Installation

Clone or download this repository to your local machine, then run the setup script corresponding to your operating system.

**For Windows Users:**
Simply double-click `setup.bat` or run the following in your Command Prompt:
```cmd
setup.bat