import time

from selenium.webdriver.common.by import By

from Tests.test_BasePage import BasePage


class Test_yandex(BasePage):

    
    def test_logging(self):
        log = self.getLogger()
        self.web_driver.find_element(By.XPATH, "//a[contains(.,'Войти')]").click()
        self.web_driver.find_element(By.ID, "passp-field-login").send_keys("89880604983")
        self.web_driver.find_element(By.ID, "passp:sign-in").click()
        self.web_driver.find_element(By.ID, "passp-field-passwd").send_keys("Marsianin")
        self.web_driver.find_element(By.ID, "passp:sign-in").click()
        c_number = self.web_driver.find_element(By.XPATH, "//strong").text
        log.info(c_number)
        self.web_driver.find_element(By.TAG_NAME, "button").click()
        code = input() #Тест с input нельзя назвать автоматизированным, данный тест для самообучения
        code_to_num = int(code)
        time.sleep(8)
        self.web_driver.find_element(By.ID, "passp-field-phoneCode").send_keys(code_to_num)
        self.web_driver.find_element(By.XPATH, "//button[@type='submit']").click()

        name_here = self.web_driver.find_element(By.XPATH, "//div[contains(text(), 'Алихан Магомедалиев')]").text
        print(name_here)
        assert name_here == "Алихан Магомедалиев"

    def test_city_settings(self):
        #тест иногда крашится, иногда работает, выяснить почему
        log = self.getLogger()
        self.web_driver.find_element(By.CSS_SELECTOR, "div[class='_6RmNB']").click()
        time.sleep(6)
        self.web_driver.find_element(By.CSS_SELECTOR, "input[class='_3qxDp']").clear()
        time.sleep(3)
        self.web_driver.find_element(By.CSS_SELECTOR, "input[class='_3qxDp']").send_keys("Москва")
        time.sleep(3)
        locations = self.web_driver.find_elements(By.XPATH, "//li")
        d_here = self.web_driver.find_element(By.XPATH, "//button//span[contains(text(), 'Привезти сюда')]")
        time.sleep(5)
        for ele in locations:
            log.info(ele.text)
            if "деревня Москва" in ele.text:
                ele.click()
                d_here.click()
                break
        else:
            try:
                pass
            except Exception:
                ex_message = self.web_driver.find_element(By.XPATH, "//div[contains(text(), 'Адрес не подходит')]")
                print(ex_message.text)

        d_here.click()
        address = self.web_driver.find_element(By.CSS_SELECTOR, "._2irI2")
        time.sleep(4)
        log.info(address.text)
        assert "деревня Москва," in address.text



