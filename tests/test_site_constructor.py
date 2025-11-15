import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys
sys.path.append(r"D:\Sprint_5.git\Sprint_5")
from my_packages.locators import TestLocators

class TestingSiteConstructor:
    # Переход на соусы
    def test_constructor_sauces(self, driver):
        # Добавь явное ожидание для загрузки страницы
        time.sleep(3)

        # Найди раздел "Соусы" и кликни по нему
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.SITE_SAUCES)).click()

        time.sleep(3)
        # Проверь, что отобразились соусы
        assert driver.find_element(*TestLocators.SELECETED_CATEGORY).text == 'Соусы'

    # Переход на начинки
    def test_constructor_toppings(self, driver):
        # Добавь явное ожидание для загрузки страницы
        time.sleep(3)

        # Найди раздел "Начинки" и кликни по нему
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.SITE_TOPPING)).click()

        time.sleep(3)
        # Проверь, что отобразились начинки
        assert driver.find_element(*TestLocators.SELECETED_CATEGORY).text == 'Начинки'

    # Переход на булки
    def test_constructor_buns(self, driver):
        # Добавь явное ожидание для загрузки страницы
        time.sleep(3)

        # Найди раздел "Булки" и кликни по нему
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.SITE_BUNS)).click()

        # Ожидаем загрузки
        time.sleep(3)
        # Проверь, что отобразились булки
        assert driver.find_element(*TestLocators.SELECETED_CATEGORY).text == 'Булки'