import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait
import time


address_serv = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class Test_Page:

    '''def test_open_page(self, browser):
        browser.get(address_serv)
        time.sleep(5)
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'login_link')))
        assert len(browser.find_elements(By.ID, 'language_selector')) > 0, "Should be absolute value of a number"
'''
    def test_find_button(self, browser):
        browser.get(address_serv)
        time.sleep(30)
        assert len(browser.find_elements(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')) > 0, f"Button is not find"

    '''def test_button_is_clickable(self, browser):
        browser.get(address_serv)
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket').click()
        assert len(browser.find_elements(By.CLASS_NAME, 'alertinner')) > 0, f'Button is not clickable'''




