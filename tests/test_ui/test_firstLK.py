import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# def test_negative_email_validation(driver):
#     browser.get(f"{custom_base_url}/customer/account/create")
#     browser.find_element('xpath', "//input[@id='firstname']").send_keys("Lady")
#     browser.find_element(By.XPATH, "//input[@id='lastname']").send_keys("GAGAha")
#     email_field = wait.until(EC.presence_of_element_located((By.ID, "email_address")))
    # Вводим некорректный email
    # driver.find_element(By.CSS_SELECTOR, Locators.EMAIL_FIELD).send_keys("invalid_email")
    # driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_FIELD).send_keys("Test12345!")
    # driver.find_element(By.CSS_SELECTOR, Locators.CONFIRM_PASSWORD_FIELD).send_keys("Test12345!")
    # driver.find_element(By.CSS_SELECTOR, Locators.CREATE_ACCOUNT_BTN).click()

    # Проверяем, что появилось сообщение об ошибке
    # error_message = driver.find_element(By.CSS_SELECTOR, Locators.ERROR_MESSAGE).text
    # assert "Please enter a valid email address" in error_message


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



