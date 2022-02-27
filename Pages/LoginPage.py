import self
from selenium.webdriver.common.by import By

from POMHere.Pages.BasePage import BasePage


class LoginHere(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    '''LocatorsHere'''
    Email = (By.CSS_SELECTOR, "input[name='login']")
    Button = (By.CSS_SELECTOR, "button[data-testid='enter-password']")
    Password = (By.CSS_SELECTOR, "input[name='password']")
    Error_message = (By.CSS_SELECTOR, "div[class='error svelte-1da0ifw']")

    def logging_in(self, username, password):
        self.send_keys(self.Email, username)
        self.click_here(self.Button)
        self.send_keys(self.Password, password)

    def finding_title(self, title):
        return self.get_title(title)

    def err_message(self):
        return self.text_message(self.Error_message)









