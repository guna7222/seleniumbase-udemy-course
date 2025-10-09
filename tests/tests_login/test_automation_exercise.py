from seleniumbase import BaseCase
from pages.login.automation_exercise_page import AutomationExercisePage

class TestAutomationExercise(BaseCase):

    # Register a new user
    """
    1. Launch browser
    2. Navigate to url 'http://automationexercise.com'
    3. Verify that home page is visible successfully
    4. Click on 'Signup / Login' button
    5. Verify 'New User Signup!' is visible
    6. Enter name and email address
    7. Click 'Signup' button
    8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    9. Fill details: Title, Name, Email, Password, Date of birth
    10. Select checkbox 'Sign up for our newsletter!'
    11. Select checkbox 'Receive special offers from our partners!'
    12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    13. Click 'Create Account button'
    14. Verify that 'ACCOUNT CREATED!' is visible
    15. Click 'Continue' button
    16. Verify that 'Logged in as username' is visible
    17. Click 'Delete Account' button
    18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    """
    def setUp(self):
        super().setUp()
        self.automation_exercise_page = AutomationExercisePage(self)
        self.automation_exercise_page.open()


    def test_register_user(self):
        # # Step 3: Verify that home page is visible successfully
        # self.home = self.get_text(self.automation_exercise_page.home_page)
        # print(self.home)
        # self.assert_text_visible(" Home", self.home)
        # 4. Click on 'Signup / Login' button
        self.click(self.automation_exercise_page.signup_login_button)
        # 5. Verify 'New User Signup!' is visible
        self.assert_text("New User Signup!", self.automation_exercise_page.new_user_signup)
        # 6. Enter name and email address
        self.type(self.automation_exercise_page.signup_name, "TestUser")
        self.type(self.automation_exercise_page.signup_email, "test@gmail.com")
        # 7. Click 'Signup' button
        self.click(self.automation_exercise_page.signup_button)
        # Further steps would continue here...
        # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
        self.assert_text_visible("ENTER ACCOUNT INFORMATION", self.automation_exercise_page.enter_account_information)