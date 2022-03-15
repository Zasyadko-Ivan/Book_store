from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.XPATH, '//a[@id="login_link"]')
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    BUTTON_VIEW_BASKET = (By.XPATH, '//a[@class="btn btn-default"]')
    NOTIFICATION_ADDED_TO_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRICE_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    NAME_BOOK = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRICE_BOOK = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    CLEAN_BASKET = (By.XPATH, '//*[@id="content_inner"]/p/a')
    CLEAN_BASKET_TX = (By.XPATH, '//p[contains(text(), "empty")]')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class RegisterLocators():
    FIELD_EMAIL = (By.XPATH, '//*[@id="id_registration-email"]')
    FIELD_PASSWORD = (By.XPATH, '//input[@name="registration-password1"]')
    FIELD_CONFIRM_PASSWORD = (By.XPATH, '//input[@name="registration-password2"]')
    BOTTON_REGISTER = (By.XPATH, '//button[@name="registration_submit"]')



