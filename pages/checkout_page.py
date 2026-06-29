from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input#first-name")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id='last-name']")
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "input#postal-code")
    CONTINUE_BUTTON = (By.XPATH, "//input[@id='continue']")
    FINISH_BUTTON = (By.CSS_SELECTOR, "button#finish")
    COMPLETE_HEADER = (By.XPATH, "//h2[@class='complete-header']")
    ERROR_CONTAINER = (By.CSS_SELECTOR, "h3[data-test='error']")

    @allure.step("Заполнение формы доставки: Имя='{first}', Фамилия='{last}', Индекс='{zip_code}'")
    def fill_shipping_info(self, first, last, zip_code):
        if first: self.find_element(self.FIRST_NAME_INPUT).send_keys(first)
        if last: self.find_element(self.LAST_NAME_INPUT).send_keys(last)
        if zip_code: self.find_element(self.POSTAL_CODE_INPUT).send_keys(zip_code)
        self.click_to(self.CONTINUE_BUTTON)

    @allure.step("Подтверждение заказа (клик Finish)")
    def finish_checkout(self):
        self.click_to(self.FINISH_BUTTON)

    @allure.step("Получение финального сообщения об успешном заказе")
    def get_complete_header_text(self):
        return self.get_text(self.COMPLETE_HEADER)

    @allure.step("Получение текста ошибки валидации формы заказа")
    def get_error_message(self):
        return self.get_text(self.ERROR_CONTAINER)