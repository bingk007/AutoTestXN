#coding=utf-8
'''
@author: wubingbing
'''

import random
import unittest
import os
from appium import webdriver
import time
from photo import Appium_Extend
from verCode import getVerCode
from idNo import IdNo
from db import Db
from cardNo import CardNO
from common import Common
from gVariable import GVariable
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lib2to3.pgen2.driver import Driver


class About(unittest.TestCase):
    
    def __init__(self,driver):
        self.driver=driver
        
        
    def test_openHtmlPage(self,text,title):
        self.driver.find_element_by_name(text).click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,title)))
    
    
    def test_feedback(self,text):
        self.driver.find_element_by_name('意见反馈').click()
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys(text)
        self.driver.find_element_by_name('提交').click()
        
        
    def test_update(self,text):
        self.driver.find_element_by_name('版本更新').click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,text)))
        
        
    def test_welcome(self):
        self.driver.find_element_by_name('欢迎页').click()
        for i in range(2):
            Common(self.driver).swipeLeft(500)
        self.driver.find_element_by_name('立即体验').click()
        
        
        
        