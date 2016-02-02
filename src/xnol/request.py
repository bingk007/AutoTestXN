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
             'appType':'XNONLINE',
             'deviceId':'ff5d7996-93aa-4a8c-9c4c-3f01d3b3ef8b',
             'channelId':'xn_internal',
             'appCode':'200010',
             'versionCode':'2.0.1.1208',
             'isAutoLogin':'true',
             'autoToken':'AMGRM8K20BK9T8FDOGR5RVFLYIKVPCDE',
             'JSESSIONID':'55325D13FC620AE64069C1182095ACAD-n2',
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

'''
respon=Request().getList('http://172.20.20.215:8002/mobile/my/funds/200/detail.json?month=0&pageSize=20&year=0&type=all&pageNum=1')
#Request().assertResult(respon['totalEarningsAmount'],"1198.58")
print type(respon[0])
'''


