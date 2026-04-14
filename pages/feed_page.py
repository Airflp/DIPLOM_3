from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    def get_total_done(self):
        return int(self.get_text(FeedPageLocators.TOTAL_DONE))

    def get_total_today(self):
        return int(self.get_text(FeedPageLocators.TOTAL_TODAY))

    def get_in_work_orders(self):
        return self.get_elements_text(FeedPageLocators.IN_WORK_ORDERS)

    def wait_total_done_changed(self, previous_value):
        return self.wait.until(
            lambda d: self.get_total_done() >= previous_value
        )

    def wait_total_today_changed(self, previous_value):
        return self.wait.until(
            lambda d: self.get_total_today() >= previous_value
        )

    def wait_for_new_order_in_work(self, before_orders):
        before_set = set(before_orders)
        return self.wait.until(
            lambda d: len(set(self.get_in_work_orders()) - before_set) > 0
        )