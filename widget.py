# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from urllib.parse import urlparse
from mega_script.megafetch import fetch_mega_link
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


        # connections
        self.ui.get_pixeldrain.clicked.connect(self.get_pixeldrain_command)
        self.ui.get_mega.clicked.connect(self.get_mega_command)

    def get_pixeldrain_command(self):

        parsed_url = urlparse(self.ui.input_pixeldrain.text())

        last_path_segment = parsed_url.path.split('/')[-1]

        if self.ui.input_pixeldrain.text():
            new_link = f"https://pixeldrain.com/api/file/{last_path_segment}"
            command = f"curl -O {new_link}"
        else:
            command = "please fill url link and try again..."

        self.ui.output_command.setPlainText(command)


    def get_google_drive_command(self):
        pass

    # for fech data from mega used one script on ./mega_script folder
    def get_mega_command(self):

        url = self.ui.input_mega.text()

        if url:
            file_url, file_name, hex_output, raw_hex_iv = fetch_mega_link(url)

            self.ui.output_command.setPlainText(f"wget -O - {file_url} | openssl enc -d -aes-128-ctr -K {hex_output} -iv {raw_hex_iv} > file.name.new && mv -f file.name.new '{file_name}'")
        else:
            command = "please fill url link and try again..."
            self.ui.output_command.setPlainText(command)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
