from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium_tests.locators.cart_locators import CartPageLocators
from selenium_tests.locators.checkout_locators import CheckoutPageLocators
from selenium_tests.locators.inventory_locators import InventoryPageLocators
from selenium_tests.utils.helpers import (
    clear_cart_before_test,
    fill_checkout_form,
    get_cart_badge_count,
    open_cart,
)


def test_successful_purchase(logged_in_driver):
    """Сценарий 1: выбрать товар, оформить покупку и убедиться, что она завершилась успешно."""
    driver = logged_in_driver
    clear_cart_before_test(driver)

    add_buttons = driver.find_elements(*InventoryPageLocators.add_to_cart_buttons)
    add_buttons[0].click()
    WebDriverWait(driver, 5).until(lambda d: get_cart_badge_count(d) == 1)

    open_cart(driver)
    cart_items = driver.find_elements(*CartPageLocators.cart_item)
    assert len(cart_items) == 1, "Товар не попал в корзину"

    driver.find_element(*CartPageLocators.checkout_button).click()
    WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-one"))

    fill_checkout_form(driver, "Ivan", "Petrov", "123456")
    driver.find_element(*CheckoutPageLocators.continue_button).click()
    WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-two"))

    driver.find_element(*CheckoutPageLocators.finish_button).click()

    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(CheckoutPageLocators.complete_header)
    ).text
    assert success_message == "Thank you for your order!", "Покупка не завершилась ожидаемым сообщением об успехе"
    assert "checkout-complete" in driver.current_url
