# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 600)
        MainWindow.setMinimumSize(QSize(400, 600))
        MainWindow.setMaximumSize(QSize(400, 800))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI Light"])
        font1.setPointSize(18)
        self.label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.closeButton = QPushButton(self.centralwidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setStyleSheet(u"background-color: transparent;\n"
"hover: {\n"
"	background-color: rgb(100,100,100)\n"
"}")
        icon = QIcon()
        if QIcon.hasThemeIcon(QIcon.ThemeIcon.ApplicationExit):
            icon = QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.closeButton.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.webButton = QPushButton(self.centralwidget)
        self.webButton.setObjectName(u"webButton")
        self.webButton.setMinimumSize(QSize(0, 50))
        self.webButton.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.webButton)

        self.appsButton = QPushButton(self.centralwidget)
        self.appsButton.setObjectName(u"appsButton")

        self.horizontalLayout.addWidget(self.appsButton)

        self.otherButton = QPushButton(self.centralwidget)
        self.otherButton.setObjectName(u"otherButton")

        self.horizontalLayout.addWidget(self.otherButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 378, 433))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.passBox = QVBoxLayout()
        self.passBox.setObjectName(u"passBox")

        self.verticalLayout_3.addLayout(self.passBox)

        self.verticalSpacer_3 = QSpacerItem(20, 372, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setMinimumSize(QSize(40, 40))
        self.addButton.setMaximumSize(QSize(16777215, 16777215))
        icon1 = QIcon()
        if QIcon.hasThemeIcon(QIcon.ThemeIcon.ListAdd):
            icon1 = QIcon.fromTheme(QIcon.ThemeIcon.ListAdd)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.addButton.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.addButton)

        self.settingsButton = QPushButton(self.centralwidget)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setMinimumSize(QSize(40, 40))
        self.settingsButton.setMaximumSize(QSize(16777215, 16777215))
        icon2 = QIcon()
        if QIcon.hasThemeIcon(QIcon.ThemeIcon.DocumentProperties):
            icon2 = QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.settingsButton.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.settingsButton)

        self.ontop_button = QPushButton(self.centralwidget)
        self.ontop_button.setObjectName(u"ontop_button")
        self.ontop_button.setMinimumSize(QSize(40, 40))

        self.horizontalLayout_4.addWidget(self.ontop_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.searchEdit = QLineEdit(self.centralwidget)
        self.searchEdit.setObjectName(u"searchEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.searchEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Z Password Manager", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Z Password Manager", None))
        self.closeButton.setText("")
#if QT_CONFIG(whatsthis)
        self.webButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.webButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0430\u0439\u0442\u044b", None))
        self.appsButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
        self.otherButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0443\u0433\u043e\u0435", None))
        self.addButton.setText("")
        self.settingsButton.setText("")
        self.ontop_button.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
    # retranslateUi

