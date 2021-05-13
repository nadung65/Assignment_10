import unittest
import time
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class ML_02(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testML_02(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.find_element_by_link_text('My Account').click()
        
        # Log-in with incorrect username and password
        driver.find_element_by_id('username').send_keys('nadung')
        driver.find_element_by_id('password').send_keys('123456')
        driver.find_element_by_name('login').click()
        time.sleep(1)
        error = driver.find_element_by_class_name('woocommerce-error').text
        self.assertEqual('ERROR: Invalid username. Lost your password?', error, '\n=> Wrong error!')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()