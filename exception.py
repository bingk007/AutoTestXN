#coding=utf-8
'''
@author: wubingbing
'''

class MyError(Exception):
    def __init__(self,error):
        self.error=error
        print error
        
