from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from my_packages.data import Urls, UserData
from my_packages.locators import TestLocators

def exit_account(driver):
        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()        # Добавь явное ожидание для загрузки страницы

        # Найди кнопку "Выход" и кликни по ней
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_EXIT)).click()

        # Переход на сайт
        driver.get(Urls.URL)

class TestingLoginPage:
    # вход по кнопке "Войти в аккаунт" на главной
    def test_login_page_log_account(self, driver):
        # Найди кнопку "Войти в аккаунт" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER_ACCOUNT)).click()
        
        # Найди поле "Email" и заполни его
        driver.find_element(*TestLocators.EMAIL).send_keys(UserData.LOGIN)

        # Найди поле "Пароль" и заполни его
        driver.find_element(*TestLocators.PASSWORD).send_keys(UserData.PASSWORD)

        # Найди кнопку "Войти" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER)).click()

        url = driver.current_url.rstrip('/')
        button_text = driver.find_element(*TestLocators.BUTTON_ORDER).text
        # Выходим из аккаунта
        exit_account(driver)

        # Проверь, что текущий url равен 'https://stellarburgers.education-services.ru/'
        assert url == Urls.URL and button_text == 'Оформить заказ'

    # вход через кнопку "личный кабинет"
    def test_login_page_profile(self, driver):
        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()

         # Найди поле "Email" и заполни его
        driver.find_element(*TestLocators.EMAIL).send_keys(UserData.LOGIN)

        # Найди поле "Пароль" и заполни его
        driver.find_element(*TestLocators.PASSWORD).send_keys(UserData.PASSWORD)

        # Найди кнопку "Войти" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER)).click()

        # Сохраняем данные для теста после входа
        url = driver.current_url.rstrip('/')
        button_text = driver.find_element(*TestLocators.BUTTON_ORDER).text
        # Выходим из аккаунта
        exit_account(driver)

        # Проверь, что текущий url равен 'https://stellarburgers.education-services.ru/' и текст кнопки изменился на "Оформить заказ"
        assert url == Urls.URL and button_text == 'Оформить заказ'

    # вход через кнопку в форме регистрации
    def test_login_page_registration(self, driver):
        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()

        # Найди слово "Зарегистрироваться" и кликни по нему
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.WORD_REGISTRATION)).click()

        # Найди кнопку "Войти в аккаунт" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER_LOG)).click()

        # Найди поле "Email" и заполни его
        driver.find_element(*TestLocators.EMAIL).send_keys(UserData.LOGIN)

        # Найди поле "Пароль" и заполни его
        driver.find_element(*TestLocators.PASSWORD).send_keys(UserData.PASSWORD)

        # Найди кнопку "Войти" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER)).click()
        
         # Проверь, что текущий url равен 'https://stellarburgers.education-services.ru/'
        url = driver.current_url.rstrip('/')
        button_text = driver.find_element(*TestLocators.BUTTON_ORDER).text
        # Выходим из аккаунта
        exit_account(driver)

        # Проверь, что текущий url равен 'https://stellarburgers.education-services.ru/'
        assert url == Urls.URL and button_text == 'Оформить заказ'

    # вход через кнопку в форме восстановления пароля
    def test_login_page_forgot_password(self, driver):
        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()

        # Найди слово "Восстановить пароль" и кликни по нему
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_FORGOT_PASSWORD)).click()

        # Найди кнопку "Войти в аккаунт" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER_LOG)).click()

        # Найди поле "Email" и заполни его
        driver.find_element(*TestLocators.EMAIL).send_keys(UserData.LOGIN)

        # Найди поле "Пароль" и заполни его
        driver.find_element(*TestLocators.PASSWORD).send_keys(UserData.PASSWORD)

        # Найди кнопку "Войти" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER)).click()
        
        # Проверь, что текущий url равен 'https://stellarburgers.education-services.ru/'
        url = driver.current_url.rstrip('/')
        button_text = driver.find_element(*TestLocators.BUTTON_ORDER).text
        # Выходим из аккаунта
        exit_account(driver)

        # Проверь, что текущий url равен 'https://stellarburgers.education-services.ru/'
        assert url == Urls.URL and button_text == 'Оформить заказ'