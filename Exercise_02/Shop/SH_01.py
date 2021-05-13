import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class SH_01(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testSH_01(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.find_element_by_link_text('Shop').click()
        
        # Check Filter by price functionality
        # Click and hold right slider to 450 (-23px)
        right_slider = driver.find_element_by_xpath('//*[@id="woocommerce_price_filter-2"]/form/div/div[1]/span[2]')
        move = ActionChains(driver)
        move.click_and_hold(right_slider).move_by_offset(-23, 0).release().perform()

        # Click on Filter button
        driver.find_element_by_css_selector('.price_slider_amount button').click()
        time.sleep(1)

        # Get all distinct price of products 
        products = driver.find_elements_by_css_selector('#content ul li .woocommerce-LoopProduct-link span span')
        product_with_del_price = driver.find_elements_by_css_selector('#content ul li .woocommerce-LoopProduct-link span del span')
        all_prices = [str(product.text)[1:] for product in products]
        del_prices = [str(product.text)[1:] for product in product_with_del_price]
        prices = []
        for price in all_prices:
            if price != '':
                if (price not in del_prices) | ((price in del_prices) & (all_prices.count(price) > del_prices.count(price))):
                    prices.append(price)
        prices = sorted(list(dict.fromkeys(prices)), key=float)

        # Check if price of filtered products are between 150 and 450 
        has_invalid_price = True
        if len(prices) > 0:
            min_price = float(prices[0])
            max_price = float(prices[len(prices) - 1])
            has_invalid_price = (min_price >= 150) & (max_price <= 450)
        self.assertTrue(has_invalid_price, "Fail to filter price!")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()