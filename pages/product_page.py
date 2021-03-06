from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from .locators import RegisterLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time


class ProductPage(BasePage):
    def add_a_book_to_the_basket (self):
        button_add_to_basket_link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket_link.click()

    def name_book_page (self):
        assert self.browser.find_element(*ProductPageLocators.NAME_BOOK).text == self.browser.find_element(*ProductPageLocators.NOTIFICATION_ADDED_TO_BASKET).text, "The name of the added book and the book in the basket do not match"

    def price_book_page (self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text == self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text, "The price of the added book and the books in the basket do not match"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NOTIFICATION_ADDED_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.NOTIFICATION_ADDED_TO_BASKET), \
            "Success message is not disappeared"

    def should_be_login_url_register(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"
        button_register = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        button_register.click()




