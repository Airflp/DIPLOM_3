import time

from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_feed(self):
        self.click(MainPageLocators.FEED_BUTTON)

    def open_ingredient_modal(self):
        self.click(MainPageLocators.INGREDIENT_CARD)

    def close_ingredient_modal(self):
        try:
            self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
        except Exception:
            self.close_modal_with_escape()

    def add_items_to_constructor(self):
        self.drag_and_drop(
            MainPageLocators.BUN_CARD,
            MainPageLocators.BURGER_CONSTRUCTOR_DROP_AREA
        )
        time.sleep(1)

        self.drag_and_drop(
            MainPageLocators.FILLING_CARD,
            MainPageLocators.BURGER_CONSTRUCTOR_DROP_AREA
        )
        time.sleep(1)

    def get_bun_counter(self):
        return self.get_text(MainPageLocators.BUN_COUNTER)

    def open_login(self):
        self.click(MainPageLocators.LOGIN_ACCOUNT_BUTTON)

    def wait_order_button_present(self):
        return self.wait.until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )

    def create_order(self):
        button = self.wait_order_button_present()

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )
        time.sleep(1)

        try:
            button.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", button)

    def get_order_number(self):
        return self.get_text(MainPageLocators.ORDER_MODAL_NUMBER)