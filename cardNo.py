#coding=utf-8
'''
@author: wubingbing
'''

import random
class CardNO:

    bank={'招商银行':('621485',16),
          '光大银行':('622666',16),
          '中信银行':('621773',16),
          '建设银行':('622700',19),
          '农业银行':('622848',19),
          '工商银行':('622202',19),
          '兴业银行':('622908',16),
          '邮储银行':('621098',19),
          '广发银行':('622556',16),
          '交通银行':('622259',17),
          '民生银行':('622620',16),
          '中国银行':('621790',19),
          '平安银行':('621626',19)
          }
         
    def makeNO(self,bankName):    
        cardNO1=''.join(random.choice('0123456789') for i in range(self.bank[bankName][1]-7))
        cardNO2=self.bank[bankName][0]+cardNO1
        c=tuple(cardNO2)
        s1=0
        s2=0
        for i in range(self.bank[bankName][1]-1):
            if i%2==0:
                a=int(c[(self.bank[bankName][1]-2)-i])*2
                b=tuple(str(a))  
                if len(b)==2:
                    s1=s1+int(b[0])+int(b[1])
                else:
                    s1=s1+a
            else:
                d=int(c[(self.bank[bankName][1]-2)-i])
                s2=s2+d

        e=tuple(str(s1+s2))
        f=int(e[len(e)-1])
        if f==0:
            n=0
        else:
            n=10-f
        cardNO=cardNO2+str(n)
        return cardNO

