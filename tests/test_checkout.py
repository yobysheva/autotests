import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@allure.feature("Модуль корзины и оформления заказа")
class TestCartCheckout:
    @pytest.fixture(autouse=True)
    def setup_steps(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        self.inventory_page = InventoryPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)

    @allure.story("7: Отображение товара в корзине")
    @allure.description("Проверка соответствия имени добавленного товара внутри корзины")
    def test_case_7_item_displayed_in_cart(self, driver):
        self.inventory_page.add_backpack_to_cart()
        self.inventory_page.click_cart()
        assert self.cart_page.get_item_name() == "Sauce Labs Backpack"

    @allure.story("8: Удаление товара внутри корзины")
    @allure.description("Проверка полного удаления товара по кнопке Remove из корзины")
    def test_case_8_remove_item_inside_cart(self, driver):
        self.inventory_page.add_backpack_to_cart()
        self.inventory_page.click_cart()
        self.cart_page.remove_item()
        assert self.cart_page.is_cart_empty() is True

    @allure.story("9: Успешный заказ (Checkout)")
    @allure.description("Сквозной сценарий успешной покупки товара до экрана Thank You")
    def test_case_9_successful_checkout(self, driver):
        self.inventory_page.add_backpack_to_cart()
        self.inventory_page.click_cart()
        self.cart_page.click_checkout()
        self.checkout_page.fill_shipping_info("Юлия", "Бобышева", "690000")
        self.checkout_page.finish_checkout()
        assert "Thank you for your order" in self.checkout_page.get_complete_header_text()

    @allure.story("10: Валидация пустой формы заказа")
    @allure.description("Проверка падения оформления заказа при незаполненных полях доставки")
    def test_case_10_checkout_validation_error(self, driver):
        self.inventory_page.add_backpack_to_cart()
        self.inventory_page.click_cart()
        self.cart_page.click_checkout()
        self.checkout_page.fill_shipping_info("", "", "")
        assert "First Name is required" in self.checkout_page.get_error_message()