import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

web_driver = None

@pytest.fixture(params=["chrome"], scope='class')
def starting_yandex(request):
    global web_driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.cls.web_driver = web_driver
    web_driver.get("https://market.yandex.ru/")
    web_driver.implicitly_wait(10)
    yield
    time.sleep(2)
