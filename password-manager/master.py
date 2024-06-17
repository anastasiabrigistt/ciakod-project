import hashlib
import os

from PySide6 import QtWidgets
from dotenv import load_dotenv

import lib.crypto as crypto
from lib import sql
from ui.master_form import Ui_Dialog

env = load_dotenv()


class MasterDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, new=False):
        super().__init__()
        self.tried = False
        self.new = new
        self.setupUi(self)
        self.setup_form()
        self.pushButton.clicked.connect(self.login)

    def setup_form(self):
        if not self.new:
            self.newLabel.setVisible(False)
            self.newEdit.setVisible(False)
        else:
            self.pushButton.setText('Изменить')
        if not env:
            self.label.setText(
                '<p style="font-size: 14px;">'
                'Придумайте мастер пароль для входа в приложение:</p>'
            )

    def login(self):
        if not self.new:
            password = hashlib.sha256(self.passEdit.text().encode()).hexdigest()
            if env:
                if os.getenv('MASTER_PASSWORD') == password:
                    self.accept()
                else:
                    self.tried = True
                    self.reject()
            else:
                if not os.path.exists('db.sqlite3'):
                    sql.create_db()
                sql.truncate()
                key = crypto.generate_key()
                with open('.env', 'w') as file:
                    file.write(f"MASTER_PASSWORD='{password}'\n"
                               f"KEY='{key}'")
                self.accept()
        else:
            password = hashlib.sha256(
                self.passEdit.text().encode()
            ).hexdigest()
            if os.getenv('MASTER_PASSWORD') == password:
                if self.newEdit.text():
                    new_password = hashlib.sha256(
                        self.newEdit.text().encode()
                    ).hexdigest()
                    key = os.getenv('KEY')
                    with open('.env', 'w') as file:
                        file.write(f"MASTER_PASSWORD='{new_password}'\n"
                                   f"KEY='{key}'")
                    QtWidgets.QMessageBox.information(
                        self, 'Успех', 'Мастер-пароль успешно изменён.'
                    )
                    self.accept()
                else:
                    QtWidgets.QMessageBox.warning(
                        self, 'Ошибка', 'Введите новый пароль!'
                    )
            else:
                QtWidgets.QMessageBox.warning(
                    self, 'Ошибка', 'Неверный Мастер-пароль!'
                )
