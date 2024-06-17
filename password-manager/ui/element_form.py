# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'element.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(579, 101)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        font.setPointSize(12)
        Form.setFont(font)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.serviceLabel = QLabel(self.frame)
        self.serviceLabel.setObjectName(u"serviceLabel")
        self.serviceLabel.setMinimumSize(QSize(0, 20))

        self.gridLayout_2.addWidget(self.serviceLabel, 0, 0, 1, 1)

        self.passLabel = QLabel(self.frame)
        self.passLabel.setObjectName(u"passLabel")
        self.passLabel.setMinimumSize(QSize(0, 20))

        self.gridLayout_2.addWidget(self.passLabel, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 20))
        icon = QIcon(QIcon.fromTheme(u"system-search"))
        self.pushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditCopy))
        self.pushButton_2.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        self.pushButton_3.setIcon(icon2)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.pushButton_4.setIcon(icon3)

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 2, 1)

        self.loginLabel = QLabel(self.frame)
        self.loginLabel.setObjectName(u"loginLabel")
        self.loginLabel.setMinimumSize(QSize(0, 20))

        self.gridLayout_2.addWidget(self.loginLabel, 1, 0, 2, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.serviceLabel.setText(QCoreApplication.translate("Form", u"Service", None))
        self.passLabel.setText(QCoreApplication.translate("Form", u"Pass", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.loginLabel.setText(QCoreApplication.translate("Form", u"Login", None))
    # retranslateUi

