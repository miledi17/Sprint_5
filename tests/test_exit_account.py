import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys
sys.path.append(r"D:\Sprint_5.git\Sprint_5")
from my_packages.data import Urls, UserData
from my_packages.locators import TestLocators

class TestingExitAccount:
    def test_exit_account(self, driver):
        # Добавь явное ожидание для загрузки страницы
        time.sleep(5)
        # Найди кнопку "Войти в аккаунт" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER_ACCOUNT)).click()

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
        # Найди кнопку "Выход" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_EXIT)).click()

        # Добавь явное ожидание для загрузки страницы
        time.sleep(5)
        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER))

        # Добавь явное ожидание для загрузки страницы
        time.sleep(5)

        # Проверь, что текущий url равен 'https://stellarburgers.education-services.ru/login'
        assert driver.current_url == Urls.URL_LOGIN