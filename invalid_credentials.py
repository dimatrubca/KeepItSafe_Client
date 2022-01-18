# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'invalid_credentials.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor, QValidator

class InvalidCredentialsDialog(QtWidgets.QDialog):
    def __init__(self, title, description, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_dialog()
        self.ui.setupUi(self)

        self.ui.title_label.setText(title)
        self.ui.description_label.setText(description)

        self.ui.ok_btn.clicked.connect(self.close_clicked)
        self.ui.ok_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def close_clicked(self):
        self.close()

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(400, 150)
        dialog.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(252, 184, 184, 255), stop: 1 rgba(178, 214, 240, 255));")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(dialog)
        self.verticalLayout_2.setContentsMargins(18, 18, 18, 18)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("background: none")
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.description_label = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.description_label.setFont(font)
        self.description_label.setStyleSheet("background: none")
        self.description_label.setObjectName("description_label")
        self.verticalLayout.addWidget(self.description_label)
        self.ok_btn = QtWidgets.QPushButton(dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_btn.sizePolicy().hasHeightForWidth())
        self.ok_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ok_btn.setFont(font)
        self.ok_btn.setStyleSheet("background: rgb(189, 67, 67, 255);\n"
"border: none;\n"
"color: white;\n"
"padding: 8px 60px;\n"
"border-radius: 15px;")
        self.ok_btn.setObjectName("ok_btn")
        self.verticalLayout.addWidget(self.ok_btn, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Failure"))
        self.title_label.setText(_translate("dialog", "Incorrect Credentials"))
        self.description_label.setText(_translate("dialog", "Please verify entered data and try again"))
        self.ok_btn.setText(_translate("dialog", "OK"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())