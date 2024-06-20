import pyperclip as pc
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtGui import QPalette

from lib import sql
from lib.classes import Service
from lib.resource import resource_path
from passdial import PasswordDialog
from ui.element_form import Ui_Form


class ElementWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, service: Service):
        super().__init__()
        self.pass_visible = False
        self.service = service
        self.setupUi(self)
        self.setup_controls()
        self.load_data()

    def setup_controls(self):
        if self.get_app_theme() == 'Dark':
            self.pushButton.setIcon(QtGui.QIcon(resource_path('files/Dark/show.png')))
            self.pushButton_2.setIcon(QtGui.QIcon(resource_path('files/Dark/copy.png')))
            self.pushButton_3.setIcon(QtGui.QIcon(resource_path('files/Dark/edit.png')))
            self.pushButton_4.setIcon(QtGui.QIcon(resource_path('files/Dark/delete.png')))
        else:
            self.pushButton.setIcon(QtGui.QIcon(resource_path('files/Light/show.png')))
            self.pushButton_2.setIcon(QtGui.QIcon(resource_path('files/Light/copy.png')))
            self.pushButton_3.setIcon(QtGui.QIcon(resource_path('files/Light/edit.png')))
            self.pushButton_4.setIcon(QtGui.QIcon(resource_path('files/Light/delete.png')))
        self.pushButton.clicked.connect(self.reveal)

        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_2.clicked.connect(self.copy)

        self.pushButton_2.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_3.clicked.connect(self.edit)

        self.pushButton_3.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_4.clicked.connect(self.delete)

        self.pushButton_4.setIconSize(QtCore.QSize(24, 24))

    def reveal(self):
        self.pass_visible = not self.pass_visible
        if self.get_app_theme() == 'Dark':
            self.pushButton.setIcon(QtGui.QIcon(
                resource_path('files/Dark/hide.png') if self.pass_visible
                else resource_path('files/Dark/show.png')
            ))
        else:
            self.pushButton.setIcon(QtGui.QIcon(
                resource_path('files/Light/hide.png') if self.pass_visible
                else resource_path('files/Light/show.png')
            ))
        self.load_data()

    def copy(self):
        pc.copy(self.service.password)

    def edit(self):
        dialog = PasswordDialog(self.service)
        if self.get_app_theme() == 'Dark':
            dialog.setWindowIcon(QtGui.QIcon(resource_path('files/Light/icon.ico')))
        else:
            dialog.setWindowIcon(QtGui.QIcon(resource_path('files/Light/icon.ico')))
        dialog.exec()
        el = sql.get_by_id(self.service.id)
        self.service = Service(int(el[0]), el[1], el[2], el[3], el[4])
        self.load_data()

    def get_app_theme(self):
        palette = self.palette()
        window_color = palette.color(QPalette.ColorRole.Window)
        if str(window_color) == 'PySide6.QtGui.QColor.fromRgbF(0.117647, 0.117647, 0.117647, 1.000000)':
            return 'Dark'
        else:
            return 'Light'

    def delete(self):
        reply = QtWidgets.QMessageBox.question(
            self, 'Подтверждение удаления',
            'Вы действительно хотите удалить этот пароль?',
            QtWidgets.QMessageBox.StandardButton.Yes |
            QtWidgets.QMessageBox.StandardButton.No

        )
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            sql.delete_data(self.service.id)
            self.hide()

    def load_data(self):
        self.serviceLabel.setText(self.service.service)
        self.loginLabel.setText(self.service.login)
        self.passLabel.setText(
            self.service.password if self.pass_visible else '********'
        )
