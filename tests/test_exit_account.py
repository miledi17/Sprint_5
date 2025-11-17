from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from my_packages.data import Urls
from my_packages.locators import TestLocators

class TestingExitAccount:
    def test_exit_account(self, driver_with_login):
        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver_with_login, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()

        # Найди кнопку "Выход" и кликни по ней
        WebDriverWait(driver_with_login, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_EXIT)).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver_with_login, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER))

        # Проверь, что текущий url равен 'https://stellarburgers.education-services.ru/login'
        assert driver_with_login.current_url == Urls.URL_LOGIN