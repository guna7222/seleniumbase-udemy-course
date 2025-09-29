import os.path

from seleniumbase import BaseCase
from pages.upload_page import UploadPage
from utils.path import get_project_path

class TestUploadPage(BaseCase):

    def setUp(self):
        super().setUp(self)
        self.upload_page = UploadPage(self)
        self.upload_page.open_upload_page()

    def test_single_upload(self):
        self.upload_page.upload_single_file()
        self.assert_text_visible("Image uploaded successfully")

    def test_upload_multiple_files(self):

        # file paths
        file_path1 = get_project_path("data","some_image.png")
        file_path2 = get_project_path("data", "some_image_1.png")
        multiple_files = f"{file_path1}\n{file_path2}"
        print(multiple_files)

        file_input_selector = self.upload_page.multiple_files_selector
        self.choose_file(file_input_selector, multiple_files)
        self.assert_element(self.upload_page.preview_multiple)

        self.click(self.upload_page.upload_button)
        self.assert_text_visible("Images uploaded successfully")
