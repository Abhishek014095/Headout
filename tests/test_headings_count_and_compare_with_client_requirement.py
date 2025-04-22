import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pytest


def test_text_from_city_cards():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.headout.com/cities/")
    driver.maximize_window()
    time.sleep(2)

    url = "//div[@class='style__StyledResponsiveGrid-sc-1jae2s0-4 hfkrit cities-list-v2-scroll-wrapper']//div//div//div//div//div//div"
    items = driver.find_elements(By.XPATH, url)

    count = 1
    all_texts = []

    for item in items:
        text = item.text.strip()
        if text:
            line = f"{count}. {text}"
            print(line)
            all_texts.append(line + "\n\n")  # extra line spacing
            count += 1

    # Save to text file
    with open("city_texts.txt", "w", encoding="utf-8") as f:
        f.writelines(all_texts)

    print(f"\nTotal text blocks saved: {count - 1}")
    driver.quit()





# comapriosion line with client requirements 



def compare_text_files(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        file1_lines = [line.strip() for line in file1 if line.strip()]
        file2_lines = [line.strip() for line in file2 if line.strip()]

    total_lines = max(len(file1_lines), len(file2_lines))
    mismatches = []

    for i in range(total_lines):
        line1 = file1_lines[i] if i < len(file1_lines) else "<Missing>"
        line2 = file2_lines[i] if i < len(file2_lines) else "<Missing>"

        if line1 != line2:
            mismatches.append((i + 1, line1, line2))

    return mismatches


@pytest.mark.parametrize("file1, file2", [
    (r"D:\GitHub\Headout\tests\city_texts.txt", r"D:\GitHub\Headout\tests\client_text.txt")
])
def test_text_file_comparison(file1, file2):
    mismatches = compare_text_files(file1, file2)

    if mismatches:
        print("\n🔍 Comparison Report:")
        for line_no, actual, expected in mismatches:
            print(f"❌ Line {line_no} mismatch:\n   Expected: {expected}\n   Actual  : {actual}")
        pytest.fail(f"\n❗ Total mismatches found: {len(mismatches)}")
    else:
        print("\n✅ All lines match perfectly!")
