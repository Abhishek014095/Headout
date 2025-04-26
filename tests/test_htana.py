import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# //div[@class='style__UniversalSearchResultsDropdown-sc-1dyds4x-2 dhGLKe']//div[2]//a[1]//div[2]//span[2]


def test_tesxtt():

    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.headout.com/")
    driver.maximize_window()

    try:
        pop_up=driver.find_element(By.XPATH,"//*[name()='path' and contains(@d,'M13.333 2.')]")
        pop_up.click()
        time.sleep(3)

    except Exception as f:
        print(f"popup not found")


    driver.find_element(By.XPATH,"//input[@id='universal-search-input']").click()
    time.sleep(2)

    cities=driver.find_elements(By.XPATH,"//span[@class='notranslate search-result-name']")
    categories=driver.find_elements(By.XPATH,"//div[@class='searchResults__ResultsItem-sc-1a4zqdo-1 ABoWu']//div//span[2]")
    citi_list=[]
    categories_list=[]
    for citi in cities:
        citi_list.append(citi.text)

    for categori in categories:
        categories_list.append(categori.text)


    assert citi_list[2]=="Chiang Mai","not matching"
    assert categories_list[2]=="Thailand","not matching with the cities"

print("Done")