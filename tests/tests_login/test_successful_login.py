from sbase.steps import assert_url
from seleniumbase import BaseCase
from pages.login.login_page import LoginPage
from config.default import LOGIN_PAGE_URL
from utils.path import get_project_path
import json
class TestLoginSuccessful(BaseCase):

    """
    Test Case 1: Successful Login
    Launch the  browser.
    Navigate to the login page URL.
    Verify that the login page is displayed successfully.
    Enter Username: practice.
    Enter Password: SuperSecretPassword!.
    Click the Login button.
    Verify that the user is redirected to the /secure page.
    Confirm the success message "You logged into a secure area!" is visible.
    Verify that a Logout button is displayed.
    """
    def setUp(self):
        super().setUp()
        self.login_page_object = LoginPage(self)
        self.login_page_object.open_login_page()

        with open(get_project_path("data", "test_data.json")) as f:
            login_data = json.load(f)

        self.user = login_data["login_successful_test_data"][0]["username"]
        self.pwd = login_data["login_successful_test_data"][0]["password"]
        self.wrong_username = login_data["login_successful_test_data"][1]["username"]

    def test_login_successful(self):
        # Verify that the login page is displayed successfully.
        self.assert_url(LOGIN_PAGE_URL)
        #Enter Username: practice. Enter Password: SuperSecretPassword!.
        self.type(self.login_page_object.username, self.user)
        self.type(self.login_page_object.password, self.pwd)
        #Click the Login button.
        self.click(self.login_page_object.login_button)
        self.assert_element_visible(self.login_page_object.login_success_message)
        # verify that a Logout button is displayed.
        self.assert_element_visible(self.login_page_object.logout_button)

    def test_invalid_username(self):
        # Verify that the login page is displayed successfully.
        self.assert_url(LOGIN_PAGE_URL)
        # Enter Username: practice. Enter Password: SuperSecretPassword!.
        self.type(self.login_page_object.username, self.wrong_username)
        self.type(self.login_page_object.password, self.pwd)
        # Click the Login button.
        self.click(self.login_page_object.login_button)
        self.assert_element_visible(self.login_page_object.login_username_wrong)
        self.assert_text("Your password is invalid!", self.login_page_object.login_username_wrong)
        self.assert_url_contains("login")