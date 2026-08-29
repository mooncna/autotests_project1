from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium_tests.locators.login_locators import LoginPageLocators


def test_unsuccessful_login_with_invalid_credentials(driver):
    """Сценарий 3: неуспешная авторизация с неверными данными -> корректное сообщение об ошибке."""
    driver.find_element(*LoginPageLocators.username_input).send_keys("invalid_user")
    driver.find_element(*LoginPageLocators.password_input).send_keys("invalid_pass")
    driver.find_element(*LoginPageLocators.login_button).click()

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.error_message)
    )
    expected_text = "Epic sadface: Username and password do not match any user in this service"
    assert error.text == expected_text, (
        f"Текст ошибки не совпадает. Ожидалось: {expected_text!r}, получено: {error.text!r}"
    )
    assert "saucedemo.com" in driver.current_url, "пользователь покинул страницу авторизации"
