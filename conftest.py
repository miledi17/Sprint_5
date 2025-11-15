import pytest
from selenium import webdriver
import sys
sys.path.append(r"D:\Sprint_5.git\Sprint_5")
from my_packages.data import Urls
 
@pytest.fixture(params=['chrome', 'firefox'], scope='class')
#@pytest.fixture(params=['firefox'], scope='class')
def driver(request):
    if request.param == "chrome":  
        driver = webdriver.Chrome()
    if request.param == "firefox":  
        driver = webdriver.Firefox()
    
    # Переход на сайт
    driver.get(Urls.URL)

    yield driver
    driver.quit()