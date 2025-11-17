from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from my_packages.data import Urls, UserData
from my_packages.locators import TestLocators

class TestingGoProfileToConstructor:
    # Переход из личного кабинета в конструктор
    def test_go_profile_to_constructor(self, driver_with_login):
        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver_with_login, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()

        # Найди кнопку "Конструктор" и кликни по ней
        WebDriverWait(driver_with_login, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_CONSTRUCTOR)).click()

        # Сохроняем url
        url = driver_with_login.current_url.rstrip('/')

        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver_with_login, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()

        # Выходим
        WebDriverWait(driver_with_login, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_EXIT)).click()
        
        # Проверь, что текущий url равен 'https://stellarburgers.education-services.ru/'
        assert url == Urls.URL

    # Переход из личного кабинета по лого
    def test_go_profile_to_logo(self, driver_with_login):
        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver_with_login, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()

        # Найди "Логотип" и кликни по нему
        WebDriverWait(driver_with_login, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGO)).click()

        # Сохроняем url
        url = driver_with_login.current_url.rstrip('/')

        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver_with_login, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()

        # Выходим
        WebDriverWait(driver_with_login, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_EXIT)).click()

        # Проверь, что текущий url равен 'https://stellarburgers.education-services.ru/'
        assert url == Urls.URL