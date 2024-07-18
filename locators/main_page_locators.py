from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка "Личный Кабинет"
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, "//p[contains(text(),'Личный Кабинет')]"

    # Кнопка "Конструктор"
    BUTTON_CONSTRUCTOR = By.LINK_TEXT, "Конструктор"

    # Заголовок конструктора
    HEADER_CONSTRUCTOR = By.XPATH, '//h1[text() = "Соберите бургер"]'

    # Кнопка "Лента заказов"
    BUTTON_ORDERS_FEED = By.XPATH, "//p[contains(text(),'Лента Заказов')]"

    # Ингредиент/объект из меню
    OBJECT_INGREDIENT = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'

    # Заголовок "Детали ингредиента"
    HEADER_DETAILS_INGREDIENT = By.XPATH, '//h2[text() = "Детали ингредиента"]'

    # Кнопка "крестик"
    BUTTON_CLOSE = By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains(@class, "Modal_modal__container")]'

    # Куда перетащить ингредиенты
    PLACE_INGREDIENT = By.XPATH, ".//ul[@class = 'BurgerConstructor_basket__list__l9dp_']"

    # Счетчик количества ингредиентов
    INGREDIENT_COUNT = By.XPATH, './/p[contains(@class, "counter_counter__num__3nue1")]'

    # Кнопка "Оформить заказ"
    BUTTON_ARRANGE_ORDER = By.XPATH, "//button[contains(text(),'Оформить заказ')]"

    # Подтверждение оформления заказа
    CONFIRM_ARRANGE_ORDER = By.XPATH, "//p[contains(text(),'Ваш заказ начали готовить')]"

    # Форма главной страница сайта
    FORM_MAIN_PAGE = By.CLASS_NAME, "App_App__aOmNj"

    # Кнопка с логотипом stellar_burgers
    BUTTON_LOGO = By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']"