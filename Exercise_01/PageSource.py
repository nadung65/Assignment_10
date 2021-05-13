import unittest
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class PageSource(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testPrintPageSource(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.set_window_size(1280, 720)
        page_source = driver.page_source
        print(page_source)

        # verify page source contain title tag
        self.assertTrue((page_source.find("<title>Automation Practice Site</title>") > -1) is True, "Can not get page source!");

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()