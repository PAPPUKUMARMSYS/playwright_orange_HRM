import time
import pytest
import conftest

BASE_URL="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
user_data={'Username' : 'Admin','Password' : 'admin123'}

correct_user_data={'Username' : 'Admin','Password' : 'admin123'}
incorrect_user_data_01={'Username' : 'Admin01','Password' : 'admin123'}
incorrect_user_data_02={'Username' : 'Admin','Password' : 'admin1234'}


def test_assign_claim(setup):
    page=setup
    page.goto(BASE_URL)
    page.get_by_placeholder("Username").fill(user_data['Username'])
    page.get_by_placeholder("Password").fill(user_data['Password'])
    page.locator("//button[@type='submit']").click()
    page.get_by_text("Claim").click()
    page.get_by_role("link",name="Employee Claims").click
    page.get_by_role("button",name=" Assign Claim ").click


def test_login_with_correct_cred(setup):
    page=setup
    page.goto(BASE_URL)
    page.get_by_placeholder("Username").fill(correct_user_data['Username'])
    page.get_by_placeholder("Password").fill(correct_user_data['Password'])
    page.locator("//button[@type='submit']").click()
    page.locator("//p[@class='oxd-userdropdown-name']").click()
    text1=page.locator("//a[@role='menuitem' and (text()='Logout')]").inner_text()
    if text1=='Logout':
        assert True
    else:
        assert False


def test_login_with_incorrect_cred_01(setup):
    page= setup
    page.goto(BASE_URL)
    page.get_by_placeholder("Username").fill(incorrect_user_data_01['Username'])
    page.get_by_placeholder("Password").fill(incorrect_user_data_01['Password'])
    page.locator("//button[@type='submit']").click()
    text1= page.locator("//p[text()='Invalid credentials']").inner_text()
    if text1=='Invalid credentials':
        assert True
    else:
        assert False


def test_login_with_incorrect_cred_02(setup):
    page = setup
    page.goto(BASE_URL)
    page.get_by_placeholder("Username").fill(incorrect_user_data_02['Username'])
    page.get_by_placeholder("Password").fill(incorrect_user_data_02['Password'])
    page.locator("//button[@type='submit']").click()
    text1 = page.locator("//p[text()='Invalid credentials']").inner_text()
    if text1 == 'Invalid credentials':
        assert True
    else:
        assert False

