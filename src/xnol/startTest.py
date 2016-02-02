#coding=utf-8

import unittest
from account import Account
from init import Init
from appium import webdriver
import os
import time
import HTMLTestRunner
from common import Common
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import random
from gVariable import GVariable
from about import About
from product import Product



PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.4'
desired_caps['deviceName'] = 'YQ601'
'''
desired_caps['app'] = PATH(
    'C:\Users\Administrator\Desktop\XNOnline_1.0.19.apk'
)
'''

desired_caps['appPackage'] = 'com.xiaoniu.finance'

desired_caps['appActivity'] = '.ui.LaucherTaskActivity'
desired_caps['appWaitActivity']= '.ui.MainActivity'
desired_caps["unicodeKeyboard"] = "True"  
desired_caps["resetKeyboard"] = "True"  

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

class Xnol(unittest.TestCase):
    
    def setUp(self):
        #Common(driver).recover()
        print u"开始测试时间:"+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    def tearDown(self):
        #self.driver.quit()
        try:
            driver.get_screenshot_as_file('D:\\appium\\screenshots\\'+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))+'.png')
        except IOError:
            print u'截图失败'
        print u"完成测试时间:"+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        
        
    #注册
    def test_case001(self):
        #WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,'我的')))
        driver.find_element_by_name("我的").click()
        driver.find_element_by_name("立即登录  >").click()
        #driver.find_element_by_name("马上登录").click()
        Account(driver).test_register()
        
    #注册成功后开通认证支付（快钱支付）
    def test_case002(self):
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,'开通认证支付')))
        driver.find_element_by_name('开通认证支付').click()
        Account(driver).test_quickPay("农业银行")
        

    #开通认证支付后设置交易密码
    def test_case003(self):
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,'立即设置交易密码')))
        driver.find_element_by_name("立即设置交易密码").click()
        Account(driver).test_transPass()

    
    #充值
    def test_case004(self):
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,'立即充值')))
        driver.find_element_by_name('立即充值').click()
        Account(driver).test_recharge()
        
        
    #提现
    def test_case005(self):
        Common(driver).recover()
        driver.find_element_by_name('我的').click()
        driver.find_element_by_name('提现').click()
        Account(driver).test_withdraw()
        
        
    #注册并开通认证支付（易宝支付）
    def test_case006(self):
        Common(driver).recover()
        driver.find_element_by_name('我的').click()
        driver.find_element_by_name('小牛君').click()
        driver.implicitly_wait(1)
        driver.find_element_by_name('安全退出').click()
        GVariable.teleNum=str(int(GVariable.teleNum)+1)
        #driver.find_element_by_name("马上登录").click()
        Account(driver).test_register()
        Common(driver).recover()
        driver.find_element_by_name('我的').click()
        driver.find_element_by_name('铜牌会员').click()
        driver.find_element_by_name('银行卡认证').click()
        driver.find_element_by_name('立即开通').click()
        Account(driver).test_quickPay("邮储银行")

    #设置交易密码（需要验证码）
    def test_case007(self):
        Common(driver).recover()
        driver.find_element_by_name('我的').click()
        driver.find_element_by_name('小牛君').click()
        driver.find_element_by_name('交易密码').click()
        driver.find_element_by_name('获取验证码').click()
        #self.driver.implicitly_wait(3)
        WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.NAME,'语音验证码')))
        driver.find_element_by_name('请输入验证码').send_keys(Common(driver).getVercode(GVariable.teleNum))
        driver.find_element_by_name('下一步').click()
        Account(driver).test_transPass()
        
    #易宝支付充值
    def test_case008(self):
        Common(driver).recover()
        driver.find_element_by_name('我的').click()
        driver.find_element_by_name('充值').click()
        Account(driver).test_recharge()
        
    #易宝支付提现(需要设置支行信息)
    def test_case009(self):
        Common(driver).recover()
        driver.find_element_by_name('我的').click()
        driver.find_element_by_name('提现').click()
        driver.find_element_by_name('知道了').click()
        driver.find_element_by_name('请选择您的银行卡开户省份').click()
        driver.find_element_by_name('内蒙古').click()
        driver.find_element_by_name('呼和浩特').click()
        driver.find_element_by_name('中国邮政储蓄银行有限责任公司呼和浩特市文化宫街支行').click()
        driver.find_element_by_name('下一步').click()
        Account(driver).test_withdraw()
        
    #账户信息check
    def test_case010(self):
        Common(driver).recover()
        driver.find_element_by_name('我的').click()
        driver.find_element_by_name('邱君华').click()
        Account(driver).test_accountInfo()
        About(driver).test_openHtmlPage("会员等级", "会员等级规则")
        
    #修改手势密码
    def test_case011(self):
        Common(driver).recover()
        driver.find_element_by_name('我的').click()
        driver.find_element_by_name('邱君华').click()
        WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.NAME,'账户信息')))
        driver.find_element_by_name('修改手势密码').click()
        Account(driver).test_verifyPass('123456')
        WebDriverWait(driver,40).until(EC.visibility_of_element_located((By.NAME,'请绘制手势密码')))
        Common(driver).gesture()
        Common(driver).gesture()
        
    #check我的账户一级界面数据
    def test_case012(self):
        Common(driver).recover()
        driver.find_element_by_name('我的').click()
        Account(driver).test_account()
        
    #check我的资产
    def test_case013(self):
        Common(driver).recover()
        driver.find_element_by_name('我的').click()
        driver.find_element_by_name('总资产  (元)  >').click()
        Account(driver).test_checkMoney()
        
        
    #check资金记录
    def test_case014(self):
        driver.find_element_by_name('资金记录').click()
        Account(driver).test_checkMoneyRecord()
        
    
    #check我的收益
    def test_case015(self):
        Common(driver).recover()
        driver.find_element_by_name('我的').click()
        driver.find_element_by_name('累计收益  (元)  >').click()
        Account(driver).test_checkIncome()
        
        
    #购买天天牛
    def test_case016(self):
        Common(driver).recover()
        driver.find_element_by_name('我的').click()
        driver.find_element_by_name('我的天天牛').click()
        WebDriverWait(driver,40).until(EC.visibility_of_element_located((By.NAME,'购买')))
        driver.find_element_by_name('购买').click()
        Product(driver).test_buyDay('100')
        
    #提取天天牛
    def test_case017(self):
        Common(driver).recover()
        driver.find_element_by_name('我的').click()
        driver.find_element_by_name('我的天天牛').click()
        WebDriverWait(driver,40).until(EC.visibility_of_element_located((By.NAME,'提取')))
        driver.find_element_by_name('提取').click()
        Product(driver).test_withdrawDay('10','123456')
        
    #添加理财金券
    def test_case018(self):
        Common(driver).recover()
        driver.find_element_by_name('我的').click()
        Common(driver).swipeUp(500)
        driver.find_element_by_name('红包优惠券').click()
        driver.find_element_by_name('理财金券').click()
        driver.find_element_by_name('添加理财金券').click()
        Account(driver).test_addGoldNote()
        
        
        
        
        
        
    
        
    
        
if __name__ == '__main__':
    driver.deactivate_ime_engine()
    suite = unittest.TestSuite()
    '''
    suite.addTest(Xnol('test_case001'))
    suite.addTest(Xnol('test_case002'))
    suite.addTest(Xnol('test_case003'))
    suite.addTest(Xnol('test_case004'))
    suite.addTest(Xnol('test_case005'))
    suite.addTest(Xnol('test_case006'))
    suite.addTest(Xnol('test_case007'))
    suite.addTest(Xnol('test_case008'))
    suite.addTest(Xnol('test_case009'))
    '''
    suite.addTest(Xnol('test_case010'))
    #suite.addTest(Xnol('test_case011'))
    #suite.addTest(Xnol('test_case012'))
    #suite.addTest(Xnol('test_case013'))
    #suite.addTest(Xnol('test_case014'))
    #suite.addTest(Xnol('test_case015'))
    #suite.addTest(Xnol('test_case016'))
    #suite.addTest(Xnol('test_case017'))
    #suite.addTest(Xnol('test_case018'))
    
    '''
    timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    filename = "D:\\appium\\appiumresult\\result_" + timestr + ".html"
    print (filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title=u'小牛在线 APP自动化测试报告 (Android)',
                description=u'【测试报告详情】：'
                )
    runner.run(suite)
    fp.close()
    '''
    #suite = unittest.TestLoader().loadTestsFromTestCase(Xnol)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    


    
    
    
    