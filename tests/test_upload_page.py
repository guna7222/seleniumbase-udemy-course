import os.path

from seleniumbase import BaseCase
from pages.upload_page import UploadPage


class TestUploadPage(BaseCase):

    def test_single_upload(self):
        upload_page = UploadPage(self)
        upload_page.open_upload_page()
        upload_page.upload_single_file()
        self.assert_text_visible("Image uploaded successfully")

    def test_upload_multiple_files(self):
        upload_page = UploadPage(self)
        upload_page.open_upload_page()
        # file paths
        file_path1 = os.path.abspath("../data/some_image.png")
        file_path2 = os.path.abspath("../data/some_image_1.png")
        multiple_files = f"{file_path1}\n{file_path2}"
        print(multiple_files)

        file_input_selector = upload_page.multiple_files_selector
        self.choose_file(file_input_selector, multiple_files)
        self.assert_element(upload_page.preview_multiple)

        self.click(upload_page.upload_button)
        self.assert_text_visible("Images uploaded successfully")