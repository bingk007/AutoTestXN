#coding=utf-8
'''
Created on 2015年7月20日

@author: Administrator
'''

class MyError(Exception):
    def __init__(self,error):
        self.error=error
        print error
        

