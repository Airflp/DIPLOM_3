from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")