import unittest
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class CurrentURL(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testPrintCurrentURL(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.set_window_size(1280, 720)
        current_url = driver.current_url
        print(current_url)

        # verify current url
        self.assertEqual("http://practice.automationtesting.in/", current_url, "Current URL is not correct")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()