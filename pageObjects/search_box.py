from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Search:
    def __init__(self, driver):
        self.driver = driver
        # self.search_box = (By.XPATH, "//input[@id='universal-search-input']")

    def click(self):
        # self.driver.find_element(*self.search_box).click()
        self.driver.find_element(By.XPATH,"//input[@id='universal-search-input']")

    def enter_text(self, text):
        # self.driver.find_element(*self.search_box).send_keys(text)
        self.driver.find_element(By.XPATH,"//input[@id='universal-search-input']").send_keys(text)

    def press_enter(self):
        # self.driver.find_element(*self.search_box).send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH,"//input[@id='universal-search-input']").send_keys(Keys.ENTER)
