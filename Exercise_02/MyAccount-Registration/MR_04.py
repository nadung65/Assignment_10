import unittest
import time
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class MR_04(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testMR_04(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.find_element_by_link_text('My Account').click()
        
        # Check register with valid email and valid password
        driver.find_element_by_id('reg_email').send_keys('adnguyen@gmail.com')
        driver.find_element_by_name('register').click()
        time.sleep(1)
        error = driver.find_element_by_class_name('woocommerce-error').text
        self.assertEqual('Error: Please enter an account password.', error)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()