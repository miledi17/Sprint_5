import time
import uuid
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys
sys.path.append(r"D:\Sprint_5.git\Sprint_5")
from my_packages.data import Urls, UserData, AdditionalData
from my_packages.locators import TestLocators

class TestingRegistration:
    def test_registration(self, driver):
         # Добавь явное ожидание для загрузки страницы
        time.sleep(5)

        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()

        # Добавь явное ожидание для загрузки страницы
        time.sleep(5)

        # Найди слово "Зарегистрироваться" и кликни по нему
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.WORD_REGISTRATION)).click()

        # Найди поле "Имя" и заполни его
        driver.find_element(*TestLocators.NAME).send_keys(UserData.USERNAME)

        # Найди поле "Email" и заполни его
        driver.find_element(*TestLocators.EMAIL).send_keys(AdditionalData.LOGIN_RANDOM.format(uuid = uuid.uuid4()))

        # Найди поле "Пароль" и заполни его
        driver.find_element(*TestLocators.PASSWORD).send_keys(UserData.PASSWORD)

        # Добавь явное ожидание для загрузки страницы
        time.sleep(5)

        # Найди кнопку "Зарегистрироваться" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_REGISTRATION)).click()
        
        time.sleep(5)
        # Проверь, что текущий url равен 'https://stellarburgers.education-services.ru/login'
        assert driver.current_url.rstrip('/') == Urls.URL_LOGIN

    def test_registration_error(self, driver):
        
        # Добавь явное ожидание для загрузки страницы
        time.sleep(5)

        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()

        # Добавь явное ожидание для загрузки страницы
        time.sleep(5)

        # Найди слово "Зарегистрироваться" и кликни по нему
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.WORD_REGISTRATION)).click()

        # Найди поле "Имя" и заполни его
        driver.find_element(*TestLocators.NAME).send_keys(UserData.USERNAME)

        # Найди поле "Email" и заполни его
        driver.find_element(*TestLocators.EMAIL).send_keys(UserData.LOGIN)

        # Найди поле "Пароль" и заполни его
        driver.find_element(*TestLocators.PASSWORD).send_keys(' ')

        # Добавь явное ожидание для загрузки страницы
        time.sleep(5)

        # Найди кнопку "Зарегистрироваться" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_REGISTRATION)).click()

        # Проверить ошибку для некорректного пароля
        assert driver.find_element(*TestLocators.TEXT_INVALID_PASSWORD).text == 'Некорректный пароль'