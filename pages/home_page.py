
class HomePage:

    def __init__(self, sb):
        self.sb = sb
        self.url = "https://practice-react.sdetunicorns.com/"
        self.search_icon = "button[class='search-active']"
        self.search_field = "input[type='text']"
        self.search_button = ".button-search"

    # homepage helper
    def open_home_page(self):
        self.sb.open(self.url)
        self.sb.maximize_window()

    # search item helper
    def search_for_item(self, item):
        self.open_home_page()
        self.sb.click(self.search_icon)
        self.sb.type(self.search_field, item)

    # navigation bar items helper
    def navigation_bar_items(self, expected_nav_items):
        self.open_home_page()
        for index, nav in enumerate(expected_nav_items, start=1):
            self.sb.assert_text(nav, f".main-menu li:nth-child({index})")


