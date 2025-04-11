# pageObjects/SearchBox.py
from selenium.webdriver.common.by import By

class date_e22e:

    def __init__(self, driver):
        self.driver = driver

    check_availability = (By.XPATH, "//span[contains(text(),'Check availability')]")
    dates = (By.XPATH, "(//div[@class='regularCalendar__CalendarBody-sc-144qu92-5 iZsZLv'])[1]//div//div")

    def click_check_availability(self):
        self.driver.find_element(*date_e22e.check_availability).click()

    def get_dates(self):
        return self.driver.find_elements(*date_e22e.dates)
