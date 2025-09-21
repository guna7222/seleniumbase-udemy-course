from sbase.steps import assert_attribute
from seleniumbase import BaseCase

class TestContactPage(BaseCase):

    def test_get_in_touch_form_is_successfully_submitting(self):
        url = "https://practice-react.sdetunicorns.com/contact"
        self.open(url)
        self.type('input[placeholder="Name*"]', "test1")
        self.type('input[placeholder="Email*"]', "test1@gmail.com")
        self.type('input[placeholder="Subject*"]', "Tesing")
        self.type('textarea[placeholder="Your Message*"]', "Good to see testing is in progress")
        # click on send button
        self.click(".submit")
        # verify success message after submitting the form
        self.assert_text("Message sent successflly", ".react-toast-notifications__toast__content.css-1ad3zal")