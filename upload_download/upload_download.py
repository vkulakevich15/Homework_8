from playwright.sync_api import sync_playwright, expect
from pathlib import Path


def demo_upload_download():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=1000
        )

        page = browser.new_page()

        # Upload
        page.goto("https://the-internet.herokuapp.com/upload")

        page.locator("#file-upload").set_input_files(r"C:\Users\assid\Documents\BelhardAcademy\AQA\CodeExamples\16_Lesson\upload_download\document.pdf")
        page.locator("#file-upload").set_input_files(r"C:\Users\assid\Documents\BelhardAcademy\AQA\CodeExamples\16_Lesson\upload_download\picture.png")

        page.locator("#file-submit").click()

        # Download
        page.goto("https://demoqa.com/upload-download")

        with page.expect_download() as download_info:
            page.locator("#downloadButton").click()

        download = download_info.value
        download.save_as("loaded_file.jpeg")

        page.wait_for_timeout(3000)
        browser.close()


# demo_upload_download()


def test_file_upload(page):
    page.goto("https://the-internet.herokuapp.com/upload")

    page.locator("#file-upload").set_input_files(r"C:\Users\assid\Documents\BelhardAcademy\AQA\CodeExamples\16_Lesson\upload_download\document.pdf")

    page.locator("#file-submit").click()

    expect(page.locator("#uploaded-files")).to_have_text("document.pdf")


def test_file_download(page):
    page.goto("https://demoqa.com/upload-download")

    with page.expect_download() as download_info:
        page.locator("#downloadButton").click()

    download = download_info.value

    file_name = download.suggested_filename

    download.save_as(file_name)

    assert Path(file_name).exists()
    