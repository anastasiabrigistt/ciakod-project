import os

from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtGui import QPalette
from dotenv import load_dotenv

from lib import sql, crypto
from lib.resource import resource_path
from ui.settings_form import Ui_settingsDialog
from master import MasterDialog


def change_master():
    master = MasterDialog(new=True)
    if master.get_app_theme() == 'Dark':
        master.setWindowIcon(QtGui.QIcon(resource_path('files/Light/icon.ico')))
    else:
        master.setWindowIcon(QtGui.QIcon(resource_path('files/Dark/icon.ico')))

    master.exec()


class SettingsDialog(QtWidgets.QDialog, Ui_settingsDialog):
    def __init__(self):
        super().__init__()
        self.tried = False
        self.setupUi(self)
        if self.get_app_theme() == 'Dark':
            self.masterButton.setIcon(QtGui.QIcon(resource_path('files/Dark/key.png')))
            self.resetButton.setIcon(QtGui.QIcon(resource_path('files/Dark/reset.png')))
        else:
            self.masterButton.setIcon(QtGui.QIcon(resource_path('files/Light/key.png')))
            self.resetButton.setIcon(QtGui.QIcon(resource_path('files/Light/reset.png')))
        self.masterButton.clicked.connect(change_master)

        self.masterButton.setIconSize(QtCore.QSize(24, 24))
        self.resetButton.clicked.connect(self.reset)

        self.resetButton.setIconSize(QtCore.QSize(24, 24))

    def get_app_theme(self):
        palette = self.palette()
        window_color = palette.color(QPalette.ColorRole.Window)
        if str(window_color) == 'PySide6.QtGui.QColor.fromRgbF(0.117647, 0.117647, 0.117647, 1.000000)':
            return 'Dark'
        else:
            return 'Light'

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
