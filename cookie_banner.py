from playwright.sync_api import sync_playwright


def accept_cookies(page):
    button = page.get_by_role(
        "button",
        name="Accept"
    )

    if button.is_visible(timeout=3000):
        button.click()


def demo_cookie_banner():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=1000,
            args=["--disable-features=LocalNetworkAccessChecks"]
        )

        page = browser.new_page()

        page.goto("https://demos.devexpress.com/")

        try:
            # accept_cookies(page)
            page.get_by_role("button", name="Accept All Cookies").click()
            page.locator("#wsMsgWnd > .CloseButton").click()
        except:
            pass    

        page.wait_for_timeout(3000)

        browser.close()


demo_cookie_banner()