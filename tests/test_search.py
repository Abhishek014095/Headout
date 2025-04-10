import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from utilities.BaseClass import BaseClass



class Testtwo(BaseClass):
    def test_search(self,setup):
        search_input=self.driver.find_element(By.XPATH,"//input[@id='universal-search-input']")
        search_input.click()
        time.sleep(1)
        search_input.send_keys("dubai")
        time.sleep(1)
        search_input.send_keys(Keys.ENTER)
        time.sleep(4)
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(500,1000)")
        time.sleep(3)
