from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

from selenium_tests.locators.inventory_locators import InventoryPageLocators
from selenium_tests.locators.login_locators import LoginPageLocators

BASE_URL = "https://www.saucedemo.com/"
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


@pytest.fixture
def driver():
    """Создаёт и настраивает Chrome WebDriver на время одного теста, открывает saucedemo.com."""
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service, options=options)
    chrome_driver.get(BASE_URL)

    yield chrome_driver

    chrome_driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    """Возвращает WebDriver, уже авторизованный валидным пользователем standard_user."""
    driver.find_element(*LoginPageLocators.username_input).send_keys(VALID_USERNAME)
    driver.find_element(*LoginPageLocators.password_input).send_keys(VALID_PASSWORD)
    driver.find_element(*LoginPageLocators.login_button).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(InventoryPageLocators.inventory_list)
    )
    return driver
