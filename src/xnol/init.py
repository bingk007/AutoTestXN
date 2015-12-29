#coding=utf-8
#!/usr/bin/env python
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Init():
    def __init__(self,driver):
        self.driver=driver
        
        
    def test_launch(self):
        time.sleep(5)
        for i in range(3):
            self.driver.swipe(600, 600, 100, 600, 500)
            time.sleep(1)
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_name("立即体验").click()
            
    def test_environment(self):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME,'更多')))
            self.driver.find_element_by_name("更多").click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME,'欢迎页')))
            self.driver.find_element_by_name("欢迎页").click()
            time.sleep(1)
            self.driver.tap([(100,100),(100,200),(100,300)], 500)
            time.sleep(1)
            '''
            for i in range(2):
                self.driver.tap([(100,100)], 500)
                time.sleep(1)
                self.driver.swipe(600, 600, 100, 600, 500)
                time.sleep(1)
            '''    
            self.driver.tap([(100,100)], 500)
            time.sleep(1)
            self.driver.swipe(600, 600, 100, 600, 500)
            time.sleep(1)
            #self.driver.tap([(100,100)], 100)
            self.driver.swipe(600, 600, 100, 600, 500)
            self.driver.implicitly_wait(2)
            self.driver.find_element_by_name("立即体验").click()

    
            
            