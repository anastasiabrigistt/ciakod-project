import sys

from PySide6 import QtWidgets, QtGui, QtCore

from lib.resource import resource_path
import lib.sql as sql
from element import ElementWidget
from lib.classes import Service
from master import MasterDialog
from passdial import PasswordDialog
from settings import SettingsDialog
from ui.main_form import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.category = 'web'
        self.on_top = False
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint, True)
        self.services = []
        self.setup_controls()
        self.master_password()
        self.load_data()
        screen_geometry = QtWidgets.QApplication.primaryScreen().geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        window_width = self.width()
        window_height = self.height()
        x = screen_width - window_width
        y = screen_height - window_height - 45
        self.move(x, y)

    def setup_controls(self):
        self.addButton.clicked.connect(self.add)
        self.addButton.setIcon(QtGui.QIcon(resource_path('files/add.png')))
        self.addButton.setIconSize(QtCore.QSize(24, 24))
        self.webButton.clicked.connect(lambda _: self.filter('web'))
        self.appsButton.clicked.connect(lambda _: self.filter('apps'))
        self.otherButton.clicked.connect(lambda _: self.filter('other'))
        self.settingsButton.clicked.connect(self.settings)
        self.settingsButton.setIcon(QtGui.QIcon(resource_path('files/settings.png')))
        self.settingsButton.setIconSize(QtCore.QSize(24, 24))
        self.searchEdit.textChanged.connect(self.load_data)
        self.ontop_button.clicked.connect(self.stay_on_top)
        self.ontop_button.setIcon(QtGui.QIcon(resource_path('files/keep.png')))
        self.ontop_button.setIconSize(QtCore.QSize(24, 24))
        self.closeButton.clicked.connect(sys.exit)

    def settings(self):
        dialog = SettingsDialog()
        dialog.setWindowIcon(QtGui.QIcon(resource_path('files/icon.ico')))
        dialog.exec()
        self.load_data()

    def add(self):
        service = Service()
        service.category = self.category
        dialog = PasswordDialog(service)
        dialog.setWindowIcon(QtGui.QIcon(resource_path('files/icon.ico')))
        dialog.exec()
        self.load_data()

    def filter(self, page):
        self.webButton.setMinimumSize(0, 50 * (page == 'web'))
        self.appsButton.setMinimumSize(0, 50 * (page == 'apps'))
        self.otherButton.setMinimumSize(0, 50 * (page == 'other'))
        self.category = page
        self.load_data()

    def master_password(self):
        master = MasterDialog()
        master.setWindowIcon(QtGui.QIcon(resource_path('files/icon.ico')))
        status = master.exec()
        while status != QtWidgets.QDialog.DialogCode.Accepted:
            if not master.tried:
                sys.exit()
            QtWidgets.QMessageBox.warning(
                self, 'Ошибка', 'Неверный Мастер-пароль!'
            )
            master.tried = False
            status = master.exec()

    def load_data(self):
        while self.passBox.count():
            item = self.passBox.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.passBox.removeItem(item)
        data = sql.get_all_data(self.searchEdit.text())
        self.services = []
        for el in data:
            self.services.append(
                Service(int(el[0]), el[1], el[2], el[3], el[4])
            )
        for service in self.services:
            if service.category == self.category:
                self.passBox.addWidget(ElementWidget(service))

    def stay_on_top(self):
        self.on_top = not self.on_top
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, self.on_top)

        self.ontop_button.setIcon(QtGui.QIcon(
            resource_path('files/keep_off.png') if self.on_top
            else resource_path('files/keep.png')
        ))
        self.show()
        self.raise_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowIcon(QtGui.QIcon(resource_path('files/icon.ico')))
    window.show()
    sys.exit(app.exec())
