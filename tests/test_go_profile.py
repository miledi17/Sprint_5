import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys
sys.path.append(r"D:\Sprint_5.git\Sprint_5")
from my_packages.data import Urls, UserData
from my_packages.locators import TestLocators

class TestingGoProfile:
    # Переход со стартовой страницы в личный кабинет
    def test_go_profile_start(self, driver):
        # Добавь явное ожидание для загрузки страницы
        time.sleep(5)
        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()

        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER)).click()

        # Проверь, что текущий url равен 'https://stellarburgers.education-services.ru/login'
        assert driver.current_url ==  Urls.URL_LOGIN

    # Переход со стартовой страницы в личный кабинет зарегистрированного пользователя
    def test_go_profile_start_registered(self, driver):

        # Добавь явное ожидание для загрузки страницы
        time.sleep(5)

        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()

        # Найди поле "Email" и заполни его
        driver.find_element(*TestLocators.EMAIL).send_keys(UserData.LOGIN)

        # Найди поле "Пароль" и заполни его
        driver.find_element(*TestLocators.PASSWORD).send_keys(UserData.PASSWORD)

        # Добавь явное ожидание для загрузки страницы
        time.sleep(5)

        # Найди кнопку "Войти" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER)).click()

        # Добавь явное ожидание для загрузки страницы
        time.sleep(5)

        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()

        # Добавь явное ожидание для загрузки страницы
        time.sleep(5)

        # Проверь, что текущий url равен 'hhttps://stellarburgers.education-services.ru/account/profile'
        assert driver.current_url == Urls.URL_PROFILE