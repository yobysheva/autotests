from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.saucedemo.com"

    def open(self, relative_url=""):
        self.driver.get(f"{self.base_url}{relative_url}")

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Не удалось дождаться элемента: {locator}"
        )

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Не удалось дождаться элементов: {locator}"
        )

    def click_to(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент не кликабелен: {locator}"
        )
        element.click()

    def get_text(self, locator, timeout=10):
        return self.find_element(locator, timeout).text