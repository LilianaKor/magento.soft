from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    options = Options()
    options.headless = False  # Отключаем headless режим
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def custom_base_url():
    return "https://magento.softwaretestingboard.com"


@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, timeout=10)


@pytest.fixture
def faker_data(faker):
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "password": "TestPassword123!"
    }
