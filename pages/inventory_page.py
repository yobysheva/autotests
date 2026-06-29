from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
import allure

class InventoryPage(BasePage):
    ADD_BACKPACK_BTN = (By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK_BTN = (By.XPATH, "//button[@id='remove-sauce-labs-backpack']")
    CART_BADGE = (By.CSS_SELECTOR, "span.shopping_cart_badge")
    CART_LINK = (By.XPATH, "//a[@class='shopping_cart_link']")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "select.product_sort_container")
    ITEM_PRICES = (By.XPATH, "//div[@class='inventory_item_price']")

    @allure.step("Добавление рюкзака в корзину через каталог")
    def add_backpack_to_cart(self):
        self.click_to(self.ADD_BACKPACK_BTN)

    @allure.step("Удаление рюкзака из корзины через каталог")
    def remove_backpack_from_cart(self):
        self.click_to(self.REMOVE_BACKPACK_BTN)

    @allure.step("Получение счетчика товаров на иконке корзины")
    def get_cart_badge_text(self):
        try:
            return self.get_text(self.CART_BADGE, timeout=2)
        except:
            return "0"

    @allure.step("Клик по иконке корзины для перехода")
    def click_cart(self):
        self.click_to(self.CART_LINK)

    @allure.step("Сортировка товаров по значению: {value}")
    def sort_products_by(self, value):
        dropdown = self.find_element(self.SORT_DROPDOWN)
        select = Select(dropdown)
        select.select_by_value(value)

    @allure.step("Сбор всех цен товаров на странице")
    def get_all_prices(self):
        elements = self.find_elements(self.ITEM_PRICES)
        return [float(el.text.replace("$", "")) for el in elements]