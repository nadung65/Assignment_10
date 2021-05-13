import unittest
import time
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class SH_10(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testSH_10(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.find_element_by_link_text('Shop').click()

        # Check Add to cart button
        driver.find_element_by_class_name('add_to_cart_button').click()
        time.sleep(1)
        cart_content = driver.find_element_by_xpath('//*[@id="wpmenucartli"]/a/span[1]').text
        self.assertEqual('1 Item', cart_content, 'User can not view that book in menu!')
        
        # Test clicking View Basket link
        driver.find_element_by_link_text('View Basket').click()
        current_url = driver.current_url
        self.assertEqual('http://practice.automationtesting.in/basket/', current_url, 'Can not click View basket link!')
        time.sleep(1)

        # Check if subtotal < total
        subtotal = float(driver.find_element_by_css_selector('.cart-subtotal td span').text[1:])
        total = float(driver.find_element_by_css_selector('.order-total td span').text[1:])
        self.assertTrue(subtotal < total, "Subtotal is not less than total!")
    
        # Test Check out button
        driver.find_element_by_class_name('checkout-button').click()
        current_url = driver.current_url
        self.assertEqual('http://practice.automationtesting.in/checkout/', current_url, "Can not navigate to check out page!")
        
        # Fill details in check out page
        driver.find_element_by_id('billing_first_name').send_keys('AD')
        driver.find_element_by_id('billing_last_name').send_keys('Nguyen')
        driver.find_element_by_id('billing_email').send_keys('nadung@gmail.com')
        driver.find_element_by_id('billing_phone').send_keys('0123456789')
        driver.find_element_by_id('select2-chosen-1').click()
        driver.find_element_by_id('s2id_autogen1_search').send_keys('Vietnam')
        driver.find_element_by_class_name('select2-match').click()
        driver.find_element_by_id('billing_address_1').send_keys('Nam Ky Khoi Nghia')
        driver.find_element_by_id('billing_city').send_keys('Danang')
        driver.find_element_by_id('payment_method_cod').click()

        # Test Place order button
        driver.find_element_by_id('place_order').click()
        time.sleep(3)
        message = driver.find_element_by_class_name('woocommerce-thankyou-order-received').text
        self.assertEqual('Thank you. Your order has been received.', message, "Fail to check out!")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()