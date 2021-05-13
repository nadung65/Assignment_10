import unittest
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class SH_07(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testSH_07(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.find_element_by_link_text('Shop').click()
        
        # Check Sort by High to Low functionality
        driver.find_element_by_xpath('//*[@id="content"]/form/select/option[6]').click()
        current_url = driver.current_url
        self.assertEqual('http://practice.automationtesting.in/shop/?orderby=price-desc', current_url, "Fail to sort by high to low!")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()