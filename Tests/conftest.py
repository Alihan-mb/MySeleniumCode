import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager




@pytest.fixture(params=["chrome"], scope='class')
def setup(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        print("there is no other browsers to be invoked")
    request.cls.driver = driver
    driver.get("https://mail.ru/")

    yield driver
    time.sleep(2)
    driver.close()