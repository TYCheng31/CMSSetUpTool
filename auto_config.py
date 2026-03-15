from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

# ==========================================
# 參數
# ==========================================
LOGIN_URL =                 "http://localhost:8889"     # cmsAdminWebServer IP (:8889)
ADMIN_USERNAME =            "admin"                     # 帳號
ADMIN_PASSWORD =            "admin"                     # 密碼
MIN_SUBMISSION_INTERVAL =   "30"                        # 繳交間隔時間
TIME_LIMIT =                "5.0"                       # 程式執行時間秒數 (秒)
MEMORY_LIMIT =              "512"                       # 程式執行空間限制 (MB)
SCORE_PER_TASK =            "4"                         # 每個測資的得分數
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
    show_more_xpath = "//a[@href='./tasks' and contains(., 'show more')]"
    show_more_element = wait.until(EC.element_to_be_clickable((By.XPATH, show_more_xpath)))
    time.sleep(1) 
    show_more_element.click()

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
        
    print(f"總共有 {len(tasks_info)} 題需要修改")
    time.sleep(2) 

    #每個task必經的修改
    for index, task in enumerate(tasks_info, start=1):
        url = task["url"]
        name = task["name"]
        
        print(f"[{index}/{len(tasks_info)}] 正在設定: {name}")
        
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

    time.sleep(5) 

except Exception as e:
    print(f"錯誤: {e}")
    time.sleep(10)

finally:
    driver.quit()