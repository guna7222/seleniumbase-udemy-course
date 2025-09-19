from seleniumbase import BaseCase

class TestHomePage(BaseCase):

    def test_verify_page_title_and_url(self):
        url = "https://practice-react.sdetunicorns.com/"
        # open home page
        self.open(url)
        # check the title
        # self.assert_title_contains("SDET Unicorns")
        self.assert_title("Practice with React | SDET Unicorns Test Site")
        # self.assert_url_contains("sdetunicorns")
        # check the URL
        self.assert_url("https://practice-reac.sdetunicorns.com/")
