#coding=UTF-8

'''
@author: wubingbing
'''
import requests
import json
from exception import MyError
from cMethod import CMethod

class Request():
    

    cookies={'osType':'ANDROID', 
             'appType':'',
             'deviceId':'ff5d7996-93aa-4a8c-9c4c-3f01d3b3ef8b',
             'channelId':'',
             'appCode':'',
             'versionCode':'',
             'isAutoLogin':'true',
             'autoToken':'',
             'JSESSIONID':'',
             'Path':'/mobile/'}

    def getData(self,url):
        r=requests.get(url,cookies=self.cookies)
        if r.json()['code']==u'M00000':
            return r.json()['data']
        else:
            raise MyError(r.text)
        
        
    def getList(self,url):
        r=requests.get(url,cookies=self.cookies)
        if r.json()['code']==u'M00000':
            return r.json()['data']['list']
        else:
            raise MyError(r.text)
        
        
    def assertResult(self,bResult,fResult,msg="Fail"):
        
        bResultOr=str(bResult).encode('UTF-8')
        if len(bResultOr.split('.'))==1:
            bResultOr=bResultOr+'.00'
        elif len(bResultOr.split('.')[1])==1:
            bResultOr=bResultOr+'0'   
        CMethod().assertEqual(bResultOr, fResult)




