from selenium import webdriver

from selenium.webdriver.common.by import By
import time 
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5501/Lazy%20Sheep%20Notebook.html")
# driver.find_element(By.NAME," ").send_keys("1111")
driver.find_element(By.XPATH,'//*[@id="todoapp"]/section/header/input').send_keys("111121324244444444")
driver.find_element(By.XPATH,'//*[@id="todoapp"]/section/section/ul/li[2]/div/label').click()
time.sleep(100)  # 等待10秒