from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_the_correct_book_has_been_added_to_the_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_a_book_to_the_basket()
    page.solve_quiz_and_get_code()
    page.name_book_page()
    page.price_book_page()