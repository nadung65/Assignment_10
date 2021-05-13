import unittest
import time
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class HP_18(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testHP_18(self):
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

        # Test Add To Basket button
        driver.find_element_by_class_name('single_add_to_cart_button').click()
        time.sleep(1)
        page_source = driver.page_source
        self.assertIn('<div class="woocommerce-message">', page_source, "Fail to click Add To Basket button!")

        # Check whether subtotal is less than total
        driver.find_element_by_css_selector('.woocommerce-message a').click()
        subtotal = float(driver.find_element_by_css_selector('.cart-subtotal td span').text[1:])
        total = float(driver.find_element_by_css_selector('.order-total td span').text[1:])
        self.assertTrue(subtotal < total, "Subtotal is not less than total!")

        # Test Check out function
        driver.find_element_by_class_name('checkout-button').click()
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
        driver.find_element_by_id('place_order').click()
        time.sleep(3)
        message = driver.find_element_by_class_name('woocommerce-thankyou-order-received').text
        self.assertEqual('Thank you. Your order has been received.', message, "Fail to check out!")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()