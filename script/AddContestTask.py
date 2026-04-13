from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
from config import *

options = webdriver.ChromeOptions()

if globals().get('HEADLESS_MODE', False):
    options.add_argument('--headless') 

options.add_argument('--no-sandbox')             
options.add_argument('--disable-dev-shm-usage')  
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')
options.add_argument('--window-size=1920,1080')  

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    print(f"~~~🚀CMS全自動新增Contest、Task NCUE用🚀~~~")
    print(f"正在前往: {LOGIN_URL}")
    driver.get(LOGIN_URL)

    wait = WebDriverWait(driver, 10)

    #login
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

    #creat new contest
    create_contest_xpath = "//a[@href='./contests/add' and contains(., 'create new contest')]"
    create_contest_btn = wait.until(EC.presence_of_element_located((By.XPATH, create_contest_xpath)))
    driver.execute_script("arguments[0].click();", create_contest_btn)

    #input contest name
    name_input = wait.until(EC.presence_of_element_located((By.NAME, "name")))
    name_input.clear()
    name_input.send_keys(CONTEST_NAME)
    
    #submit
    submit_btn_xpath = "(//input[@type='submit'])[last()]"
    submit_btn = wait.until(EC.presence_of_element_located((By.XPATH, submit_btn_xpath)))
    driver.execute_script("arguments[0].click();", submit_btn)

    #creat new task
    driver.get(LOGIN_URL)
    total_tasks = len(TASK_NAMES)
    print(f"開始建立 {total_tasks} 個task")

    for index, task_name in enumerate(TASK_NAMES, start=1):
        print(f"[{index}/{total_tasks}] 正在建立task: {task_name}")

        # create new task
        create_task_xpath = "//a[contains(@href, 'tasks/add') and contains(., 'create new task')]"
        create_task_btn = wait.until(EC.presence_of_element_located((By.XPATH, create_task_xpath)))
        driver.execute_script("arguments[0].click();", create_task_btn)

        # input task name
        task_name_input = wait.until(EC.presence_of_element_located((By.NAME, "name")))
        task_name_input.clear()
        task_name_input.send_keys(task_name)

        # submit
        submit_task_btn_xpath = "(//input[@type='submit'])[last()]"
        submit_task_btn = wait.until(EC.presence_of_element_located((By.XPATH, submit_task_btn_xpath)))
        driver.execute_script("arguments[0].click();", submit_task_btn)

        print(f"  -> {task_name} 建立完成！")
        time.sleep(1)
        
    print("🎉 task全部建立完成!")

except Exception as e:
    print(f"錯誤: {e}")
    time.sleep(10)

finally:
    driver.quit()