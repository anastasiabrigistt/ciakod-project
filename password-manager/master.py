import hashlib
import os

from PySide6 import QtWidgets, QtGui
from PySide6.QtGui import QPalette
from dotenv import load_dotenv

import lib.crypto as crypto
from lib import sql
from lib.resource import resource_path
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
        if self.get_app_theme() == 'Dark':
            self.setWindowIcon(QtGui.QIcon(resource_path('files/Light/icon.ico')))
        else:
            self.setWindowIcon(QtGui.QIcon(resource_path('files/Dark/icon.ico')))
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

    def get_app_theme(self):
        palette = self.palette()
        window_color = palette.color(QPalette.ColorRole.Window)
        if str(window_color) == 'PySide6.QtGui.QColor.fromRgbF(0.117647, 0.117647, 0.117647, 1.000000)':
            return 'Dark'
        else:
            return 'Light'

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
