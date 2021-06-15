import pytest
import time


class TestStore:
    def test_basket_button(self, browser):
        browser.implicitly_wait(10)
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        time.sleep(30)
        print("In browser...")
        basket_button = browser.find_element_by_css_selector(".btn.btn-add-to-basket")
        print(basket_button.text.lower())
        assert basket_button
