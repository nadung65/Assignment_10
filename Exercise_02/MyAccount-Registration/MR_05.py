import unittest
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class MR_05(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testMR_05(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.find_element_by_link_text('My Account').click()
        
        # Check register with empty email and empty password
        driver.find_element_by_name('register').click()
        error = driver.find_element_by_class_name('woocommerce-error').text
        self.assertEqual('Error: Please provide a valid email address.', error, "Wrong error!")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()