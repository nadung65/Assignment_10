import unittest
from selenium import webdriver

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

class PageTitle(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def testPrintPageTitle(self):
        driver = self.driver
        driver.get('http://practice.automationtesting.in/')
        driver.maximize_window()
        title = driver.title
        print(title)

        # verify title
        self.assertEqual("Automation Practice Site", title, "Page title is not correct!")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()