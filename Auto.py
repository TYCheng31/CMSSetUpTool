from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

# ==========================================
# 參數區
# ==========================================
LOGIN_URL =                 "http://localhost:8889"         # cmsAdminWebServer IP (:8889)
ADMIN_USERNAME =            "admin"                         # account
ADMIN_PASSWORD =            "admin"                         # password
CONTEST_NAME =              "NCUE"                          # contest name
TASK_NAMES =                ["Q1", "Q2", "Q3", "Q4", "Q5"]  # task name
#task設定
MIN_SUBMISSION_INTERVAL =   "30"                            # 繳交間隔時間
TIME_LIMIT =                "5.0"                           # 程式執行時間秒數 (秒)
MEMORY_LIMIT =              "512"                           # 程式執行空間限制 (MB)
SCORE_PER_TASK =            "4"                             # 每個測資的得分數
# ==========================================

options = webdriver.ChromeOptions()
# 讓瀏覽器背景執行就取消註解 VVVVVVVVV
# options.add_argument('--headless')                              
options.add_argument('--no-sandbox')             
options.add_argument('--disable-dev-shm-usage')  
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')
options.add_argument('--window-size=1920,1080')  

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    print(f"~~~🚀CMS全自動新增 Contest、Task 並設定參數 NCUE🚀~~~")
    print(f"正在前往: {LOGIN_URL}")
    driver.get(LOGIN_URL)

    wait = WebDriverWait(driver, 10)

    # 1. Login
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

    # 2. Create new contest
    create_contest_xpath = "//a[@href='./contests/add' and contains(., 'create new contest')]"
    create_contest_btn = wait.until(EC.presence_of_element_located((By.XPATH, create_contest_xpath)))
    driver.execute_script("arguments[0].click();", create_contest_btn)

    # 3. Input contest name
    name_input = wait.until(EC.presence_of_element_located((By.NAME, "name")))
    name_input.clear()
    name_input.send_keys(CONTEST_NAME)
    
    # Submit contest
    submit_btn_xpath = "(//input[@type='submit'])[last()]"
    submit_btn = wait.until(EC.presence_of_element_located((By.XPATH, submit_btn_xpath)))
    driver.execute_script("arguments[0].click();", submit_btn)
    print(f"contest {CONTEST_NAME} 建立完成")

    # 4. Create new tasks (Q1~Q5)
    driver.get(LOGIN_URL)
    total_tasks = len(TASK_NAMES)
    print(f"開始建立 {total_tasks} 個 task...")

    for index, task_name in enumerate(TASK_NAMES, start=1):
        print(f"[{index}/{total_tasks}] 正在建立task: {task_name}")

        create_task_xpath = "//a[contains(@href, 'tasks/add') and contains(., 'create new task')]"
        create_task_btn = wait.until(EC.presence_of_element_located((By.XPATH, create_task_xpath)))
        driver.execute_script("arguments[0].click();", create_task_btn)

        task_name_input = wait.until(EC.presence_of_element_located((By.NAME, "name")))
        task_name_input.clear()
        task_name_input.send_keys(task_name)

        submit_task_btn_xpath = "(//input[@type='submit'])[last()]"
        submit_task_btn = wait.until(EC.presence_of_element_located((By.XPATH, submit_task_btn_xpath)))
        driver.execute_script("arguments[0].click();", submit_task_btn)

        print(f"  -> {task_name} 建立完成！")
        time.sleep(1)
        
    print("🎉 task全部建立完成! 準備進入參數設定階段...")
    time.sleep(1)


    # ========================================================
    # 題目設定
    # ========================================================
    driver.get(LOGIN_URL)
    # 按下 show more (task)
    show_more_xpath = "//a[@href='./tasks' and contains(., 'show more')]"
    show_more_element = wait.until(EC.element_to_be_clickable((By.XPATH, show_more_xpath)))
    driver.execute_script("arguments[0].click();", show_more_element)
    time.sleep(1)

    # 抓取目前所有 task 網址
    print("抓取所有題目中...")
    tasks_xpath = "//td/a[contains(@href, './task/')]"
    task_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, tasks_xpath)))
    
    tasks_info = []
    for element in task_elements:
        t_name = element.text
        t_url = element.get_attribute("href")
        tasks_info.append({
            "name": t_name,
            "url": t_url
        })
        
    print(f"總共有 {len(tasks_info)} 題需要修改設定")
    time.sleep(2) 

    # 6. 每個 task 必經的修改迴圈
    for index, task in enumerate(tasks_info, start=1):
        url = task["url"]
        name = task["name"]
        
        print(f"[{index}/{len(tasks_info)}] 正在設定: {name}")
        
        driver.get(url)
        
        # Minimum interval between submissions
        input_xpath = "//input[@name='min_submission_interval']"
        input_element = wait.until(EC.presence_of_element_located((By.XPATH, input_xpath)))
        input_element.clear()
        input_element.send_keys(MIN_SUBMISSION_INTERVAL)
        
        # Score mode
        select_element = wait.until(EC.presence_of_element_located((By.NAME, "score_mode")))
        score_select = Select(select_element)
        score_select.select_by_value("max")

        # Time limit
        time_xpath = "//input[starts-with(@name, 'time_limit_')]"
        time_input = wait.until(EC.presence_of_element_located((By.XPATH, time_xpath)))
        time_input.clear()
        time_input.send_keys(TIME_LIMIT)

        # Memory limit
        mem_xpath = "//input[starts-with(@name, 'memory_limit_')]"
        mem_input = wait.until(EC.presence_of_element_located((By.XPATH, mem_xpath)))
        mem_input.clear()
        mem_input.send_keys(MEMORY_LIMIT)

        # Score Parameters
        score_param_xpath = "//textarea[starts-with(@name, 'score_type_parameters_')]"
        score_param_input = wait.until(EC.presence_of_element_located((By.XPATH, score_param_xpath)))
        score_param_input.clear()
        score_param_input.send_keys(SCORE_PER_TASK)

        # Update 按鈕
        update_btn_xpath = "//input[@type='submit' and @value='Update']"
        update_btn = wait.until(EC.presence_of_element_located((By.XPATH, update_btn_xpath)))
        driver.execute_script("arguments[0].click();", update_btn)
        
        print(f"  -> {name} 設定完成")
        time.sleep(1) 
        
    print("所有task設定完成！")

    time.sleep(5) 

except Exception as e:
    print(f"錯誤: {e}")
    time.sleep(10)

finally:
    driver.quit()