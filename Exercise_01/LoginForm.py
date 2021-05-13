import unittest
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class LoginForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testLoginForm(self):
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com')
        driver.find_element_by_link_text('Form Authentication').click()
        driver.find_element_by_id('username').send_keys('tomsmith')
        driver.find_element_by_id('password').send_keys('SuperSecretPassword!')
        driver.find_element_by_tag_name('button').click()
        title = driver.title

        # verify login success
        self.assertEqual("The Internet", title, "Fail to login!");

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()