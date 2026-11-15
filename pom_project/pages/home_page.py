from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "/"

    def __init__(self, page):
        super().__init__(page)
        self.products_link = page.locator("a[href='/products']")
        self.login_link = page.locator("a[href='/login']")
        self.contact_us_link = page.locator("a[href='/contact_us']")
        self.featured_products = page.locator(".features_items")
        self.cart_link = page.get_by_role("link", name="Cart")
        self.category_block = page.locator(".left-sidebar .panel-group").first
        self.brands_block = page.locator(".brands_products")
        self.scroll_up_button = page.locator("#scrollUp")
        self.subscription_heading = page.get_by_role("heading", name="Subscription")
        self.subscription_email = page.get_by_role("textbox", name="Your email address")
        self.subscribe_button = page.locator("#subscribe")
        self.subscription_success = page.get_by_text("You have been successfully")
    

    def open_home_page(self): 
        self.open(self.URL)

    def go_to_products(self): 
        self.products_link.click()

    def go_to_login(self): 
        self.login_link.click()

    def go_to_contact_us(self): 
        self.contact_us_link.click() 

    def go_to_cart(self):
        self.cart_link.click()

    def open_category(self):
        self.category_heading.click()

    def open_brands(self):
        self.brands_heading.click()

    def scroll_to_top(self):
        self.scroll_up_button.click()

    def open_subscription(self):
        self.subscription_heading.click()

    def subscribe(self, email):
        self.subscription_email.click()
        self.subscription_email.fill(email)
        self.subscribe_button.click()   
