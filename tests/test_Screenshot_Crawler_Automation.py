import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




# Folder jisme screenshot save honge

def test_screenshots_crawler():
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.headout.com")  # Starting URL

    time.sleep(2)
    links = driver.find_elements(By.TAG_NAME, "a")
    urls = []

    for link in links:
        href = link.get_attribute("href")
        if href and href.startswith("http"):
            urls.append(href)


    urls = list(set(urls))

    print(f"Total URLs found: {len(urls)}")


    for idx, url in enumerate(urls):
        try:
            driver.get(url)
            time.sleep(2)
            driver.save_screenshot(f"screenshots/page_{idx+1}.png")
            print(f"Screenshot saved for {url}")
        except Exception as e:
            print(f"Error visiting {url}: {e}")

    driver.quit()
