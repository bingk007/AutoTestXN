#coding=UTF-8

'''
Created on 2015年7月7日

@author: Administrator
'''
import MySQLdb

class Db:
    def __init__(self):
        self.conn=MySQLdb.connect(
            host='172.20.77.41',
            port =3306,
            user='root',
            passwd='123456',
            db ='xnmsg',
            charset='utf8'
            )
        
    def sql(self,sqlStr):   
        cur =self.conn.cursor()
        cur.execute(sqlStr)
        for row in cur.fetchall():    
            for r in row:    
                return r
        cur.close()
        self.conn.close()
'''
a=Db().sql("SELECT content FROM sms_sendlog_his WHERE mobile='18938055502' ORDER BY id DESC LIMIT 1")

'''
