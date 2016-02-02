#coding=utf-8
'''
@author: wubingbing
'''

'''

bank={'招商银行':('621485',16),
      '光大银行':('622666',16),
      '中 信银行':('622696',16),
      '建设银行':('622700',19),
      '农业银行':('620059',19),
      '工商银行':('621211',18),
      '兴业银行':('622908',16),
      '邮政银行':('621098',19),
      '广发银行':('622556',16),
      '交通银行':('622259',17),
      '民生银行':('622620',16),
      '中国银行':('621790',19),
      '平安银行':('622298',16),
      '兴业银行':('622909',16)
      }
    
for bankName in bank.keys():
    print type(bankName)

'''

'''
import xlrd

table=xlrd.open_workbook('D:\\appium\\testCase.xlsx').sheets()[0]
nrows=table.nrows
for i in range(nrows):
    #print table.row_values(i)[1].encode('UTF-8')
    key=table.row_values(i)[0]
    value=table.row_values(i)[1]
    case_dict={key: value
         }
    if key.encode('UTF-8')=='test_quickPay':
        case_desc=case_dict[key].encode('UTF-8')
    #print case_dict[key].encode('UTF-8') 
#data_caseid=table.row_values(0)
#print data_caseid
print case_desc

'''
'''
import time
import random
from gVariable import GVariable
'''
'''
t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

print t
time.sleep(3)
print t
'''
'''
print GVariable.teleNum

GVariable.teleNum=str(int(GVariable.teleNum)+1)

print GVariable.teleNum
'''
'''
def funcD(a, b, *c):
 print a
 print b
 #print "length of c is: %d " % len(c)
 print c[0]+1
 
 
funcD(0, 0,1,1,1)
'''

a="123456"
print len(a.split('.'))


