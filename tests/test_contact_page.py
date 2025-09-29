from seleniumbase import BaseCase
from parameterized import parameterized


class TestContactPage(BaseCase):

    # unit testing style
    @parameterized.expand([(
        "test2",
        "test2@gmail.com",
        "testing with different username",
        "this should work fine"
    ),
    ])
    def test_get_in_touch_form_is_successfully_submitting_param(self, name, email, subject, message):
        url = "https://practice-react.sdetunicorns.com/contact"
        self.open(url)
        self.type('input[placeholder="Name*"]', name)
        self.type('input[placeholder="Email*"]', email)
        self.type('input[placeholder="Subject*"]', subject)
        self.type('textarea[placeholder="Your Message*"]', message)
        # click on send button
        self.click(".submit")
        # verify success message after submitting the form
        self.assert_text("Message sent successflly", ".react-toast-notifications__toast__content.css-1ad3zal")
        self.assert_element_not_visible('[class*="error"]')

    # @pytest.mark.parametrize( "name,email,subject,message",
    # [
    #     ("test2","test2@gmail.com","testing with different username","this should work fine"),
    #     ("john", "john@gmail.com", "subject line", "another message"),
    # ],
    #                           )
    # def test_get_in_touch_form_is_successfully_submitting_param_pytest(self, name, email, subject, message):
    #     url = "https://practice-react.sdetunicorns.com/contact"
    #     self.open(url)
    #     self.type('input[placeholder="Name*"]', name)
    #     self.type('input[placeholder="Email*"]', email)
    #     self.type('input[placeholder="Subject*"]', subject)
    #     self.type('textarea[placeholder="Your Message*"]', message)
    #     # click on send button
    #     self.click(".submit")
    #     # verify success message after submitting the form
    #     self.assert_text("Message sent successflly", ".react-toast-notifications__toast__content.css-1ad3zal")
    #     self.assert_element_not_visible('[class*="error"]')

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
        self.assert_element_not_visible('[class*="error"]')

    def test_submit_get_in_touch_form_with_out_input(self):
        self.open("https://practice-react.sdetunicorns.com/contact")
        self.click(".submit")
        errors = self.find_elements('[class*="error"]')
        self.assert_equal(len(errors), 4)
        