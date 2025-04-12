from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_text():
    driver = webdriver.Chrome()
    driver.get("https://navoergonomics.com/")
    driver.maximize_window()
    time.sleep(10)


    try:
        popup = driver.find_element(By.XPATH, "//span[@class='close-btn']")
        popup.click()
        time.sleep(2)
        print("✅ Popup closed")
    except:
        print("⚠️ Popup not found")


    driver.execute_script("window.scrollBy(0, 3000)")
    time.sleep(3)


    expected_data = {
        "High-Quality Materials:": "Our office furniture is made from premium materials, ensuring durability and longevity.",
        "Wide Range of Products:": "We have something for everyone, from modern office furniture to gaming chairs.",
        "Ergonomic Design:": "We prioritise your comfort and well-being with our ergonomically designed products."
    }


    for heading, expected_desc in expected_data.items():
        try:

            heading_element = driver.find_element(By.XPATH, f"//h6[normalize-space()='{heading}']")
            actual_heading = heading_element.text.strip()


            paragraph_element = heading_element.find_element(By.XPATH, "following::p[1]")
            actual_paragraph = paragraph_element.text.strip()

            print(f"\n Checking heading: {actual_heading}")
            assert actual_heading == heading, "Heading match nahi ho rahi bhai"
            assert actual_paragraph == expected_desc, "Paragraph match nahi ho raha bhai"
            print("Match hogaya bhai!")

        except Exception as e:
            print(f"Error in checking '{heading}': {e}")

    driver.quit()
