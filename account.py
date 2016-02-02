#coding=UTF-8
'''
@author: wubingbing
'''

import random
import unittest
import os
from appium import webdriver
import time
from photo import Appium_Extend
from verCode import getVerCode
from idNo import IdNo
from db import Db
from cardNo import CardNO
from common import Common
from gVariable import GVariable
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import xlrd
from pydoc import replace
from request import Request
from cMethod import CMethod

class Account(unittest.TestCase):
    
    
    def __init__(self,driver):
        self.driver=driver
        

        
    def test_register(self):
        '''
        code=self.driver.find_element_by_id("com.xiaoniu.finance:id/login_iv_code")
        Appium_Extend(self.driver).get_screenshot_by_element(code)
        Appium_Extend(self.driver).write_to_file("E:\python\Lib\site-packages\pytesser", "codePhoto","tif") 
        vercode=getVerCode().getverify('codePhoto.tif')
        
        '''
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_name("免费注册").click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_name("请输入手机号码").send_keys(GVariable.teleNum)
        print GVariable.teleNum
        self.driver.find_element_by_name('推荐人').click()
        self.driver.find_element_by_name("推荐人的用户名或手机号").send_keys('manchao')
        self.driver.find_element_by_name("下一步").click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_name("确定").click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'注册')))
        views=self.driver.find_elements_by_class_name('android.widget.EditText')
        views[0].send_keys('aaa12345')
        views[1].send_keys(Common(self.driver).getVercode(GVariable.teleNum))
        self.driver.find_element_by_name("完成注册").click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'恭喜您，注册成功!')))
        
        
    def test_quickPay(self,bank):
        self.driver.activate_ime_engine('io.appium.android.ime/.UnicodeIME')
        self.driver.find_element_by_name("请输入您的开户姓名").send_keys(u"小牛君")
        self.driver.find_element_by_name("请输入您的身份证号").send_keys(IdNo().makeNO())
        self.driver.deactivate_ime_engine()
        self.driver.find_element_by_name("请选择您的银行卡开户银行").click()
        if bank=='邮储银行':
            time.sleep(1)
            Common(self.driver).swipeUp(500)
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_name(bank).click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_name("请输入您的银行卡号").send_keys(CardNO().makeNO(bank))
        #self.driver.find_element_by_name("请输入银行预留手机号").click()
        self.driver.find_element_by_name("请输入银行预留手机号").send_keys(GVariable.teleNum)
        #self.driver.hide_keyboard()
        self.driver.find_element_by_name('下一步').click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'完成开通认证')))
        if bank=='邮储银行':
            self.driver.find_element_by_name("请输入验证码").send_keys(Common(self.driver).getVercode(GVariable.teleNum)[0:6])
        else:
            self.driver.find_element_by_name("请输入验证码").send_keys('123456')
        self.driver.find_element_by_name("完成开通认证").click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'恭喜您，开通认证支付成功!')))
        
        
    def test_transPass(self):
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'交易密码')))
        views=self.driver.find_elements_by_class_name('android.widget.EditText')
        views[0].send_keys('a1234567')
        views[1].send_keys('a1234567')
        self.driver.find_element_by_name('确定').click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'恭喜您，交易密码设置成功！')))
        
        
    def test_recharge(self):
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'充值金额')))
        self.driver.find_element_by_name("请输入金额").click()
        self.driver.find_element_by_name("请输入金额").send_keys('9999')
        #self.driver.hide_keyboard()
        self.driver.find_element_by_name('下一步').click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'确认充值')))
        views=self.driver.find_elements_by_class_name('android.widget.EditText')
        views[0].send_keys(Common(self.driver).getVercode(GVariable.teleNum)[-6:])
        views[1].send_keys('a1234567')
        #self.driver.hide_keyboard()
        self.driver.find_element_by_name('确认充值').click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'恭喜您！充值成功')))
        
        
    def test_withdraw(self):
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'提现金额'))) 
        self.driver.find_element_by_id("com.xiaoniu.finance:id/et_input").click()       
        self.driver.find_element_by_id("com.xiaoniu.finance:id/et_input").send_keys('1000')
        #self.driver.hide_keyboard()
        self.driver.find_element_by_name('下一步').click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'提现金额')))
        views=self.driver.find_elements_by_class_name('android.widget.EditText')
        views[0].send_keys(Common(self.driver).getVercode(GVariable.teleNum)[-6:])
        views[1].send_keys('a1234567')
        #self.driver.hide_keyboard()
        self.driver.find_element_by_name('确认提现').click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'恭喜您,提现申请成功')))
        
        
        
    def test_accountInfo(self):
        text=self.driver.find_elements_by_class_name('android.widget.TextView')
        CMethod().assertText(text[4].text,"铜牌会员")
        CMethod().assertText(text[6].text,"已实名")
        CMethod().assertText(text[8].text,"已认证")
        CMethod().assertText(text[10].text,"已认证")
        CMethod().assertText(text[12].text,"已设置")
        CMethod().assertText(text[14].text,"修改/找回")
        
    def test_changePassword(self):
        views=self.driver.find_elements_by_class_name('android.widget.EditText')
        views[0].send_keys('a1234567')
        views[1].send_keys(Common(self.driver).getVercode(GVariable.teleNum)[0:6])
        views[2].send_keys('a12345678')
        views[3].send_keys('a12345678')
        self.driver.find_element_by_name('完成').click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'账户信息')))
        
    def test_findPassword(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME,'找回交易密码')))
        self.driver.find_element_by_name("请输入验证码").send_keys(Common(self.driver).getVercode(GVariable.teleNum)[0:6])
        self.driver.find_element_by_name("请输入您的身份证号").send_keys(Db('af88').sql('SELECT idNO FROM t_person WHERE cellPhone='+GVariable.teleNum).encode('UTF-8'))
        self.driver.find_element_by_name('下一步').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME,'设置新交易密码')))
        views=self.driver.find_elements_by_class_name('android.widget.EditText')
        views[0].send_keys('a1234567')
        views[1].send_keys('a1234567')
        self.driver.find_element_by_name('确定').click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.NAME,'账户信息')))
        
        
    def test_verifyPass(self,password):
        views=self.driver.find_elements_by_class_name('android.widget.EditText')
        views[1].send_keys(password)
        self.driver.find_element_by_name('验证').click()
        
        
    def test_addGoldNote(self):
        data=xlrd.open_workbook('D:\\appium\\GoldNote.xls')
        table=data.sheets()[0]
        activatronCode=table.row_values(random.randint(1,100))
        self.driver.find_element_by_name('请输入激活码').send_keys(activatronCode)
        self.driver.find_element_by_name('确定').click()
        
    def test_account(self):
        value_amount=self.driver.find_element_by_id('com.xiaoniu.finance:id/total_amount').text.replace(',','')
        value_earnings=self.driver.find_element_by_id('com.xiaoniu.finance:id/account_accumulate_earnings').text.replace(',','')
        value_availble=self.driver.find_element_by_id('com.xiaoniu.finance:id/availble_value').text.replace(',','')
        respon=Request().getData(GVariable.httpUrl+'my/account/details.json')
        Request().assertResult(respon['totalAssets'],value_amount)
        Request().assertResult(respon['totalEarningsAmount'],value_earnings)
        Request().assertResult(respon['availableBalance'],value_availble)
        
        
    def test_checkMoney(self):
        value_total_money=self.driver.find_element_by_id('com.xiaoniu.finance:id/AAIF_Tv_Total').text.replace(',','')
        value_available=self.driver.find_element_by_id('com.xiaoniu.finance:id/amount_rl_available').text.replace(',','')
        value_frozen=self.driver.find_element_by_id('com.xiaoniu.finance:id/amount_rl_frozen').text.replace(',','')
        value_principal=self.driver.find_element_by_id('com.xiaoniu.finance:id/amount_rl_principal').text.replace(',','')
        value_profit=self.driver.find_element_by_id('com.xiaoniu.finance:id/amount_rl_profit').text.replace(',','')
        value_hqn=self.driver.find_element_by_id('com.xiaoniu.finance:id/amount_rl_hqn').text.replace(',','')
        respon=Request().getData(GVariable.httpUrl+'my/assets.json')
        Request().assertResult(respon['totalAssets'],value_total_money)
        Request().assertResult(respon['availableBalance'],value_available)
        Request().assertResult(respon['freezedAmount'],value_frozen)
        Request().assertResult(respon['collectionPrincipalAmount'],value_principal)
        Request().assertResult(respon['collectionEarningsAmount'],value_profit)
        Request().assertResult(respon['currentInvestAmount'],value_hqn)
        
    def test_checkMoneyRecord(self):
        self.driver.implicitly_wait(2)
        value=[]
        value_fund_change=self.driver.find_elements_by_id('com.xiaoniu.finance:id/item_fund_change')
        for i in range(5):
            changeValue=value_fund_change[i].text.replace(',','')
            value.append(changeValue)
        respon=Request().getList(GVariable.httpUrl+'my/funds/200/detail.json?month=0&pageSize=20&year=0&type=all&pageNum=1')
        for i in range(5):
            Request().assertResult(respon[i]['operateAmount'],value[0])
            
            
    def test_checkIncome(self):
        value_total_in_money=self.driver.find_element_by_id('com.xiaoniu.finance:id/AAIF_Tv_Total').text.replace(',','')
        value_income_receive=self.driver.find_element_by_id('com.xiaoniu.finance:id/amount_rl_income_receive').text.replace(',','')
        value_income_will=self.driver.find_element_by_id('com.xiaoniu.finance:id/amount_rl_income_will').text.replace(',','')
        value_income_friend=self.driver.find_element_by_id('com.xiaoniu.finance:id/amount_rl_income_friend').text.replace(',','')
        value_income_game=self.driver.find_element_by_id('com.xiaoniu.finance:id/amount_rl_income_game').text.replace(',','')
        respon=Request().getData(GVariable.httpUrl+'my/assets.json')
        Request().assertResult(respon['totalEarningsAmount'],value_total_in_money)
        Request().assertResult(respon['dueEarningsAmount'],value_income_receive)
        Request().assertResult(respon['collectionEarningsAmount'],value_income_will)
        Request().assertResult(respon['fpEarningAmount'],value_income_friend)
        Request().assertResult(respon['actRewardsAmount'],value_income_game)
        
        
    
        

        
        
        
        
        
        
         
        
        
        
        
        
        
        
        
        


    
        
        
