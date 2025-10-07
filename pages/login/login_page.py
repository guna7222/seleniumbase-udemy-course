from config.default import LOGIN_PAGE_URL

class LoginPage:
    def __init__(self, sb):
        self.sb = sb
        # locators
        self.username = '#username'
        self.password = '#password'
        self.login_button = 'button[type="submit"]'
        self.login_success_message = '#flash'
        self.logout_button = ".icon-2x.icon-signout"
        self.login_username_wrong = '#flash'


    def open_login_page(self):
        self.sb.open(LOGIN_PAGE_URL)
