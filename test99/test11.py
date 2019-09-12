#coding:utf8
'''
Created on 2019��9��11��

@author: admin
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

exepath="lib/chromedriver.exe"
class Web():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=exepath)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def upload(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.XPATH,"//span[@class='soutu-btn']").click()
#         self.driver.find_element(By.CSS_SELECTOR, "[class='upload-pic']").send_keys("C:/Users/admin/Desktop/3.jpg")
        self.driver.find_element(By.CSS_SELECTOR, "[class='upload-pic']").send_keys("C:/Users/admin/Desktop/3.jpg")
        time.sleep(5)
        
    
    def close(self):
        time.sleep(3)
        self.driver.quit()
        
        