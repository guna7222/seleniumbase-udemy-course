
class AutomationExercisePage:

    def __init__(self, sb):
        self.sb = sb
        # selectors
        self.home_page = "li:nth-child(1) a:nth-child(1)"
        self.signup_login_button = "a[href='/login']"
        self.new_user_signup = "div[class='signup-form'] h2"
        self.signup_name = 'input[data-qa="signup-name"]'
        self.signup_email = 'input[data-qa="signup-email"]'
        self.signup_button = 'input[data-qa="signup-button"]'
        self.enter_account_information = "body > section:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h2:nth-child(1) > b:nth-child(1)"

    # page opening helper method
    def open(self):
        self.sb.open("http://automationexercise.com")
