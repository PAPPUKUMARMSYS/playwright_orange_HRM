import time
from playwright.sync_api import Playwright

user_data={'Username' : 'Admin','Password' : 'admin123'}
def test_login(playwright:Playwright):
    page=playwright.chromium.launch(headless=False)
    page=page.new_context()
    page=page.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill(user_data['Username'])
    page.get_by_placeholder("Password").fill(user_data['Password'])
    page.locator("//button[@type='submit']").click()

    page.get_by_text("Claim").click()
    page.get_by_role("link",name="Employee Claims").click
    page.get_by_role("button",name=" Assign Claim ").click
    page.get_by_placeholder("Type for hints...").fill("Pappu kumar")
    time.sleep(5)