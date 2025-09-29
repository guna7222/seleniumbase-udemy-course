from seleniumbase import BaseCase
from pages.home_page import HomePage


class TestHomePage(BaseCase):

    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self)
        self.home_page.open_home_page()

    def test_verify_page_title_and_url(self):
        # check the title
        # self.assert_title_contains("SDET Unicorns")
        self.assert_title("Practice with React | SDET Unicorns Test Site")
        # self.assert_url_contains("sdetunicorns")
        # check the URL
        self.assert_url("https://practice-reac.sdetunicorns.com/")

    def test_search_for_products_and_verify_the_text(self):

        self.home_page.search_for_item("Lenovo")

    def test_2_position_is_products_or_not_in_the_navigation(self):
        expected_nav_products = ["Home", "Products", "About Us", "Contact", "Upload"]
        self.home_page.navigation_bar_items(expected_nav_products)

    def test_about_us_page_url(self):

        self.click(self.home_page.about_position)
        self.assert_url_contains("about")

    def test_new_tab(self):
        self.click(".copyright.mb-30 p a")
        print(self.driver.window_handles)  # return list of tabs
        self.switch_to_tab(1)
        print(self.driver.window_handles)
        self.assert_url("https://sdetunicorns.com/")
        self.switch_to_default_tab()
        self.assert_url("https://practice-react.sdetunicorns.com/")
