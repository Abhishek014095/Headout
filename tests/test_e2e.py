# test_e2e.py
import pytest
import time
from utilities.BaseClass import BaseClass
from pageObjects.date_e2e import date_e22e

class Testone(BaseClass):

    def test_e2e(self, setup):

        search = date_e22e(self.driver)

        try:
            self.driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(2)
            search.click_check_availability()
            time.sleep(2)
        except Exception as e:
            print(f"this is an error {e}")

        Dates = search.get_dates()
        print(len(Dates))

        for Date in Dates:
            aria_label = Date.get_attribute("aria-label")
            if aria_label == "11":
                print("Date 11 found, clicking....")
                Date.click()
                time.sleep(4)
                break

        print("after run")
