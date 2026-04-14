from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def login(self, email, password):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)