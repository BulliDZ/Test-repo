import pytest


class TestStore:
    def test_browser_view(self, browser):
        browser.implicitly_wait(10)
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        print("In browser...")
        basket_button = browser.find_element_by_css_selector(".btn.btn-add-to-basket")
        print(basket_button.text.lower())
