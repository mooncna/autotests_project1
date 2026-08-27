from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Локаторы для страницы авторизации (https://www.saucedemo.com/)."""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
