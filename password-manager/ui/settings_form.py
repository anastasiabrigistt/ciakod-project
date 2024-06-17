# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        if not settingsDialog.objectName():
            settingsDialog.setObjectName(u"settingsDialog")
        settingsDialog.resize(500, 400)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        font.setPointSize(12)
        settingsDialog.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(settingsDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(settingsDialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(16)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalFrame = QFrame(settingsDialog)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.masterButton = QPushButton(self.verticalFrame)
        self.masterButton.setObjectName(u"masterButton")
        self.masterButton.setMinimumSize(QSize(250, 40))

        self.verticalLayout.addWidget(self.masterButton)

        self.resetButton = QPushButton(self.verticalFrame)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setMinimumSize(QSize(250, 40))

        self.verticalLayout.addWidget(self.resetButton)


        self.horizontalLayout.addWidget(self.verticalFrame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_2 = QLabel(settingsDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)


        self.retranslateUi(settingsDialog)

        QMetaObject.connectSlotsByName(settingsDialog)
    # setupUi

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(QCoreApplication.translate("settingsDialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("settingsDialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.masterButton.setText(QCoreApplication.translate("settingsDialog", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u041c\u0430\u0441\u0442\u0435\u0440-\u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.resetButton.setText(QCoreApplication.translate("settingsDialog", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0431\u0430\u0437\u0443 \u043f\u0430\u0440\u043e\u043b\u0435\u0439", None))
        self.label_2.setText(QCoreApplication.translate("settingsDialog", u"Z Password Manager v.1.0", None))
    # retranslateUi

