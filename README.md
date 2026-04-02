# CMS 自動化設定工具

傳統的 CMS (Contest Management System，競賽管理系統) 需要手動設定每一道題目。
此工具基於 Python 的網頁爬蟲，將設定過程完全自動化。
- 自動上傳題目敘述statements
- 自動上傳題目測資testcases
- 自動配置各題目設定(測資分數、程式碼執行時間、程式碼執行限制記憶體、題目繳交間隔時間限制)  
  
* **相容性：** 適用於非虛擬環境的 CMS 。
* **測試環境：** Ubuntu 22.04

## 一鍵安裝

```bash
curl -sSL https://raw.githubusercontent.com/TYCheng31/CMSSetUpTool/master/install.sh | bash
```

## 使用指南

task的statements、testcases統一放在task_file中，檔案名稱要跟該題的題目名稱一樣  
EX: Week1Q1的題目名稱為Week1Q1.pdf，測資名稱為Week1Q1.zip並放在task_file中  

詳細的操作說明，請參考[使用教學](https://hackmd.io/@OgocyKRSRuKEbEqdS0BoKg/Sku88wjsbl)
