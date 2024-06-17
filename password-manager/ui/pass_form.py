# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pass_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_PasswordDialog(object):
    def setupUi(self, PasswordDialog):
        if not PasswordDialog.objectName():
            PasswordDialog.setObjectName(u"PasswordDialog")
        PasswordDialog.resize(508, 348)
        PasswordDialog.setMinimumSize(QSize(0, 0))
        PasswordDialog.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        font.setPointSize(12)
        PasswordDialog.setFont(font)
        self.verticalLayout = QVBoxLayout(PasswordDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame = QFrame(PasswordDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(10, -1, 10, -1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.serviceEdit = QLineEdit(self.frame)
        self.serviceEdit.setObjectName(u"serviceEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.serviceEdit)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.loginEdit = QLineEdit(self.frame)
        self.loginEdit.setObjectName(u"loginEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.loginEdit)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.passEdit = QLineEdit(self.frame)
        self.passEdit.setObjectName(u"passEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.passEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.genButton = QPushButton(self.frame)
        self.genButton.setObjectName(u"genButton")
        self.genButton.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.genButton)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setTextFormat(Qt.TextFormat.AutoText)
        self.label_4.setScaledContents(False)

        self.verticalLayout_2.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.saveButton = QPushButton(PasswordDialog)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(120, 0))

        self.horizontalLayout.addWidget(self.saveButton)

        self.horizontalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(PasswordDialog)

        QMetaObject.connectSlotsByName(PasswordDialog)
    # setupUi

    def retranslateUi(self, PasswordDialog):
        PasswordDialog.setWindowTitle(QCoreApplication.translate("PasswordDialog", u"title", None))
        self.label.setText(QCoreApplication.translate("PasswordDialog", u"\u0421\u0435\u0440\u0432\u0438\u0441", None))
        self.label_2.setText(QCoreApplication.translate("PasswordDialog", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_3.setText(QCoreApplication.translate("PasswordDialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
#if QT_CONFIG(tooltip)
        self.genButton.setToolTip(QCoreApplication.translate("PasswordDialog", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043d\u0430\u0434\u0451\u0436\u043d\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.genButton.setText(QCoreApplication.translate("PasswordDialog", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("PasswordDialog", u"password", None))
        self.saveButton.setText(QCoreApplication.translate("PasswordDialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

