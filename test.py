#coding=utf-8
'''
@author: wubingbing
'''

import unittest
from appium import webdriver
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from db import Db
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Xnol(unittest.TestCase):
    
    def setUp(self):
        
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = 'YQ601'
        '''
        desired_caps['app'] = PATH(
            'C:\Users\Administrator\Desktop\XNOnline_1.0.19.apk'
        )
        '''
        desired_caps['appPackage'] = 'com.xiaoniu.finance'
        desired_caps['appActivity'] = '.ui.LaucherTaskActivity'
        desired_caps['appWaitActivity']= '.ui.MainActivity'
        desired_caps["unicodeKeyboard"] = "True"  
        desired_caps["resetKeyboard"] = "True"  
        
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Xnol)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    