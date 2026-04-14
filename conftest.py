import random
import string

import pytest
import requests

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from data.urls import BASE_URL, REGISTER_ENDPOINT, USER_ENDPOINT


def generate_user():
    rand = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return {
        "email": f"ui_{rand}@yandex.ru",
        "password": "123456",
        "name": f"user_{rand}"
    }


@pytest.fixture(scope="session", params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    driver = None

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    else:
        options = FirefoxOptions()
        options.add_argument("-headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        last_error = None
        for _ in range(2):
            try:
                driver = webdriver.Firefox(
                    service=FirefoxService(GeckoDriverManager().install()),
                    options=options
                )
                break
            except WebDriverException as error:
                last_error = error

        if driver is None:
            raise last_error

    driver.set_window_size(1920, 1080)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def reset_app_state(driver):
    driver.get(BASE_URL)
    driver.execute_script("""
        const overlays = document.querySelectorAll('[class*="Modal_modal_overlay"]');
        overlays.forEach(el => el.remove());
        document.body.style.overflow = 'auto';
    """)
    return


@pytest.fixture
def create_user():
    payload = generate_user()

    response = requests.post(REGISTER_ENDPOINT, json=payload)

    access_token = None
    if response.status_code == 200:
        access_token = response.json().get("accessToken")

    yield payload

    if access_token:
        requests.delete(
            USER_ENDPOINT,
            headers={"Authorization": access_token}
        )