from playwright.sync_api import expect
from pages.home_page import HomePage

def test_open_home_page(page):
    h = HomePage(page) 
    h.open_home_page() 
    assert 'Automation Exercise' in h.get_title()

def test_featured_products_visible(page):
    h = HomePage(page)
    h.open_home_page() 
    expect(h.featured_products).to_be_visible()

def test_navigation_to_products(page):
    h = HomePage(page)
    h.open_home_page()
    h.go_to_products()
    assert '/products' in h.get_url()
    expect(page).to_have_url('https://automationexercise.com/products')

def test_navigation_to_login(page):
    h = HomePage(page)
    h.open_home_page()
    h.go_to_login()
    assert '/login' in h.get_url()
    expect(page).to_have_url('https://automationexercise.com/login')

def test_navigation_to_contact(page):
    h = HomePage(page)
    h.open_home_page()
    h.go_to_contact_us()
    assert '/contact_us' in h.get_url()
    expect(page).to_have_url('https://automationexercise.com/contact_us')


def test_navigation_to_cart(page):
    h = HomePage(page)
    h.open_home_page()
    h.go_to_cart()
    assert '/view_cart' in h.get_url()
    expect(page).to_have_url('https://automationexercise.com/view_cart')

def test_category_block_visible(page):
    h = HomePage(page)
    h.open_home_page()
    expect(h.category_block).to_be_visible()


def test_brands_block_visible(page):
    h = HomePage(page)
    h.open_home_page()
    expect(h.brands_block).to_be_visible()


def test_scroll_up(page):
    h = HomePage(page)
    h.open_home_page()
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    h.scroll_to_top()
    expect(page.locator("#scrollUp")).to_be_hidden()


def test_subscription_success(page):
    h = HomePage(page)
    h.open_home_page()
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    h.open_subscription()
    expect(h.subscription_heading).to_contain_text("Subscription")
    h.subscribe("test1@mail.ru")
    expect(h.subscription_success).to_contain_text("You have been successfully subscribed!")
