import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from utilities.BaseClass import BaseClass

# @pytest.mark.usefixtures("setup")-we can use it too if we are not using inheritance method -importing class from base class
class Testone(BaseClass):
    def test_e2e(self , setup):


        try:
            self.driver.execute_script("window.scrollBy(0, 500);")
            # self.driver.execute_script("window.scrollBy(0,100)")
            time.sleep(2)
            self.driver.find_element(By.XPATH,"//span[contains(text(),'Check availability')]").click()
            time.sleep(2)
        except Exception as e:
            print(f"this is an error {e}")

        Dates=self.driver.find_elements(By.XPATH,"(//div[@class='regularCalendar__CalendarBody-sc-144qu92-5 iZsZLv'])[1]//div//div")
        print(len(Dates))

        for Date in Dates:
            aria_label = Date.get_attribute("aria-label")
            if aria_label=="10":
                print("Date 10 found ,clicking....")
                Date.click()
                time.sleep(4)
                break
        print("after run")

