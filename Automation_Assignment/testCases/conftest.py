import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver


@pytest.fixture()
def setup(browser, headless_mode):
    if browser == "Chrome":
        browser_options = webdriver.ChromeOptions()
        browser_options.add_argument('--disable-cookies')
    else:
        browser_options = webdriver.FirefoxOptions()

    if headless_mode:
        browser_options.add_argument("--headless")

    driver = webdriver.Chrome(executable_path='C:/Users/xxpallep/Desktop/chromedriver.exe', options=browser_options)

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--browser', action="store", default="Chrome", help="Browser to run tests on (chrome/firefox)")
    parser.addoption('--headless', action="store_true", help="Run browser in headless mode")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def headless_mode(request):
    return request.config.getoption("--headless")
