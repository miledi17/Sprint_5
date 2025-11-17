import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from my_packages.data import Urls, UserData
from my_packages.locators import TestLocators
 
@pytest.fixture(params=['chrome', 'firefox'], scope='class')
def driver(request):
    if request.param == "chrome":  
        driver = webdriver.Chrome()
    if request.param == "firefox":  
        driver = webdriver.Firefox()
    
    # Переход на сайт
    driver.get(Urls.URL)

    yield driver
    driver.quit()

@pytest.fixture()
def driver_with_login(driver):
    # Найди кнопку "Войти в аккаунт" и кликни по ней
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER_ACCOUNT)).click()
    
    # Найди поле "Email" и заполни его
    driver.find_element(*TestLocators.EMAIL).send_keys(UserData.LOGIN)

    # Найди поле "Пароль" и заполни его
    driver.find_element(*TestLocators.PASSWORD).send_keys(UserData.PASSWORD)

    # Найди кнопку "Войти" и кликни по ней
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_ENTER)).click()

    return driver