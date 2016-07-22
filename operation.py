#coding=UTF-8
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
import xlrd
from pydoc import replace
from request import Request
from cMethod import CMethod

class Operation:
    
    def __init__(self,driver):
        self.driver=driver
        
        
    def accessAccountInfo(self):
        Common(self.driver).recover()
        self.driver.find_element_by_name('我的').click()
        self.driver.find_element_by_name('大大君').click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'账户信息')))


    def accessProduct(self):
        Common(self.driver).recover()
        self.driver.find_elements_by_id('com.package:id/menu_item')[1].click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'项目分类')))
        self.driver.find_element_by_name('项目分类').click()
        
        
#     def checkButtom(self):
#         try:
#             self.driver.find_element_by_class_name().click()
#         except:
#             self.driver.keyevent(4)
#             
        