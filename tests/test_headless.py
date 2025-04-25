from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True  # Enable headless mode


def test_headless():
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.example.com')
    print(driver.title)
    driver.quit()
