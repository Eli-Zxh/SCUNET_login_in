import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
#import pyautogui

# 初始化浏览器
browser = webdriver.Edge()
browser.get("http://192.168.2.135")

# 用户信息
user_name = '2021151620070' #输入你的学号
user_pwd = '232693' #输入你的密码
service_typelist = {
    '校园网': 'bch_service_0',
    '中国联通': 'bch_service_3',
    '中国电信': 'bch_service_2',
    '中国移动': 'bch_service_1'
}
target_service_value = '校园网'  # 这里选择你想使用的服务类型

try:
    # 等待用户名输入框可见并输入（通过 `ID` 定位）
    username_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username_input.clear()  # 清空输入框
    username_input.send_keys(user_name)

    # 定位密码输入框并通过 JavaScript 设置值（通过 `ID` 定位）
    password_input = browser.find_element(By.ID, "pwd")
    browser.execute_script("arguments[0].value = arguments[1];", password_input, user_pwd)
    # 如果需要模拟键盘输入
    # ActionChains(browser).move_to_element(password_input).click().send_keys(user_pwd).perform()
    # password_input.click()
    # time.sleep(1)  # 等待焦点切换
    # # 模拟键盘输入
    # pyautogui.write(user_pwd)

    # 点击服务选择框（通过 `ID` 定位）
    service_selector = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "defaultService"))
    )
    service_selector.click()

    # 选择目标服务类型（通过 `ID` 定位）
    target_service_id = service_typelist.get(target_service_value, '')
    if target_service_id:
        service_option = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, target_service_id))
        )
        service_option.click()
    else:
        raise Exception(f"未找到服务类型：{target_service_value}")

    # 等待登录按钮可点击并点击（通过 `ID` 定位）
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "loginLink"))
    )
    login_button.click()

    time.sleep(3)

finally:
    browser.quit()  # 关闭浏览器
