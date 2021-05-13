import unittest
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class ML_06(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testML_06(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.find_element_by_link_text('My Account').click()
        
        # Check whether password is visible
        password_input = driver.find_element_by_id('password')
        password_input.send_keys('DungNA_65')
        input_type = password_input.get_attribute('type')
        self.assertEqual('password', input_type, 'The password is visible!')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()