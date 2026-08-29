from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Локаторы для страницы авторизации (https://www.saucedemo.com/)."""

    username_input = (By.ID, "user-name")  # Поле ввода имени пользователя
    password_input = (By.ID, "password")   # Поле ввода пароля
    login_button = (By.ID, "login-button") # Кнопка входа
    error_message = (By.CSS_SELECTOR, "[data-test='error']")  # Сообщение об ошибке
