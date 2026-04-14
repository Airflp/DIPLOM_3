from selenium.webdriver.common.by import By


class FeedPageLocators:
    TOTAL_DONE = (
        By.XPATH,
        "(//p[text()='Выполнено за все время:']/following-sibling::p)[1]"
    )

    TOTAL_TODAY = (
        By.XPATH,
        "(//p[text()='Выполнено за сегодня:']/following-sibling::p)[1]"
    )

    # Правая колонка "Готово"
    READY_ORDERS = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderListReady')]/li"
    )

    # Левая/средняя колонка "В работе"
    IN_WORK_ORDERS = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderList') and not(contains(@class, 'OrderFeed_orderListReady'))]/li"
    )