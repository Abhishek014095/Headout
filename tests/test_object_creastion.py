from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import IEDriverManager


def test_systemroles():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    driver.get("https://dealy.hipl-staging2.com")
    driver.maximize_window()

    # Login
    wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys("admin@gmail.com")
    driver.find_element(By.XPATH, "//input[@placeholder='*********']").send_keys("Admin@123")
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()

    wait.until(EC.visibility_of_element_located((By.ID, "otp"))).send_keys("111111")
    driver.find_element(By.XPATH, "//button[normalize-space()='Verify OTP']").click()

    wait.until(EC.element_to_be_clickable((By.XPATH, "//h6[normalize-space()='System Roles']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/admin/roles']"))).click()

    wait.until(EC.element_to_be_clickable((By.ID, "btnAddRole"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("Abhi")

    # Handle Select2 dropdown
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'select2-selection')]"))).click()
    permission_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[@id='select2-permissions-results']/li[1]")))
    permission_option.click()

    # Save the role
    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']")))
    save_button.click()

    # Confirmation popup
    popup_ok = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']")))
    driver.save_screenshot(r"D:\GitHub\Headout\screenshot\popup_full_page.png")

    popup_ok.click()

    print("✅ Role successfully created!")

    driver.quit()

