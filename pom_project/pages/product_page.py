from pages.base_page import BasePage

class ProductPage(BasePage):
    URL='https://automationexercise.com/products'

    def __init__(self,page):
        super().__init__(page)
        self.search_input=page.locator('#search_product')
        self.search_button=page.locator('#submit_search')
        self.products=page.locator('.product-image-wrapper')
        self.searched_products_title=page.locator('.title.text-center')
        self.product_information=page.locator('.product-information')
        self.product_names=page.locator('.product-information h2')
        self.all_products_heading = page.get_by_role("heading", name="All Products")
        self.website_logo = page.get_by_role("img", name="Website for practice")
        self.women_category_link = page.locator("a[href='#Women']")
        self.men_category_link = page.locator("a[href='#Men']")
        self.kids_category_link = page.locator("a[href='#Kids']")
        self.polo_brand_link = page.get_by_role("link", name="(6) Polo")
        self.product_overlay = page.locator(".product-overlay")
        self.add_to_cart_button = page.get_by_text("Add to cart")
        self.added_heading = page.get_by_role("heading", name="Added!")
        self.continue_shopping_button = page.get_by_role("button", name="Continue Shopping")
        self.price_headings = page.get_by_role("heading", name="Rs.")
        self.frozen_tops_text = page.get_by_text("Frozen Tops For Kids")
        self.first_product_card = page.locator(".product-image-wrapper").first

    def open_products(self):
        self.open(self.URL)

    def search_product(self, product):
        self.search_input.fill(product)
        self.search_button.click()

    def open_first_product(self):
        self.products.first.locator("a[href^='/product_details/']").click()

    def open_women_category(self):
        self.women_category_link.click()

    def open_men_category(self):
        self.men_category_link.click()

    def open_kids_category(self):
        self.kids_category_link.click()

    def open_polo_brand(self):
        self.polo_brand_link.click()

    def hover_first_product(self):
        self.first_product_card.hover()

    def add_first_product_to_cart(self):
        self.first_product_card.hover()
        self.product_overlay.first.get_by_text("Add to cart").click()

    def continue_shopping(self):
        self.continue_shopping_button.click()