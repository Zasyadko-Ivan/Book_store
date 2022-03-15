from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegisterLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*RegisterLocators.FIELD_EMAIL)
        email_field.send_keys(email)
        email_password = self.browser.find_element(*RegisterLocators.FIELD_PASSWORD)
        email_password.send_keys(password)
        email_password2 = self.browser.find_element(*RegisterLocators.FIELD_CONFIRM_PASSWORD)
        email_password2.send_keys(password)
        button_register = self.browser.find_element(*RegisterLocators.BOTTON_REGISTER)
        button_register.click()









