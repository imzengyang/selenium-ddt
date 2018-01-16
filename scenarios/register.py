import unittest
import time
import os

from selenium import webdriver
from ddt import ddt, data, unpack


from library.getData import get_csv_data
from library.getScreenShot import getScreenShotsPath


@ddt
class Register(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.screenshotDir = getScreenShotsPath()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    @data(*get_csv_data('./data/scenario-register.csv'))
    @unpack
    def test_register(self, username, passwd, repasswd, email, assert_result):
        driver = self.driver
        driver.get('http://118.31.19.120:3000/')

        driver.find_element_by_css_selector('a[href="/signup"]').click()
        driver.find_element_by_id('loginname').send_keys(username)
        driver.find_element_by_id('pass').send_keys(passwd)
        driver.find_element_by_id('re_pass').send_keys(repasswd)
        driver.find_element_by_id('email').send_keys(email)

        driver.find_element_by_css_selector('.span-primary').click()

    def tearDown(self):
        filename = str(time.time()) +".png"
        self.driver.save_screenshot(os.path.join(self.screenshotDir,filename))

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
