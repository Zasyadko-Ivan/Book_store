from .base_page import BasePage
from selenium.webdriver.common.by import By

from .locators import ProductPageLocators

class BasketPage(BasePage):
    def go_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_VIEW_BASKET), "Button basket is not presented"
        button_add_to_basket_link = self.browser.find_element(*ProductPageLocators.BUTTON_VIEW_BASKET)
        button_add_to_basket_link.click()

    def basket_clean(self):
        assert self.is_element_present(*ProductPageLocators.CLEAN_BASKET), "Basket is not clean"

    def basket_clean_tx(self):
        assert self.browser.find_element(*ProductPageLocators.CLEAN_BASKET_TX).text == "Your basket is empty. Continue shopping", "Basket is not clean"


