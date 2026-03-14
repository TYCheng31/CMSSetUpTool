# CMS Auto Configurator (CMS 自動化設定腳本)

這是一個使用 Python Selenium 撰寫的自動化工具，旨在幫助開發者或系統管理員，一鍵批次修改 Contest Management System (CMS) 後台的任務參數（如 Time Limit, Memory Limit 等），省去手動逐一設定的麻煩。

## 🚀 快速開始

### 1. 前置需求
* Python 3.8 或以上版本
* Google Chrome 瀏覽器

### 2. 安裝步驟

我們提供了快速安裝腳本，會自動為你建立虛擬環境並安裝所需套件：

**Windows 使用者：**
雙擊執行 `setup.bat`，或者在終端機執行以下指令：
```cmd
python -m venv cms_env
cms_env\Scripts\activate
pip install -r requirements.txt
```

**Ubuntu / macOS 使用者：**
在終端機執行安裝腳本：
```bash
bash setup.sh
```

### 3. 設定與執行

1. 用文字編輯器打開 `auto_config.py`。
2. 找到最上方的 **「系統與任務設定區」**，將登入網址、帳號密碼以及各項任務數值（如 `TIME_LIMIT`、`MEMORY_LIMIT`）修改為你需要的設定。
3. 啟動虛擬環境後，執行腳本：
```bash
python auto_config.py
```

### 📝 注意事項
* 執行期間請確保終端機網路可正常連線至目標 CMS 伺服器。
* 本腳本預設會開啟 Chrome 瀏覽器實體視窗以便觀察進度。若需在背景執行，請將程式碼中的 `options.add_argument('--headless')` 解除註解。