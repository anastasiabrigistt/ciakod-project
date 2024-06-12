from PySide6 import QtWidgets

import lib.strong_password as strong_password
import lib.sql as sql
from pass_form import Ui_PasswordDialog
from classes import Service


class PasswordDialog(QtWidgets.QDialog, Ui_PasswordDialog):
    def __init__(self, service: Service, parent=None):
        super().__init__()
        self.setupUi(self)
        self.service = service
        self.genButton.clicked.connect(self.generate)
        self.saveButton.clicked.connect(self.save)
        self.passEdit.textChanged.connect(self.check)
        self.fill_info()

    def generate(self):
        self.passEdit.setText(strong_password.generate_password())

    def check(self):
        level, comments = strong_password.check_password_strength(
            self.passEdit.text()
        )
        self.label_4.setText(
            f'{level}: {comments}'
        )

    def fill_info(self):
        self.serviceEdit.setText(self.service.service)
        self.loginEdit.setText(self.service.login)
        self.passEdit.setText(self.service.password)
        if self.service.id >= 0:
            self.setWindowTitle(
                f'Редактировать: {self.service.service} / {self.service.login}'
            )
        else:
            self.setWindowTitle('Добавить аккаунт')

    def save(self):
        if self.service.id >= 0:
            sql.update_data(
                self.service.id,
                self.serviceEdit.text(),
                self.loginEdit.text(),
                self.passEdit.text(),
            )
        else:
            sql.insert_data(
                self.service.category,
                self.serviceEdit.text(),
                self.loginEdit.text(),
                self.passEdit.text(),
            )
        self.accept()