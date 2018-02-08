import unittest
import time
import os

from selenium import webdriver
from ddt import ddt, data, unpack


from library.getData import get_xls_data
from library.getScreenShot import getScreenShotsPath


@ddt
class Register(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.screenshotDir = getScreenShotsPath()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    # @data(*get_csv_data('./data/scenario-register.csv'))
    # @unpack
    # def test_register(self, username, passwd, repasswd, email, assert_result):
    #     driver = self.driver
    #     driver.get('http://118.31.19.120:3000/')

    #     driver.find_element_by_css_selector('a[href="/signup"]').click()
    #     driver.find_element_by_id('loginname').send_keys(username)
    #     driver.find_element_by_id('pass').send_keys(passwd)
    #     driver.find_element_by_id('re_pass').send_keys(repasswd)
    #     driver.find_element_by_id('email').send_keys(email)

    #     driver.find_element_by_css_selector('.span-primary').click()
    @data(*get_xls_data('./data/user.xls'))
    @unpack
    def test_login(self,username,passwd,status,excpetVal):
        dr = self.driver 
        dr.get("http://118.31.19.120:3000/")
        dr.find_element_by_css_selector('body > div.navbar > div > div > ul > li:nth-child(6) > a').click()
        dr.find_element_by_id('name').send_keys(username)
        dr.find_element_by_id('pass').send_keys(passwd)

        dr.find_element_by_css_selector(".span-primary").click()

        if status == "成功":
            successText = dr.find_element_by_css_selector('#sidebar > div:nth-child(1) > div.inner > div > div > span.user_name > a').text
            self.assertEqual(successText,excpetVal)
        else:
            faildeText = dr.find_element_by_css_selector('#content > div > div.inner > div > strong').text
            self.assertEqual(faildeText,excpetVal)

    def tearDown(self):
        # 2018-02-08_09_20_30.png
        filename = str(time.strftime('%Y-%m-%d_%H_%M_%S')) +".png"
        self.driver.save_screenshot(os.path.join(self.screenshotDir,filename))

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
