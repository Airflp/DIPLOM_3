import time
import allure

from data.urls import BASE_URL, FEED_URL, LOGIN_URL
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.feed_page import FeedPage


class TestFeed:

    @allure.title("Увеличение счетчика выполнено за все время")
    def test_total_done_increases_after_order(self, driver, create_user):
        user = create_user
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        feed_page.open(FEED_URL)
        total_before = feed_page.get_total_done()

        main_page.open(LOGIN_URL)
        login_page.login(user["email"], user["password"])
        main_page.wait_for_url_not_contains("/login")

        main_page.open(BASE_URL)
        main_page.add_items_to_constructor()
        main_page.wait_order_button_present()
        main_page.create_order()
        time.sleep(5)

        feed_page.open(FEED_URL)
        total_after = feed_page.get_total_done()

        assert total_after >= total_before

    @allure.title("Увеличение счетчика выполнено за сегодня")
    def test_total_today_increases_after_order(self, driver, create_user):
        user = create_user
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        feed_page.open(FEED_URL)
        total_before = feed_page.get_total_today()

        main_page.open(LOGIN_URL)
        login_page.login(user["email"], user["password"])
        main_page.wait_for_url_not_contains("/login")

        main_page.open(BASE_URL)
        main_page.add_items_to_constructor()
        main_page.wait_order_button_present()
        main_page.create_order()
        time.sleep(5)

        feed_page.open(FEED_URL)
        total_after = feed_page.get_total_today()

        assert total_after >= total_before

    @allure.title("После оформления заказа появляется новый номер в разделе В работе")
    def test_order_number_appears_in_work(self, driver, create_user):
        user = create_user
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        feed_page.open(FEED_URL)
        before_orders = feed_page.get_in_work_orders()

        main_page.open(LOGIN_URL)
        login_page.login(user["email"], user["password"])
        main_page.wait_for_url_not_contains("/login")

        main_page.open(BASE_URL)
        main_page.add_items_to_constructor()
        main_page.wait_order_button_present()
        main_page.create_order()

        feed_page.open(FEED_URL)
        appeared = feed_page.wait_for_new_order_in_work(before_orders)

        assert appeared is True