# CMS 自動化設定工具

傳統的 CMS (Contest Management System，競賽管理系統) 需要手動設定每一道題目。此工具利用基於 Python 的網頁爬蟲，將設定過程完全自動化。

* **相容性：** 適用於非虛擬環境的 CMS 。
* **測試環境：** Ubuntu 22.04

## 安裝

```bash
sudo apt update
git clone https://github.com/TYCheng31/CMSSetUpTool.git
cd CMSSetUpTool
sudo apt install python3-tk
python3 gui.py
```

初次啟動圖形化介面 (GUI) 後，請先點擊 **安裝環境** 按鈕來設定必要的相依套件，接著再開始使用此工具。

## 使用指南

task的statements、testcases統一放在task_file中，檔案名稱要跟該題的題目名稱一樣
EX: Week1Q1的題目名稱為Week1Q1.pdf，測資名稱為Week1Q1.zip並放在task_file中

詳細的操作說明，請參考下方教學：
https://hackmd.io/@OgocyKRSRuKEbEqdS0BoKg/B19sOhQsbl
