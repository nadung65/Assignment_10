import unittest
import time
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class HP_03(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testHP_03(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.find_element_by_link_text('Shop').click()
        driver.find_element_by_link_text('Home').click()

        # Test whether the Home page has Three Arrivals only
        arrivals = driver.find_elements_by_class_name('products')
        self.assertTrue((len(arrivals) == 3), "Home page has more than three arrivals!")

        # Test whether image is clickable and navigates to next page where user can add that book to his basket
        driver.find_element_by_css_selector('.woocommerce-LoopProduct-link img').click()
        time.sleep(1)
        current_url = str(driver.current_url)
        self.assertTrue(current_url.startswith("http://practice.automationtesting.in/product/"), "Can not click the arrivals!")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()