#coding=utf-8
'''
Created on 2015年7月21日

@author: Administrator
'''
import time
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from db import Db
from appium.webdriver.common.touch_action import TouchAction
from cMethod import CMethod

class Common:
    
    
    
    def __init__(self,driver):
        self.driver=driver
        
        
    
    def recover(self):
        for i in range(2):
            try:
                self.driver.implicitly_wait(1)
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME,'首页')))
            except:
                self.driver.keyevent(4)

                
                #self.driver.start_activity('com.xiaoniu.finance','.ui.MainActivity')
        
    def getVercode(self,teleNum):
        time.sleep(5)
        content=Db().sql("SELECT content FROM sms_sendlog_his WHERE mobile="+teleNum+" ORDER BY id DESC LIMIT 1 ")
        code_zc=filter(str.isdigit,content.encode('UTF-8'))
        return code_zc
        print code_zc

    def getSize(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return(x,y)
    
    def swipeLeft(self,t):
        l=self.getSize()
        x1=int(l[0]*0.75)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.25)
        self.driver.swipe(x1,y1,x2,y1,t)
        
    def swipeRight(self,t):
        l=self.getSize()
        x1=int(l[0]*0.25)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.75)
        self.driver.swipe(x1,y1,x2,y1,t)
        
    def swipeUp(self,t):
        l=self.getSize()
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.75)
        y2=int(l[1]*0.25)
        self.driver.swipe(x1,y1,x1,y2,t)

        
    def swipeDown(self,t):
        l=self.getSize()
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.25)
        y2=int(l[1]*0.75)
        self.driver.swipe(x1,y1,x1,y2,t)
    
    
    def gesture(self):
        el=self.driver.find_elements_by_class_name('android.view.View')
        TouchAction(self.driver).press(el[0]).move_to(el[1]).move_to(el[4]).move_to(el[7]).move_to(el[8]).release().perform()
        
        

        
    
        
        