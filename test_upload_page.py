import os.path

from seleniumbase import BaseCase

class TestUploadPage(BaseCase):

    def test_single_upload(self):
        url = "https://practice-react.sdetunicorns.com/upload"
        self.open(url)

        # file path
        file_path = os.path.abspath("data/some_image.png")
        print(file_path)

        # file input selector
        file_input = ".single input"
        # upload file selector
        self.choose_file(file_input, file_path)
        self.sleep(5)
        # # verify preview
        self.assert_element(".preview img")

        self.click('.btn.btn-primary')

        self.assert_text_visible("Image uploaded successfully")

    def test_upload_multiple_files(self):
        url = "https://practice-react.sdetunicorns.com/upload"
        self.open(url)

        file_path1 = os.path.abspath("data/some_image.png")
        file_path2 = os.path.abspath("data/some_image_1.png")

        multiple_files = f"{file_path1}\n{file_path2}"
        print(multiple_files)
        file_input_selector = ".multiple input"
        self.choose_file(file_input_selector, multiple_files)
        self.assert_element(".preview")

        self.click(".btn.btn-primary")
        self.assert_text_visible("Images   uploaded successfully")


