import unittest
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class SH_04(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testSH_04(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.find_element_by_link_text('Shop').click()
        
        # Check Sort by Average ratings functionality
        driver.find_element_by_xpath('//*[@id="content"]/form/select/option[3]').click()
        current_url = driver.current_url
        self.assertEqual('http://practice.automationtesting.in/shop/?orderby=rating', current_url, "Fail to sort by average rating!")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()