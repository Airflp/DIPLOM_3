from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//a[.//p[text()='Конструктор']]")
    FEED_BUTTON = (By.XPATH, ".//a[contains(@href, '/feed')]")

    INGREDIENT_CARD = (
        By.XPATH,
        "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]"
    )
    INGREDIENT_MODAL = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Modal_modal__close')]"
    )

    BUN_CARD = (
        By.XPATH,
        "(//a[contains(@class, 'BurgerIngredient_ingredient')][.//p[contains(text(),'булка')]])[1]"
    )
    FILLING_CARD = (
        By.XPATH,
        "(//a[contains(@class, 'BurgerIngredient_ingredient')][not(.//p[contains(text(),'булка')])])[1]"
    )

    BUN_COUNTER = (
        By.XPATH,
        "(//a[contains(@class, 'BurgerIngredient_ingredient')][.//p[contains(text(),'булка')]]//p[contains(@class,'counter_counter__num')])[1]"
    )

    BURGER_CONSTRUCTOR_DROP_AREA = (
        By.XPATH,
        ".//section[contains(@class, 'BurgerConstructor_basket')]"
    )

    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")

    ORDER_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Оформить заказ' or contains(., 'Оформить заказ')]"
    )

    ORDER_BUTTON_IN_CONSTRUCTOR = (
        By.XPATH,
        "//section[contains(@class,'BurgerConstructor')]//button[contains(., 'Оформить заказ')]"
    )

    ORDER_MODAL_NUMBER = (
        By.XPATH,
        ".//h2[contains(@class,'Modal_modal__title_shadow')]"
    )