import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys
sys.path.append(r"D:\Sprint_5.git\Sprint_5")
from my_packages.data import Urls, UserData
from my_packages.locators import TestLocators

class TestingGoProfileToConstructor:
    # Переход из личного кабинета в конструктор
    def test_go_profile_to_constructor(self, driver):

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

        # Найди кнопку "Конструктор" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_CONSTRUCTOR)).click()

        # Добавь явное ожидание для загрузки страницы
        time.sleep(5)

        # Сохроняем url
        url = driver.current_url.rstrip('/')

        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()

        # Добавь явное ожидание для загрузки страницы
        time.sleep(5)

        # Выходим
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_EXIT)).click()
        
        # Проверь, что текущий url равен 'https://stellarburgers.education-services.ru/'
        assert url == Urls.URL

    # Переход из личного кабинета по лого
    def test_go_profile_to_logo(self, driver):

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

        # Найди "Логотип" и кликни по нему
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGO)).click()

        # Добавь явное ожидание для загрузки страницы
        time.sleep(5)

        # Сохроняем url
        url = driver.current_url.rstrip('/')

        # Найди кнопку "Личный кабинет" и кликни по ней
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ACCOUNT)).click()

        # Добавь явное ожидание для загрузки страницы
        time.sleep(5)

        # Выходим
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_EXIT)).click()

        # Проверь, что текущий url равен 'https://stellarburgers.education-services.ru/'
        assert url == Urls.URL