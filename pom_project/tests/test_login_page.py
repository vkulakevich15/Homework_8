from playwright.sync_api import expect
from pages.login_page import LoginPage

VALID_EMAIL = "nika_test@mail.ru"
VALID_PASSWORD = "Password123"

def test_open_login_page(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    assert "login" in login_page.get_url()

def test_email_field_visible(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    expect(login_page.email_input).to_be_visible()

def test_password_field_visible(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    expect(login_page.password_input).to_be_visible()

def test_login_button_visible(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    expect(login_page.login_button).to_be_visible()

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login("123@df.er", "123")
    expect(login_page.error_message).to_be_visible()


def test_invalid_password(page):
    login = LoginPage(page)
    login.open_login_page()
    login.login(VALID_EMAIL, "qwert123")
    expect(login.error_message).to_contain_text("Your email or password is incorrect!")


def test_invalid_email(page):
    login = LoginPage(page)
    login.open_login_page()
    login.login("qwert123@mail.ru", VALID_PASSWORD)
    expect(login.error_message).to_contain_text("Your email or password is incorrect!")


def test_empty_fields(page):
    login = LoginPage(page)
    login.open_login_page()
    login.login_button.click()
    expect(page).to_have_url("https://automationexercise.com/login")


def test_login_with_email_only(page):          
    login = LoginPage(page)
    login.open_login_page()
    login.email_input.fill(VALID_EMAIL)
    login.login_button.click()
    expect(page).to_have_url("https://automationexercise.com/login")
    expect(login.logged_in_user).not_to_be_visible()

def test_login_with_password_only(page):
    login = LoginPage(page)
    login.open_login_page()
    login.password_input.fill(VALID_PASSWORD)
    login.login_button.click()
    expect(page).to_have_url("https://automationexercise.com/login")
    expect(login.logged_in_user).not_to_be_visible()

def test_fields_keep_values_after_failed_login(page):
    login = LoginPage(page)
    login.open_login_page()
    login.login("qwert555@mail.ru", "Qwert12345")
    expect(login.error_message).to_contain_text("Your email or password is incorrect!")
    expect(login.email_input).to_have_value("qwert555@mail.ru")
    expect(login.password_input).to_have_value("Qwert12345")