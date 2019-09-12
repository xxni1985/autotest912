#coding:utf8
'''
Created on 2019��9��11��

@author: admin
'''
from selenium import webdriver
from asyncio.tasks import sleep

exepath="lib/chromedriver.exe"
class Web():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=exepath)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def close(self):
        sleep(4)
        self.driver.quit()
        
        