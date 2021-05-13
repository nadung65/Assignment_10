import unittest
import time
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class ML_07(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testML_07(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.find_element_by_link_text('My Account').click()
        
        # Login with case changed
        username = 'abc65@gmail.com'.upper()
        password = 'DungNA_65'.upper()
        driver.find_element_by_id('username').send_keys(username.upper())
        driver.find_element_by_id('password').send_keys(password.upper())
        driver.find_element_by_name('login').click()
        time.sleep(1)
        error = driver.find_element_by_class_name('woocommerce-error').text
        self.assertEqual('ERROR: The password you entered for the username ' + username + ' is incorrect. Lost your password?', error)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()