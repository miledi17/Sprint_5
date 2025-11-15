from selenium.webdriver.common.by import By

class TestLocators:
    NAME = By.XPATH, "//label[text() = 'Имя']/following-sibling::input"
    EMAIL = By.XPATH, ".//*[text()='Email']/following-sibling::input"
    PASSWORD = By.XPATH, ".//*[text()='Пароль']/following-sibling::input"

    # слово "Зарегистрироваться"
    WORD_REGISTRATION = By.XPATH, '//a[@href="/register"]'
    # кнопка "Зарегистрироваться"
    BUTTON_REGISTRATION = By.XPATH, '//button[.="Зарегистрироваться"]'
    # надпись "Некорректный пароль"
    TEXT_INVALID_PASSWORD = By.CLASS_NAME, 'input__error'
    # кнопка "Войти в аккаунт"
    BUTTON_ENTER_ACCOUNT = By.XPATH, '//button[.="Войти в аккаунт"]'
    # кнопка "Войти"
    BUTTON_ENTER = By.XPATH, '//button[.="Войти"]'
    # кнопка "Сохранить"
    BUTTON_SAVE = By.XPATH, '//button[.="Сохранить"]'
    # кнопка "Выход"
    BUTTON_EXIT = By.XPATH, '//button[.="Выход"]'
    # кнопка "Конструктор"
    BUTTON_CONSTRUCTOR = By.XPATH, '//p[.="Конструктор"]'
    # кнопка "Лого"
    BUTTON_LOGO = By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']"
    # кнопка "Оформить заказ"
    BUTTON_ORDER = By.XPATH, '//button[.="Оформить заказ"]'
    # раздел "Соусы"
    SITE_SAUCES = By.XPATH, '//span[text() = "Соусы"]'
    # раздел "Начинки"
    SITE_TOPPING = By.XPATH, '//span[text() = "Начинки"]'
    # раздел "Булки"
    SITE_BUNS = By.XPATH, '//span[text() = "Булки"]'
    # кнопка "Личный кабинет"
    BUTTON_ACCOUNT = By.XPATH, '//p[.="Личный Кабинет"]'
    # кнопка "Войти" на странице регистрации
    BUTTON_ENTER_LOG = By.XPATH, '//a[@href="/login"]'
    # кнопка "Восстановить пароль"
    BUTTON_FORGOT_PASSWORD = By.XPATH, '//a[@href="/forgot-password"]'
    # Выбранный раздел конструктора
    SELECETED_CATEGORY = By.CLASS_NAME, 'tab_tab_type_current__2BEPc'