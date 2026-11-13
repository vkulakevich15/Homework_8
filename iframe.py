from playwright.sync_api import sync_playwright, expect

def iframe_demo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/iframe")

        # iframe = page.frame_locator("#mce_0_ifr")

        # iframe.locator("#tinymce").clear()
        # iframe.locator("#tinymce").fill("Playwright iframe demo")
        page.locator("#tinymce").clear()
        page.locator("#tinymce").fill("Playwright iframe demo")

        page.wait_for_timeout(3000)

        browser.close()

# iframe_demo()


def test_iframe_editor():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/iframe")
        expect(page).to_have_title("The Internet")

        iframe = page.frame_locator("#mce_0_ifr")
        editor = iframe.locator("#tinymce")
        expect(editor).to_be_visible()

        editor.fill("Playwright iframe demo")
        expect(editor).to_have_text("Playwright iframe demo")

        expect(editor).to_have_count(1)

        browser.close()