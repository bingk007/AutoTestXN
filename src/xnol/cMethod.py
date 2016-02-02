#coding=UTF-8
'''
Created on 2015年12月21日

@author: wubingbing
'''

from unittest import TestCase
 
class CMethod(TestCase):
     
    def __init__(self):
        self._type_equality_funcs = {}
        
        
        
    def assertText(self,first,second):
        firstS=str(first).encode('UTF-8')
        self.assertEqual(firstS, second)