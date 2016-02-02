#coding=utf-8
'''
@author: wubingbing
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

        while True:
            try:
                if self.driver.find_element_by_name('首页'): 
                    break
            except:
                self.driver.keyevent(4)

                
        
    def getVercode(self,teleNum):
        time.sleep(5)
        content=Db("xnmsg").sql("SELECT content FROM sms_sendlog_his WHERE mobile="+teleNum+" ORDER BY id DESC LIMIT 1 ")
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
        
        

        
    
        
        