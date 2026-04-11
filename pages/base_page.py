from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException
)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url):
        self.driver.get(url)
        self.wait_page_loaded()

    def wait_page_loaded(self):
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def clear_modal_overlay(self):
        self.driver.execute_script("""
            const overlays = document.querySelectorAll('[class*="Modal_modal_overlay"]');
            overlays.forEach(el => el.remove());
            document.body.style.overflow = 'auto';
        """)

    def click(self, locator):
        self.clear_modal_overlay()
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except (ElementClickInterceptedException, TimeoutException):
            self.clear_modal_overlay()
            self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_url_contains(self, value):
        return self.wait.until(EC.url_contains(value))

    def wait_for_url_not_contains(self, value):
        return self.wait.until(lambda d: value not in d.current_url)

    def is_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait.until(EC.visibility_of_element_located(source_locator))
        target = self.wait.until(EC.visibility_of_element_located(target_locator))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            source
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            target
        )

        try:
            self.driver.execute_script(
                """
                const source = arguments[0];
                const target = arguments[1];

                const rectSource = source.getBoundingClientRect();
                const rectTarget = target.getBoundingClientRect();

                const dataTransfer = new DataTransfer();

                source.dispatchEvent(new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                }));

                target.dispatchEvent(new DragEvent('dragenter', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer,
                    clientX: rectTarget.left + 10,
                    clientY: rectTarget.top + 10
                }));

                target.dispatchEvent(new DragEvent('dragover', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer,
                    clientX: rectTarget.left + 10,
                    clientY: rectTarget.top + 10
                }));

                target.dispatchEvent(new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer,
                    clientX: rectTarget.left + 10,
                    clientY: rectTarget.top + 10
                }));

                source.dispatchEvent(new DragEvent('dragend', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                }));
                """,
                source,
                target
            )
        except Exception:
            ActionChains(self.driver) \
                .move_to_element(source) \
                .click_and_hold(source) \
                .pause(0.5) \
                .move_to_element(target) \
                .pause(0.5) \
                .release(target) \
                .perform()

    def close_modal_with_escape(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()