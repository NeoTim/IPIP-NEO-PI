from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
from selenium.webdriver.support.ui import Select
import time

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8888/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_name("Nick").clear()
        driver.find_element_by_name("Nick").send_keys("hello")
        driver.find_element_by_name("Sex").click()
        driver.find_element_by_name("Age").clear()
        driver.find_element_by_name("Age").send_keys("28")

        Select(driver.find_element_by_name('Country')).select_by_index(3)

        # 76, 82, 64, 63, 88, 26, 84 (Extraversion)
        answers = "455454245414355144252442444444435454354214445435053442424254" + "455453415314242354554251515543245452445414245444452135425154"

        answers = list(map(int, list(answers)))

        N = 120
        for i in range(1, N + 1):
            if answers[i - 1] == 0:
                continue
            xpath = "(//input[@name='Q%s'][@value=%d])" % (i, answers[i - 1])
            print(xpath)
            driver.find_element_by_xpath(xpath).click()

        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        time.sleep(3000)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
