from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import tkinter as tk
from tkinter import ttk
from config import *

# ==========================================
# 建立選擇題目的圖形化介面 (GUI)
# ==========================================
def select_tasks_gui(tasks_info):
    selected_tasks = []
    
    root = tk.Tk()
    root.title("請勾選要自動設定的題目")
    
    # 設定較大的預設尺寸，並嘗試自動最大化視窗
    root.geometry("900x600")
    root.configure(padx=20, pady=20)
    
    # 標題
    tk.Label(root, text="勾選需要自動設定的題目 (預設全選):", font=("Arial", 14, "bold")).pack(pady=(0, 10))
    
    # 建立可滾動的區域
    frame_container = tk.Frame(root)
    frame_container.pack(fill=tk.BOTH, expand=True)
    
    canvas = tk.Canvas(frame_container)
    scrollbar = ttk.Scrollbar(frame_container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # --- 支援滑鼠滾輪 ---
    def _on_mousewheel(event):
        if event.num == 4:    # Linux 滾輪向上
            canvas.yview_scroll(-1, "units")
        elif event.num == 5:  # Linux 滾輪向下
            canvas.yview_scroll(1, "units")
        else:                 # Windows 滾輪
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    canvas.bind_all("<Button-4>", _on_mousewheel)
    canvas.bind_all("<Button-5>", _on_mousewheel)
    
    # ==========================================
    # 動態產生 Checkbuttons (改為網格排列)
    # ==========================================
    check_vars = []
    MAX_COLUMNS = 5  # <--- 這裡可以修改一排要顯示幾個題目
    
    for index, task in enumerate(tasks_info):
        var = tk.BooleanVar(value=True) # 預設為勾選 (True)
        chk = tk.Checkbutton(scrollable_frame, text=task["name"], variable=var, font=("Arial", 12))
        
        # 計算應該被放在第幾列 (row)、第幾欄 (column)
        row = index // MAX_COLUMNS
        col = index % MAX_COLUMNS
        
        # 用 grid 將元件由左至右排列，並加上適當的間距
        chk.grid(row=row, column=col, sticky="w", pady=5, padx=20)
        
        check_vars.append((task, var))
        
    # 全選 / 取消全選 功能
    def select_all():
        for _, var in check_vars: var.set(True)
        
    def deselect_all():
        for _, var in check_vars: var.set(False)
        
    btn_frame = tk.Frame(root)
    btn_frame.pack(fill=tk.X, pady=15)
    tk.Button(btn_frame, text="全部勾選", font=("Arial", 11), command=select_all).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10)
    tk.Button(btn_frame, text="取消全選", font=("Arial", 11), command=deselect_all).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10)
    
    # 確認按鈕的觸發事件
    def on_confirm():
        for task, var in check_vars:
            if var.get():  # 如果有被勾選
                selected_tasks.append(task)
                
        # 關閉視窗前解除滾輪綁定，避免影響其他 Tkinter 視窗
        canvas.unbind_all("<MouseWheel>")
        canvas.unbind_all("<Button-4>")
        canvas.unbind_all("<Button-5>")
        root.destroy() 
        
    tk.Button(root, text="確認並開始執行", bg="#5cb85c", fg="black", font=("Arial", 14, "bold"), height=2, command=on_confirm).pack(fill=tk.X, pady=5)
    
    # 啟動並阻斷程式，直到視窗關閉
    root.mainloop()
    
    return selected_tasks

# ==========================================
# 主程式 (Selenium)
# ==========================================
options = webdriver.ChromeOptions()

# 從 config.py 讀取是否要使用 Headless 模式
if globals().get('HEADLESS_MODE', False):
    options.add_argument('--headless')                              

options.add_argument('--no-sandbox')             
options.add_argument('--disable-dev-shm-usage')  
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')
options.add_argument('--window-size=1920,1080')  

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    print(f"~~~🚀CMS全自動設定開始🚀~~~")
    #前往頁面
    print(f"正在前往: {LOGIN_URL}")
    driver.get(LOGIN_URL)

    wait = WebDriverWait(driver, 10)

    #輸入帳號密碼
    print("等待登入欄位")
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_input.clear()
    username_input.send_keys(ADMIN_USERNAME)
    
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_input.clear()
    password_input.send_keys(ADMIN_PASSWORD)
    
    login_button_xpath = "//button[@type='submit' and contains(text(), 'Login')]"
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, login_button_xpath)))
    login_button.click()
    print("登入成功")

    #按下show more (task)
    tasks_link_xpath = "//a[contains(@href, 'tasks') and text()='Tasks']"
    tasks_link_element = wait.until(EC.presence_of_element_located((By.XPATH, tasks_link_xpath)))
    driver.execute_script("arguments[0].click();", tasks_link_element)
    time.sleep(1) 

    #抓取目前所有task
    tasks_xpath = "//td/a[contains(@href, './task/')]"
    task_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, tasks_xpath)))
    
    tasks_info = []
    for element in task_elements:
        task_name = element.text
        task_url = element.get_attribute("href")
        tasks_info.append({
            "name": task_name,
            "url": task_url
        })
        
    # ========================================================
    # 💡 新增：將抓取到的題目依據名稱 (字母順序) 進行排序
    # (加入 .lower() 是為了不區分大小寫，確保 A 和 a 排序在一起)
    # ========================================================
    tasks_info = sorted(tasks_info, key=lambda x: x["name"].lower())
        
    print(f"總共抓取到 {len(tasks_info)} 題，等待使用者勾選...")
    
    # 呼叫 GUI 讓使用者勾選
    tasks_to_update = select_tasks_gui(tasks_info)
    
    if not tasks_to_update:
        print("沒有勾選任何題目，程式結束。")
    else:
        print(f"開始執行，共 {len(tasks_to_update)} 題需要修改")
        time.sleep(1) 

        # 針對使用者「勾選的題目」進行修改
        for index, task in enumerate(tasks_to_update, start=1):
            url = task["url"]
            name = task["name"]
            
            print(f"[{index}/{len(tasks_to_update)}] 正在設定: {name}")
            
            driver.get(url)
            
            #Minimum interval between submissions
            input_xpath = "//input[@name='min_submission_interval']"
            input_element = wait.until(EC.presence_of_element_located((By.XPATH, input_xpath)))
            input_element.clear()
            input_element.send_keys(MIN_SUBMISSION_INTERVAL)
            
            #Score mode
            select_element = wait.until(EC.presence_of_element_located((By.NAME, "score_mode")))
            score_select = Select(select_element)
            score_select.select_by_value("max")

            #Time limit
            time_xpath = "//input[starts-with(@name, 'time_limit_')]"
            time_input = wait.until(EC.presence_of_element_located((By.XPATH, time_xpath)))
            time_input.clear()
            time_input.send_keys(TIME_LIMIT)

            #Memory limit
            mem_xpath = "//input[starts-with(@name, 'memory_limit_')]"
            mem_input = wait.until(EC.presence_of_element_located((By.XPATH, mem_xpath)))
            mem_input.clear()
            mem_input.send_keys(MEMORY_LIMIT)

            #Score Parameters
            score_param_xpath = "//textarea[starts-with(@name, 'score_type_parameters_')]"
            score_param_input = wait.until(EC.presence_of_element_located((By.XPATH, score_param_xpath)))
            score_param_input.clear()
            score_param_input.send_keys(SCORE_PER_TASK)

            #Update
            update_btn_xpath = "//input[@type='submit' and @value='Update']"
            update_btn = wait.until(EC.presence_of_element_located((By.XPATH, update_btn_xpath)))
            driver.execute_script("arguments[0].click();", update_btn)
            
            print(f"  -> {name} 設定完成")
            time.sleep(1) 
            
        print("全部設定完成")

    time.sleep(3) 

except Exception as e:
    print(f"錯誤: {e}")
    time.sleep(10)

finally:
    driver.quit()