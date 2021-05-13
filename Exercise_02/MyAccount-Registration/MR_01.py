import unittest
import time
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class MR_01(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testMR_01(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.find_element_by_link_text('My Account').click()
        
        # Check register with valid email and valid password
        driver.find_element_by_id('reg_email').send_keys('nad06051999@gmail.com')
        password_textbox = driver.find_element_by_id('reg_password')
        password = 'DungNA_65'
        for character in password:
            password_textbox.send_keys(character)
            time.sleep(0.5)
        driver.find_element_by_name('register').click()
        page_source = str(driver.page_source)
        email_already_exists = page_source.find('An account is already registered with your email address.') != -1
        register_success = page_source.find('From your account dashboard you can view') != -1
        self.assertTrue(email_already_exists | register_success, '\n\n=> Fail to register!')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()