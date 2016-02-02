#coding=utf-8
'''
Created on 2015年12月7日

@author: wubingbing
'''

import requests
import json

'''
payload={'cpatchaCode':'?',
         'password':'c71456db4f16287df23bdb9741a354932306fb416916cad89d8d82e9e56bbcd20c120c0c01c1751da92d9714cabe216362df6b8f066604f051fdc2774f08311ebb313616a11f7339a9d9469bce3702f0e93c32d8fddf23c7f936ae4915567e302233a11b9d15b08b91779a5f8997fe54ef1f30b4461285838016281905d63de6',
         'userName':'manchao2015'}
r=requests.post('http://172.20.20.215:8002/mobile/200/login.json', data=payload)

print (r.text)
'''
'''
r=requests.get('http://172.20.20.215:8002/mobile/400/home.json')
print (r.text)
'''

cookies={'osType':'ANDROID', 
         'appType':'XNONLINE',
         'deviceId':'ff5d7996-93aa-4a8c-9c4c-3f01d3b3ef8b',
         'channelId':'xn_internal',
         'appCode':'200010',
         'versionCode':'2.0.1.1208',
         'isAutoLogin':'true',
         'autoToken':'ICGQPN3YCC3X81I935JSVAN77JY5G35N',
         'JSESSIONID':'A51AAD9C35BE4D4255C5F9BC5195CA4B-n2',
         'Path':'/mobile/'}


r=requests.get('http://172.20.20.215:8002/mobile/my/account/details.json',cookies=cookies)

a=r.json()['data']
print a
b=a['bankName'].encode('UTF-8')
print b
#print a[].encode('UTF-8')
#print type(json.dumps(a))
#print type(json.loads(a))
#print (json.loads(a))


