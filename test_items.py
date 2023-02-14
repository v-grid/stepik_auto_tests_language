
from selenium.webdriver.common.by import By
import time


address_serv = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class Test_Page:


    def test_find_button(self, browser):
        browser.get(address_serv)
        time.sleep(30)
        assert len(browser.find_elements(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')) > 0, f"Button is not find"






