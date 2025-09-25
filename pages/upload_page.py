import os.path
from config.default import BASE_URl


class UploadPage:

    def __init__(self, sb):
        self.sb = sb
        self.file_input_selector = ".single input"
        self.verify_preview = ".preview img"
        self.upload_button = ".btn.btn-primary"
        self.multiple_files_selector = ".multiple input"
        self.preview_multiple = ".preview"

    # page helper
    def open_upload_page(self):
        self.sb.open(f"{BASE_URl}/upload")

    def upload_single_file(self):
        # file path
        file_path = os.path.abspath("../data/some_image.png")
        print(file_path)
        # file input selector
        file_input = self.file_input_selector
        # upload file selector
        self.sb.choose_file(file_input, file_path)
        # verify preview
        self.sb.assert_element(self.verify_preview)
        self.sb.click(self.upload_button)

