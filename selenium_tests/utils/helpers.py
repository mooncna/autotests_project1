from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium_tests.locators.cart_locators import CartPageLocators
from selenium_tests.locators.checkout_locators import CheckoutPageLocators
from selenium_tests.locators.inventory_locators import InventoryPageLocators


def get_cart_badge_count(driver) -> int:
    """Число на значке корзины. 0, если значок не отображается (корзина пуста)."""
    badges = driver.find_elements(*InventoryPageLocators.cart_badge)
    if not badges:
        return 0
    return int(badges[0].text)


def open_cart(driver):
    """Открывает корзину и дожидается загрузки страницы."""
    driver.find_element(*InventoryPageLocators.cart_link).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(CartPageLocators.page_title)
    )


def remove_all_items_from_cart(driver):
    """Удаляет все товары, находясь на странице корзины."""
    remove_buttons = driver.find_elements(*CartPageLocators.remove_buttons)
    for _ in range(len(remove_buttons)):
        driver.find_elements(*CartPageLocators.remove_buttons)[0].click()


def clear_cart_before_test(driver):
    """Гарантирует, что тест стартует с пустой корзиной, независимо от состояния до него."""
    if get_cart_badge_count(driver) > 0:
        open_cart(driver)
        remove_all_items_from_cart(driver)
        driver.find_element(*CartPageLocators.continue_shopping_button).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(InventoryPageLocators.page_title)
        )


def fill_checkout_form(driver, first_name: str, last_name: str, postal_code: str):
    """Заполняет форму на шаге один."""
    driver.find_element(*CheckoutPageLocators.first_name_input).send_keys(first_name)
    driver.find_element(*CheckoutPageLocators.last_name_input).send_keys(last_name)
    driver.find_element(*CheckoutPageLocators.postal_code_input).send_keys(postal_code)
