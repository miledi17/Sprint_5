from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from my_packages.locators import TestLocators

class TestingSiteConstructor:
    # Тест переходов(табов) конструктора
    def test_constructor(self, driver):
        # Найди раздел "Соусы" и кликни по нему
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.SITE_SAUCES)).click()

        # Проверь, что отобразились соусы
        isSouces = driver.find_element(*TestLocators.SELECETED_CATEGORY).text == 'Соусы'
        
        # Найди раздел "Начинки" и кликни по нему
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.SITE_TOPPING)).click()

        # Проверь, что отобразились начинки
        isToppings = driver.find_element(*TestLocators.SELECETED_CATEGORY).text == 'Начинки'

        # Найди раздел "Булки" и кликни по нему
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.SITE_BUNS)).click()

        # Проверь, что отобразились булки
        isBuns = driver.find_element(*TestLocators.SELECETED_CATEGORY).text == 'Булки'

        assert isSouces and isToppings and isBuns