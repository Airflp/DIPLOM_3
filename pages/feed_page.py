import time

from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    def get_total_done(self):
        return int(self.get_text(FeedPageLocators.TOTAL_DONE))

    def get_total_today(self):
        return int(self.get_text(FeedPageLocators.TOTAL_TODAY))

    def get_in_work_orders(self):
        elements = self.driver.find_elements(*FeedPageLocators.IN_WORK_ORDERS)
        result = []

        for element in elements:
            text = element.text.strip()
            if text:
                result.append(text)

        return result

    def wait_for_new_order_in_work(self, before_orders, attempts=10, delay=2):
        before_set = set(before_orders)

        for _ in range(attempts):
            current_orders = self.get_in_work_orders()
            current_set = set(current_orders)

            if current_set - before_set:
                return True

            time.sleep(delay)

        return False