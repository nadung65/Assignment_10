import unittest
import time
import datetime
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class WebForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testSubmitWebForm(self):
        driver = self.driver
        driver.get('https://itmscoaching.herokuapp.com/form')
        driver.find_element_by_id('first-name').send_keys('Binh')
        driver.find_element_by_id('last-name').send_keys('Nguyen')
        driver.find_element_by_id('job-title').send_keys('Tester')
        driver.find_element_by_id('radio-button-3').click()
        driver.find_element_by_id('checkbox-2').click()
        driver.find_element_by_xpath('//*[@id="select-menu"]/option[4]').click()
        driver.find_element_by_id('datepicker').click()
        driver.find_element_by_class_name('datepicker-switch').click()
        prev_button = driver.find_element_by_css_selector('.datepicker-months .prev')
        next_button = driver.find_element_by_css_selector('.datepicker-months .next')
        current_year = int(datetime.datetime.now().year)
        selected_year = 2011
        if (current_year > selected_year):
            for i in range (0, current_year - selected_year):
                prev_button.click()
                time.sleep(0.2)
        else:
            for i in range (0, selected_year - current_year):
                next_button.click()
                time.sleep(0.2)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/table/tbody/tr/td/span[7]').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/table/tbody/tr[4]/td[4]').click()
        driver.find_element_by_link_text('Submit').click()
        time.sleep(1)

        # verify submit form success
        message = driver.find_element_by_class_name('alert-success').text
        self.assertEqual("The form was successfully submitted!", message, "Fail to submit form!");

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()