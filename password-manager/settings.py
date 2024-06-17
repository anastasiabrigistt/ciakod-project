import os

from PySide6 import QtWidgets, QtGui, QtCore
from dotenv import load_dotenv

from lib import sql, crypto
from lib.resource import resource_path
from ui.settings_form import Ui_settingsDialog
from master import MasterDialog


def change_master():
    master = MasterDialog(new=True)
    master.setWindowIcon(QtGui.QIcon(resource_path('files/icon.ico')))
    master.exec()


class SettingsDialog(QtWidgets.QDialog, Ui_settingsDialog):
    def __init__(self):
        super().__init__()
        self.tried = False
        self.setupUi(self)
        self.masterButton.clicked.connect(change_master)
        self.masterButton.setIcon(QtGui.QIcon(resource_path('files/key.png')))
        self.masterButton.setIconSize(QtCore.QSize(24, 24))
        self.resetButton.clicked.connect(self.reset)
        self.resetButton.setIcon(QtGui.QIcon(resource_path('files/reset.png')))
        self.resetButton.setIconSize(QtCore.QSize(24, 24))

    def reset(self):
        reply = QtWidgets.QMessageBox.question(
            self, 'Подтверждение удаления',
            'Вы действительно хотите сбросить базу паролей?',
            QtWidgets.QMessageBox.StandardButton.Yes |
            QtWidgets.QMessageBox.StandardButton.No

        )
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            load_dotenv()
            sql.truncate()
            password = os.getenv('MASTER_PASSWORD')
            key = crypto.generate_key()
            with open('.env', 'w') as file:
                file.write(f"MASTER_PASSWORD='{password}'\n"
                           f"KEY='{key}'")
            QtWidgets.QMessageBox.information(
                self, 'Успех', 'База паролей успешно очищена.'
            )
