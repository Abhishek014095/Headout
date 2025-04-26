import time
import requests
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_broken_links():
    # Output file redirect
    original_stdout = sys.stdout
    with open('broken_links_report.txt', 'w', encoding='utf-8') as f:
        sys.stdout = f

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.headout.com/")

        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"Total links found: {len(links)}")

        broken_links = []

        for link in links:
            url = link.get_attribute("href")
            if url is None or not url.startswith("http"):
                continue
            try:
                response = requests.head(url, timeout=5)
                if response.status_code >= 400:
                    print(f"[BROKEN] {url} - Status: {response.status_code}")
                    broken_links.append((url, response.status_code))
                else:
                    print(f"[OK] {url}")
            except Exception as e:
                print(f"[ERROR] {url} - {e}")
                broken_links.append((url, "Exception"))

        driver.quit()

        print("\n📄 Broken Links Report:")
        for link, status in broken_links:
            print(f"❌ {link} - {status}")

        # Restore original stdout
        sys.stdout = original_stdout
