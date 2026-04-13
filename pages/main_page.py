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

    def is_ingredient_modal_opened(self):
        return self.wait_for_visibility(MainPageLocators.INGREDIENT_MODAL).is_displayed()

    def is_ingredient_modal_closed(self):
        return self.wait_for_invisibility(MainPageLocators.INGREDIENT_MODAL)

    def add_items_to_constructor(self):
        self.drag_and_drop(
            MainPageLocators.BUN_CARD,
            MainPageLocators.BURGER_CONSTRUCTOR_DROP_AREA
        )
        self.wait.until(
            lambda d: self.get_bun_counter() == "2"
        )

        self.drag_and_drop(
            MainPageLocators.FILLING_CARD,
            MainPageLocators.BURGER_CONSTRUCTOR_DROP_AREA
        )

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
        self.scroll_to_element(button)

        try:
            button.click()
        except Exception:
            self.click_with_js(button)

    def get_order_number(self):
        return self.get_text(MainPageLocators.ORDER_MODAL_NUMBER)

    def is_feed_opened(self):
        return "feed" in self.get_current_url()

    def is_constructor_opened(self):
        return "feed" not in self.get_current_url()