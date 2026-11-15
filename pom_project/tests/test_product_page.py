from playwright.sync_api import expect
from pages.product_page import ProductPage


def test_open_products_page(page):
    p = ProductPage(page)
    p.open_products()
    assert '/products' in p.get_url()
    expect(p.products.first).to_be_visible()


def test_all_products_heading_visible(page):
    p = ProductPage(page)
    p.open_products()
    expect(p.all_products_heading).to_contain_text("All Products")


def test_website_logo_visible(page):
    p = ProductPage(page)
    p.open_products()
    expect(p.website_logo).to_be_visible()


def test_search_product(page):
    p = ProductPage(page)
    p.open_products()
    p.search_product("Blue Top")
    expect(p.searched_products_title).to_contain_text("Searched Products")


def test_search_result_contains_product(page):
    p = ProductPage(page)
    p.open_products()
    p.search_product("Blue Top")
    expect(p.products.first).to_contain_text("Blue Top")


def test_open_women_category(page):
    p = ProductPage(page)
    p.open_products()
    p.open_women_category()
    expect(p.women_category_link).to_be_visible()


def test_open_men_category(page):
    p = ProductPage(page)
    p.open_products()
    p.open_men_category()
    expect(p.men_category_link).to_be_visible()


def test_open_kids_category(page):
    p = ProductPage(page)
    p.open_products()
    p.open_kids_category()
    expect(p.kids_category_link).to_be_visible()


def test_open_polo_brand(page):
    p = ProductPage(page)
    p.open_products()
    p.open_polo_brand()
    assert '/brand_products/Polo' in p.get_url()


def test_frozen_tops_product_visible(page):
    p = ProductPage(page)
    p.open_products()
    expect(p.frozen_tops_text.first).to_be_visible()


def test_open_first_product_details(page):
    p = ProductPage(page)
    p.open_products()
    p.open_first_product()
    assert '/product_details/' in p.get_url()
    expect(p.product_information).to_be_visible()

def test_product_overlay_visible_on_hover(page):
    p = ProductPage(page)
    p.open_products()
    p.hover_first_product()
    expect(p.add_to_cart_button.first).to_be_visible()


def test_add_to_cart_shows_added_modal(page):
    p = ProductPage(page)
    p.open_products()
    p.add_first_product_to_cart()
    expect(p.added_heading).to_contain_text("Added!")


def test_continue_shopping_after_add(page):
    p = ProductPage(page)
    p.open_products()
    p.add_first_product_to_cart()
    expect(p.added_heading).to_contain_text("Added!")
    p.continue_shopping()
    assert '/products' in p.get_url()

