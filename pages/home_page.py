from config.default import BASE_URl

class HomePage:

    def __init__(self, sb):
        self.sb = sb
        self.search_icon = "button[class='search-active']"
        self.search_field = "input[type='text']"
        self.search_button = ".button-search"
        self.about_position = '.main-menu li:nth-child(3)'

    # homepage helper
    def open_home_page(self):
        self.sb.open(BASE_URl)
        self.sb.maximize_window()

    # search item helper
    def search_for_item(self, item):
        self.open_home_page()
        self.sb.click(self.search_icon)
        self.sb.type(self.search_field, item)
        # verify the text
        self.sb.assert_text_visible("Showing Results for Lenovo")

    # navigation bar items helper
    def navigation_bar_items(self, expected_nav_items):
        self.open_home_page()
        for index, nav in enumerate(expected_nav_items, start=1):
            self.sb.assert_text(nav, f".main-menu li:nth-child({index})")


