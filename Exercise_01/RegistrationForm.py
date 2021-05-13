import unittest
import time
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class RegistrationForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testRegistrationForm(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.find_element_by_link_text('My Account').click()
        driver.find_element_by_id('reg_email').send_keys('nadung.18it1@vku.udn.vn')
        password_textbox = driver.find_element_by_id('reg_password')
        password = 'DungNA_65'
        for character in password:
            password_textbox.send_keys(character)
            time.sleep(0.5)
        driver.find_element_by_name('register').click()

        # verify that account is already registered or not
        page_source = driver.page_source
        self.assertIn("An account is already registered with your email address.", page_source, "\n\n=> Account have been created successfully!");

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()