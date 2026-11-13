from playwright.sync_api import sync_playwright, expect


def demo_tabs():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=1000
        )

        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/windows")
        
        with page.expect_popup() as popup_info:
            page.get_by_text("Click Here").click()

        new_page = popup_info.value

        print(new_page.title())

        new_page.bring_to_front()
        page.bring_to_front()
        new_page.bring_to_front()

        new_page.close()
        page.bring_to_front()

        page.wait_for_timeout(3000)

        browser.close()


# demo_tabs()

def test_tabs(page):
    page.goto("https://the-internet.herokuapp.com/windows")

    assert len(page.context.pages) == 1

    with page.expect_popup() as popup_info:
        page.get_by_text("Click Here").click()

    new_page = popup_info.value
    expect(new_page).to_have_url("https://the-internet.herokuapp.com/windows/new")
    expect(new_page).to_have_title("New Window")
    expect(new_page.get_by_text("New Window")).to_be_visible()
    assert len(page.context.pages) == 2

    new_page.close()
    assert len(page.context.pages) == 1