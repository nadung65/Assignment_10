import unittest
import time
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class ML_08(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testML_08(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.find_element_by_link_text('My Account').click()
        
        # Check if user can return to the account page after logging out 
        driver.find_element_by_id('username').send_keys('nadung.18it1@vku.udn.vn')
        driver.find_element_by_id('password').send_keys('Dungpro6599')
        driver.find_element_by_name('login').click()
        time.sleep(0.5)
        driver.find_element_by_link_text('Sign out').click()
        time.sleep(0.5)
        driver.back()
        page_source = driver.page_source
        self.assertNotIn('From your account dashboard you can view', page_source, 'User can return to the account page after logging out!')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()