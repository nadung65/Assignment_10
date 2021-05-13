import unittest
import time
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class MR_03(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testMR_03(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.find_element_by_link_text('My Account').click()
        
        # Check register with empty email and valid password
        password_textbox = driver.find_element_by_id('reg_password')
        password = 'DungNA_65'
        for character in password:
            password_textbox.send_keys(character)
            time.sleep(0.5)
        driver.find_element_by_name('register').click()
        error = driver.find_element_by_class_name('woocommerce-error').text
        self.assertEqual('Error: Please provide a valid email address.', error, "Wrong error!")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()