import unittest
from unittest.main import main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Test Loader - Class
#Test Case - Class with test handlers - writing building blocks of cases
#Test Suite - Container/Group
#Test Runner - Runnable interface 
#Test Report - Test results organized

#Automate a Scenario using a Test Case Class
#Arrange - Act - Assert

class ChromeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.implicitly_wait(10)

    def test_search_in_python_org_site(self):
        driver = self.driver
        driver.get("https://www.python.org/")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("getting started with python")
        elem.send_keys(Keys.RETURN)
        assert "https://www.python.org/search/?q=getting+started+with+python&submit=" == driver.current_url
    
    def test_load_amazon_site(self):
        driver = self.driver
        driver.get("https://www.amazon.ca/") 
        self.assertIn("Amazon", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()