import sys

from PyQt5.QtWinExtras import QtWin
from PySide6 import QtWidgets, QtGui

from main_form import Ui_MainWindow
from master import MasterDialog
from passdial import PasswordDialog
from classes import Service
import lib.sql as sql



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.category = 'web'
        self.setup_controls()
        self.master_password()
        self.load_data()

    def setup_controls(self):
        self.addButton.clicked.connect(self.add)
        self.editButton.clicked.connect(self.edit)
        self.delButton.clicked.connect(self.delete)
        self.webButton.clicked.connect(lambda _: self.filter('web'))
        self.appsButton.clicked.connect(lambda _: self.filter('apps'))
        self.otherButton.clicked.connect(lambda _: self.filter('other'))
        self.listWidget.itemDoubleClicked.connect(self.edit)

    def add(self):
        service = Service()
        service.category = self.category
        dialog = PasswordDialog(service)
        dialog.exec()
        self.load_data()

    def edit(self):
        pass

    def delete(self):
        pass

    def filter(self, page):
        self.category = page
        self.load_data()

    def master_password(self):
        master = MasterDialog()
        status = master.exec()
        while status != QtWidgets.QDialog.DialogCode.Accepted:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Неверный Мастер-пароль!'
            )
            status = master.exec()

    def load_data(self):
        self.listWidget.clear()
        data = sql.get_all_data()
        for i in data:
            if i[1] == self.category:
                self.listWidget.addItem(f'{i[0]}) {i[2]} / {i[3]}')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myappid = 'z.passmanager.1'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
    window = MainWindow()
    window.setWindowIcon(QtGui.QIcon('files/icon.ico'))
    window.show()
    sys.exit(app.exec())

