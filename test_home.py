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


    def test_search_for_products_and_verify_the_text(self):
        url = "https://practice-react.sdetunicorns.com/"
        self.open(url)
        # click on search icon
        self.click("button[class='search-active']")

        # enter text in search field
        self.type("input[type='text']", "Lenovo")

        # click on search button
        self.click(".button-search")

        # verify the text
        self.assert_text_visible("Showing Results for Lenovo")
        
    def test_2_position_is_products_or_not_in_the_navigation(self):
        url = "https://practice-react.sdetunicorns.com/"
        self.open(url)
        # verify the position of products in the navigation bar
        self.assert_text("Products", ".main-menu li:nth-child(2)")
        expected_nav_products = ["Home", "Products", "About Us", "Contact", "Upload"]
        for index, nav in enumerate(expected_nav_products, start=1):
            self.assert_text(nav, f".main-menu li:nth-child({index})")

    def test_about_us_page_url(self):
        # go to about us page
        # Verify url contains About
        url = "https://practice-react.sdetunicorns.com/"
        self.open(url)
        self.click('.main-menu li:nth-child(3)')
        self.assert_url_contains("bout")

