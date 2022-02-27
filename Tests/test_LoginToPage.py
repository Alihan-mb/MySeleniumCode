from POMHere.Config.config import Basics
from POMHere.Pages.LoginPage import LoginHere
from POMHere.Tests.test_base_page import BaseClass

class Test_loginPage(BaseClass):

    def test_titleis(self):
        log = self.getLogger()
        self.login = LoginHere(self.driver)
        title = self.login.finding_title(Basics.LoginPageTitle)
        log.info(title)
        assert title == Basics.LoginPageTitle

    def test_loggingIntoTheApp(self):
        self.login.logging_in(Basics.url, Basics.PASSWORD)


    def test_checking_message(self):
        log = self.getLogger()
        self.login.logging_in(Basics.email, Basics.inc_password)
        error = self.login.err_message()
        log.info(error)
        assert error == Basics.ERROR_MESSAGE