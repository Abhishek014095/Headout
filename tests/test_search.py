import time

import pytest
from utilities.BaseClass import BaseClass
from pageObjects.search_box import Search

@pytest.mark.usefixtures("setup")
class TestSearch(BaseClass):
    def test_search_box(self):
        search = Search(self.driver)

        search.click()
        time.sleep(1)
        # self.wait_for_seconds(1)

        search.enter_text("dubai")
        time.sleep(1)
        # self.wait_for_seconds(1)

        search.press_enter()
        time.sleep(4)
        # self.wait_for_seconds(4)

        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)
        # self.wait_for_seconds(2)

        self.driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(3)
        # self.wait_for_seconds(3)
