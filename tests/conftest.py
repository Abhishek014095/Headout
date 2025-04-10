import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--execution", action="store", default="local")  # local or remote


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    execution_type = request.config.getoption("execution")

    driver = None  # define kr diya safe side ke liye

    if execution_type == "remote":
        # SauceLabs Credentials
        sauce_username = 'oauth-abhisheksharma.hipl-ed503'
        sauce_access_key = '544b3b3e-2935-4fed-9821-f1cdf4f97b79'
        sauce_url = f"https://{sauce_username}:{sauce_access_key}@ondemand.eu-central-1.saucelabs.com:443/wd/hub"

        sauce_options = {
            'username': sauce_username,
            'accessKey': sauce_access_key,
            'build': 'Headout-Automation-Build',
            'name': request.node.name  # test ka name dynamically
        }

        if browser_name == "chrome":
            options = ChromeOptions()
            options.browser_version = 'latest'
            options.platform_name = 'Windows 11'
            options.set_capability('sauce:options', sauce_options)

        elif browser_name == "firefox":
            options = FirefoxOptions()
            options.browser_version = 'latest'
            options.platform_name = 'Windows 11'
            options.set_capability('sauce:options', sauce_options)

        driver = webdriver.Remote(command_executor=sauce_url, options=options)

    else:
        # Local Execution
        if browser_name == "chrome":
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        elif browser_name == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    # Common Steps
    driver.get("https://www.headout.com/sun-world-ba-na-hills-tickets/sun-world-ba-na-hills-tickets-with-indian-buffet-lunch-e-30778/")
    driver.maximize_window()
    time.sleep(2)

    request.cls.driver = driver
    yield
    driver.quit()
