import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_outh_positive(browser, custom_base_url, wait, faker_data):
    browser.get(f"{custom_base_url}/customer/account/create")

    browser.find_element(By.XPATH, "//input[@id='firstname']").send_keys(faker_data['first_name'])
    browser.find_element(By.XPATH, "//input[@id='lastname']").send_keys(faker_data['last_name'])
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email_address")))
    email_field.send_keys(faker_data['email'])
    browser.find_element(By.XPATH, "//*[@id='password']").send_keys(faker_data['password'])
    browser.find_element(By.XPATH, "//*[@id='password-confirmation']").send_keys(faker_data['password'])
    browser.find_element(By.XPATH, "//button[@title='Create an Account']").click()
    browser.save_screenshot("screenshot.png")
    # Ждём редиректа в личный кабинет
    wait.until(EC.url_contains("/customer/account"))

    assert "/customer/account" in browser.current_url, "URL is not correct"
