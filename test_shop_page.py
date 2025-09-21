from seleniumbase import BaseCase

class TestShopPage(BaseCase):


    def test_verify_all_categories_after_clicking_on_products(self):
       url = "https://practice-react.sdetunicorns.com/shop-grid-standard"
       self.open(url)
       expected_categories = ["All Categories", "Laptop", "Electronics", "Keyboard"]
       for index, category in enumerate(expected_categories, start=1):
           self.assert_text(category, f".sidebar-widget-list.mt-30 li:nth-child({index})")