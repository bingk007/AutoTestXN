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



class Product(unittest.TestCase):
    
    def __init__(self,driver):
        self.driver=driver
        
    def test_buyYyn(self,value):
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys(value)
        self.driver.find_element_by_name('确定购买').click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'成功购买月月牛'+value+'.00元')))
        

    def test_buyDay(self,value):
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys(value)
        self.driver.find_element_by_name('确定购买').click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'成功购买天天牛'+value+'.00元')))
        
        
    def test_withdrawDay(self,value,passWord):
        edit=self.driver.find_elements_by_class_name('android.widget.EditText')
        edit[0].send_keys(value)
        edit[1].send_keys(passWord)
        self.driver.find_element_by_name('确定提取').click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'恭喜您，提取申请已提交成功')))
        
        
    def test_buyAxn(self,value):
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys(value)
        self.driver.find_element_by_name('立即加入').click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'成功加入安心牛'+value+'.00元')))
        
    def test_buyProduct(self,value,name):
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys(value)
        self.driver.find_element_by_name('立即购买').click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'恭喜您，成功购买'+name.encode('UTF-8')+value+'.00元')))
    
    def test_buyZhuan(self,value,name):
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys(value)
        self.driver.find_element_by_name('立即购买').click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'成功购买'+name.encode('UTF-8')+value+'.00元')))
        
    def test_buyExperience(self):
        self.driver.find_element_by_name('仅支持理财金券购买').click()
        self.driver.find_elements_by_class_name('android.widget.CompoundButton')[0].click()
        self.driver.find_element_by_name('确认购买').click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'恭喜您，成功购买理财体验标1,000.00元')))
        
        
        
        