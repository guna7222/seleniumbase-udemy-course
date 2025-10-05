from sbase.steps import assert_attribute
from seleniumbase import BaseCase

class TestDemoPage(BaseCase):

    def test_input_slider(self):
        url = "https://seleniumbase.io/demo_page"
        self.open(url)
        # before state
        self.assert_attribute("#progressBar", "value", "60")
        # change the slider value
        self.set_value("#mySlider", "80")
        # after state
        self.assert_attribute("#progressBar", "value", "70")

    def test_dropdown(self):
        url = "https://seleniumbase.io/demo_page"
        self.open(url)
        # before state
        self.assert_attribute("#meterBar", "value", "0.25")

        # change the dropdown value
        self.select_option_by_index("#mySelect", 1)

        # after state
        self.assert_attribute("#meterBar", "value", "0.5")

    def test_checkbox(self):
        url = "https://seleniumbase.io/demo_page"
        self.open(url)
        # before state
        self.assert_element_not_visible("img[src='https://seleniumbase.io/cdn/img/sb_logo_tiny.png']")
        # is checkbox selected
        is_checkbox_selected = self.is_selected("#checkBox1")
        if not is_checkbox_selected:
            # click on checkbox
            self.click("#checkBox1")

        self.assert_element_visible("img[src='https://seleniumbase.io/cdn/img/sb_logo_tiny.png']")

    def test_iframe(self):
        url = "https://seleniumbase.io/demo_page"
        self.open(url)
        # switch to iframe
        self.switch_to_frame("#myFrame2")
        self.assert_text("iFrame Text", "h4")
        self.switch_to_default_content()

    def test_select_checkbox_inside_iframe(self):
        url = "https://seleniumbase.io/demo_page"
        self.open(url)
        # assertion checkbox element is not visible
        self.assert_element_not_visible("#checkBox6")
        # switch to iframe
        self.switch_to_frame("#myFrame3")

        # click on checkbox
        self.click("#checkBox6")
        # check is checked box selected
        self.assert_true(self.is_checked("#checkBox6")) # is_checked is_selected

        self.switch_to_default_content()
        self.assert_element("#progressLabel")

    def test_hover_dropdown(self):
        url = "https://seleniumbase.io/demo_page"
        self.open(url)
        # hover on hoverDropdown
        self.hover("#myDropdown")
        self.click("#dropOption3")
        self.assert_text("Link Three Selected", "h3" )