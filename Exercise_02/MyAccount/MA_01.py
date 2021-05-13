import unittest
import time
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class MA_01(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testMA_01(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.find_element_by_link_text('My Account').click()
        
        # Log-in with valid username and valid password
        username = 'abc65'
        driver.find_element_by_id('username').send_keys(username + '@gmail.com')
        driver.find_element_by_id('password').send_keys('DungNA_65')
        driver.find_element_by_name('login').click()
        time.sleep(1)
        message = driver.find_element_by_xpath('//*[@id="page-36"]/div/div[1]/div/p[1]/strong').text
        self.assertEqual(username, message, "Fail to login!")

        # Check if click on Myaccount link which leads to Dashboard
        driver.find_element_by_link_text('My Account').click()
        self.assertEqual(username, message, "Fail to view Dashboard when click My Account link!")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()