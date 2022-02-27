from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(text)

    def click_here(self, locator):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator)).click()

    def text_message(self, locator):
        message = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))
        return message

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(ec.title_is(title))
        return self.driver.title
