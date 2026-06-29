import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@allure.feature("Модуль каталога товаров")
class TestCatalog:
    @pytest.fixture(autouse=True)
    def setup_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        self.inventory_page = InventoryPage(driver)

    @allure.story("4: Добавление товара из каталога")
    @allure.description("Проверка изменения счетчика корзины при добавлении товара")
    def test_case_4_add_to_cart_from_inventory(self, driver):
        self.inventory_page.add_backpack_to_cart()
        assert self.inventory_page.get_cart_badge_text() == "1"

    @allure.story("5: Удаление товара из каталога")
    @allure.description("Проверка уменьшения счетчика корзины при удалении товара кнопкой из каталога")
    def test_case_5_remove_from_cart_from_inventory(self, driver):
        self.inventory_page.add_backpack_to_cart()
        self.inventory_page.remove_backpack_from_cart()
        assert self.inventory_page.get_cart_badge_text() == "0"

    @allure.story("6: Сортировка товаров по цене")
    @allure.description("Проверка фильтрации цен от низкой к высокой")
    def test_case_6_sort_products_by_price(self, driver):
        self.inventory_page.sort_products_by("lohi")
        prices = self.inventory_page.get_all_prices()
        assert prices == sorted(prices)