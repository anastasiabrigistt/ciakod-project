import hashlib
import os

from PySide6 import QtWidgets

from master_form import Ui_Dialog

filename = 'app.bin'


class MasterDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)

    def login(self):
        password = hashlib.sha256(self.passEdit.text().encode()).hexdigest()
        if os.path.exists(filename):
            with open(filename, "rb") as file:
                file_content = file.read().decode('utf-8')
            if file_content == password:
                self.accept()
            else:
                self.reject()
        else:
            with open(filename, "wb") as file:
                file.write(password.encode('utf-8'))
            self.accept()
