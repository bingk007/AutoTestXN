#coding=utf-8
'''
@author: wubingbing
'''

import random

class GVariable:
    
    teleNum=random.choice(['150','137','189'])+''.join(random.choice('0123456789') for i in range(8))
    
    httpUrl='http://172.20.20.215:8002/mobile/'
    httpsUrl='https://172.20.20.215:8447/mobile/'
