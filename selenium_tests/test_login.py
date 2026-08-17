from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium_tests.fixtures.browser_fixtures import driver
from selenium_tests.locators.login_locators import LoginPageLocators


def test_login_success(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(*LoginPageLocators.USERNAME).send_keys("standard_user")
    driver.find_element(*LoginPageLocators.PASSWORD).send_keys("secret_sauce")
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_list"))
    )
    assert "inventory" in driver.current_url


def test_login_error(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(*LoginPageLocators.USERNAME).send_keys("locked_out_user")
    driver.find_element(*LoginPageLocators.PASSWORD).send_keys("secret_sauce")
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE)
    )
    assert "Epic sadface" in error.text