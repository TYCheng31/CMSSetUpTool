# ==========================================
# CMS 全自動化通用設定檔 (config.py)
# 所有的參數都在這裡集中管理，修改此檔案即可套用到所有腳本
# ==========================================

LOGIN_URL =                 "http://localhost:8889"         # cmsAdminWebServer IP (:8889)
ADMIN_USERNAME =            "admin"                         # 系統帳號
ADMIN_PASSWORD =            "admin"                         # 系統密碼

CONTEST_NAME =              "NCUE"                          # 競賽名稱
TASK_NAMES =                ["Q1", "Q2", "Q3", "Q4", "Q5"]  # 任務名稱清單

MIN_SUBMISSION_INTERVAL =   "30"                            # 繳交間隔時間 (秒)
TIME_LIMIT =                "5.0"                           # 程式執行時間秒數 (秒)
MEMORY_LIMIT =              "512"                           # 程式執行空間限制 (MB)
SCORE_PER_TASK =            "4"                             # 每個測資的得分數

HEADLESS_MODE = True
