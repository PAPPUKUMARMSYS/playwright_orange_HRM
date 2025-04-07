import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def setup(playwright:Playwright):
    browser_context=playwright.chromium.launch(headless=False)
    my_context=browser_context.new_context()
    my_page=my_context.new_page()
    yield my_page
    my_context.close()
    browser_context.close()