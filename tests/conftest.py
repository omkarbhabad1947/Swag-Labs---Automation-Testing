import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    # Start Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)  # show browser
        context = browser.new_context()
        page = context.new_page()

        # Go to website
        page.goto("https://www.saucedemo.com/")

        # Login steps (common for all tests)
        page.fill("input#user-name", "standard_user")
        page.fill("input#password", "secret_sauce")
        page.click("input#login-button")

        # Yield page to the test
        yield page

        # Close after test
        browser.close()