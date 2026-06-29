from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class CartPage(BasePage):
    CART_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    REMOVE_BTN = (By.XPATH, "//button[contains(@id, 'remove-')]")
    CHECKOUT_BTN = (By.CSS_SELECTOR, "button#checkout")

    @allure.step("Получение названия товара в корзине")
    def get_item_name(self):
        return self.get_text(self.CART_ITEM_NAME)

    @allure.step("Удаление товара внутри корзины")
    def remove_item(self):
        self.click_to(self.REMOVE_BTN)

    @allure.step("Переход к оформлению заказа (клик Checkout)")
    def click_checkout(self):
        self.click_to(self.CHECKOUT_BTN)

    @allure.step("Проверка, пуста ли корзина")
    def is_cart_empty(self):
        try:
            self.find_element(self.CART_ITEM_NAME, timeout=2)
            return False
        except:
            return True