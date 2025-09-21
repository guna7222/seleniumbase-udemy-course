from seleniumbase import BaseCase

class TestAboutPage(BaseCase):

    def test_verify_about_page_who_are_we_text(self):
        url = "https://practice-react.sdetunicorns.com/about"
        self.open(url)
        who_are_we = self.get_text(".welcome-content.text-center h5")
        self.assert_equal(who_are_we, "Who Are We")

    def test_assert_true(self):
        url = "https://practice-react.sdetunicorns.com/about"
        self.open(url)
        is_breadcrumb_visible = self.is_element_visible('.breadcrumb-content')
        self.assert_true(is_breadcrumb_visible)
        self.assert_true("Welcome To Practice React Site" in self.get_text(".welcome-content h1"))

    def test_assert_in(self):
        self.open("https://practice-react.sdetunicorns.com/about")
        text = self.get_text(".welcome-content h1")
        self.assert_in("Welcome", text)

    def test_free_delivery_price(self):
        url = "https://practice-react.sdetunicorns.com/about"
        self.open(url)
        free_delivery_text = self.get_text(".header-offer span")
        self.assert_not_equal("$0", free_delivery_text)
