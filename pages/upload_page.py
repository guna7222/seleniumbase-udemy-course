import os.path

class UploadPage:

    def __init__(self, sb):
        self.sb = sb
        self.file_input_selector = ".single input"
        self.verify_preview = ".preview img"
        self.upload_button = ".btn.btn-primary"
        self.url = "https://practice-react.sdetunicorns.com/upload"
        self.multiple_files_selector = ".multiple input"
        self.preview_multiple = ".preview"

    # page helper
    def open_upload_page(self):
        self.sb.open(self.url)

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

