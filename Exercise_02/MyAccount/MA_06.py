import unittest
import time
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class MA_06(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testMA_06(self):
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
        driver.find_element_by_link_text('My Account').click()

        # Edit Shipping Address
        driver.find_element_by_link_text('Addresses').click()
        driver.find_element_by_xpath('//*[@id="page-36"]/div/div[1]/div/div/div[2]/header/a').click()
        driver.find_element_by_id('shipping_first_name').send_keys('AD')
        driver.find_element_by_id('shipping_last_name').send_keys('Nguyen')
        driver.find_element_by_id('select2-chosen-1').click()
        driver.find_element_by_id('s2id_autogen1_search').send_keys('Vietnam')
        driver.find_element_by_class_name('select2-match').click()
        driver.find_element_by_id('shipping_address_1').send_keys('Nam Ky Khoi Nghia')
        driver.find_element_by_id('shipping_city').send_keys('Danang')
        driver.find_element_by_name('save_address').click()
        time.sleep(1)
        current_url = driver.current_url
        self.assertEqual('http://practice.automationtesting.in/my-account/', current_url, 'Fail to edit shipping address!')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()