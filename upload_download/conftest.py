import pytest
import allure
from playwright.sync_api import sync_playwright


# @pytest.fixture(params=["chromium", "firefox"])
@pytest.fixture(params=["chromium"])
def page(request):

    with sync_playwright() as p:

        browser_type = getattr(p, request.param)

        browser = browser_type.launch(
            headless=False,
            slow_mo=1000,
            args=[
                "--start-maximized",
                "--window-position=0,-1080"
            ]
        )

        context = browser.new_context(
            viewport={
                "width": 900,
                "height": 950
            }
        )

        page = context.new_page()

        yield page

        context.close()
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:
            filename = f"screenshots/{item.name}.png"

            page.screenshot(
                path=filename,
                full_page=True
            )

            allure.attach.file(
                filename,
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
