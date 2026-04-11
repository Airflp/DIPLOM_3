import time
import allure

from data.urls import BASE_URL, FEED_URL, LOGIN_URL
from pages.main_page import MainPage
from pages.login_page import LoginPage
from locators.main_page_locators import MainPageLocators


class TestConstructor:

    @allure.title("Переход по клику на Конструктор")
    def test_click_constructor_button(self, driver):
        page = MainPage(driver)
        page.open(FEED_URL)
        page.click_constructor()

        assert "feed" not in driver.current_url

    @allure.title("Переход по клику на Ленту заказов")
    def test_click_feed_button(self, driver):
        page = MainPage(driver)
        page.open(BASE_URL)
        page.click_feed()

        assert "feed" in driver.current_url

    @allure.title("Открытие модального окна ингредиента")
    def test_ingredient_modal_opens(self, driver):
        page = MainPage(driver)
        page.open(BASE_URL)
        page.open_ingredient_modal()

        assert page.wait_for_visibility(MainPageLocators.INGREDIENT_MODAL).is_displayed()

        page.close_ingredient_modal()
        assert page.wait_for_invisibility(MainPageLocators.INGREDIENT_MODAL)

    @allure.title("Закрытие модального окна по крестику")
    def test_ingredient_modal_closes(self, driver):
        page = MainPage(driver)
        page.open(BASE_URL)
        page.open_ingredient_modal()
        page.close_ingredient_modal()

        assert page.wait_for_invisibility(MainPageLocators.INGREDIENT_MODAL)

    @allure.title("Увеличение счетчика при добавлении ингредиента")
    def test_counter_increases_after_add_ingredient(self, driver):
        page = MainPage(driver)
        page.open(BASE_URL)
        page.add_items_to_constructor()
        time.sleep(2)

        assert page.get_bun_counter() == "2"

    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_authorized_user(self, driver, create_user):
        user = create_user
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.open(LOGIN_URL)
        login_page.login(user["email"], user["password"])

        # ВАЖНО: ждём, пока уйдём именно со страницы логина
        main_page.wait_for_url_not_contains("/login")

        main_page.open(BASE_URL)
        main_page.add_items_to_constructor()
        main_page.wait_order_button_present()
        main_page.create_order()

        order_number = main_page.get_order_number()
        assert int(order_number) > 0