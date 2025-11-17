from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from my_packages.data import Urls
from my_packages.locators import TestLocators

class TestingGoProfile:
    # Переход со стартовой страницы в личный кабинет
    def test_go_profile_start(self, driver):
        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER)).click()

        # Проверь, что текущий url равен 'https://stellarburgers.education-services.ru/login'
        assert driver.current_url ==  Urls.URL_LOGIN

    # Переход со стартовой страницы в личный кабинет зарегистрированного пользователя
    def test_go_profile_start_registered(self, driver_with_login):
        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver_with_login, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()

        # Проверь, что текущий url равен 'hhttps://stellarburgers.education-services.ru/account/profile'
        assert driver_with_login.current_url == Urls.URL_PROFILE