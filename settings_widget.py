# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class SettingsWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 576)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_frame = QtWidgets.QFrame(Form)
        self.left_frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.left_frame.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(208, 229, 244, 0), stop: 1 rgba(165, 207, 238, 255));")
        self.left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_frame.setObjectName("left_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.app_logo = QtWidgets.QLabel(self.left_frame)
        self.app_logo.setMaximumSize(QtCore.QSize(200, 80))
        self.app_logo.setStyleSheet("background: none\n"
"")
        self.app_logo.setText("")
        self.app_logo.setPixmap(QtGui.QPixmap(":/images/logo.png"))
        self.app_logo.setScaledContents(True)
        self.app_logo.setObjectName("app_logo")
        self.verticalLayout.addWidget(self.app_logo)
        self.main_menu_vlayout = QtWidgets.QVBoxLayout()
        self.main_menu_vlayout.setObjectName("main_menu_vlayout")
        self.menu_label = QtWidgets.QLabel(self.left_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menu_label.setFont(font)
        self.menu_label.setStyleSheet("background: none;\n"
"margin: 10px 0")
        self.menu_label.setObjectName("menu_label")
        self.main_menu_vlayout.addWidget(self.menu_label)
        self.home_btn = QtWidgets.QPushButton(self.left_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_btn.setFont(font)
        self.home_btn.setStyleSheet("border: none;\n"
"background: none;\n"
"margin: 5px 0")
        self.home_btn.setObjectName("home_btn")
        self.main_menu_vlayout.addWidget(self.home_btn, 0, QtCore.Qt.AlignLeft)
        self.users_btn = QtWidgets.QPushButton(self.left_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.users_btn.setFont(font)
        self.users_btn.setStyleSheet("border: none;\n"
"background: none;")
        self.users_btn.setObjectName("users_btn")
        self.main_menu_vlayout.addWidget(self.users_btn, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addLayout(self.main_menu_vlayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.second_menu_vlayout = QtWidgets.QVBoxLayout()
        self.second_menu_vlayout.setObjectName("second_menu_vlayout")
        self.support_btn = QtWidgets.QPushButton(self.left_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.support_btn.setFont(font)
        self.support_btn.setStyleSheet("border: none;\n"
"background: none;\n"
"margin: 5px 0")
        self.support_btn.setObjectName("support_btn")
        self.second_menu_vlayout.addWidget(self.support_btn, 0, QtCore.Qt.AlignLeft)
        self.settings_btn = QtWidgets.QPushButton(self.left_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.settings_btn.setFont(font)
        self.settings_btn.setStyleSheet("border: none;\n"
"background: none")
        self.settings_btn.setObjectName("settings_btn")
        self.second_menu_vlayout.addWidget(self.settings_btn, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addLayout(self.second_menu_vlayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.left_frame)
        self.center_frame = QtWidgets.QFrame(Form)
        self.center_frame.setStyleSheet("background-color: \"white\"")
        self.center_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center_frame.setObjectName("center_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.center_frame)
        self.verticalLayout_5.setContentsMargins(-1, 25, 150, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("vertical_layout")
        self.label = QtWidgets.QLabel(self.center_frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: \"#28B1D0\";\n"
"font-weight: bold;\n"
"margin: 10px 0 30px 0;\n"
"")
        self.label.setObjectName("label")
        self.vertical_layout.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.two_fa_checkbox = QtWidgets.QCheckBox(self.center_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.two_fa_checkbox.setFont(font)
        self.two_fa_checkbox.setObjectName("two_fa_checkbox")
        self.two_fa_checkbox.setChecked(True)
        self.vertical_layout.addWidget(self.two_fa_checkbox)
        self.two_fa_label = QtWidgets.QLabel(self.center_frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.two_fa_label.setFont(font)
        self.two_fa_label.setStyleSheet("color: gray;\n"
"margin-bottom: 30px")
        self.two_fa_label.setWordWrap(True)
        self.two_fa_label.setObjectName("two_fa_label")
        self.vertical_layout.addWidget(self.two_fa_label)
        self.sync_checkbox = QtWidgets.QCheckBox(self.center_frame)
        self.sync_checkbox.setChecked(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sync_checkbox.setFont(font)
        self.sync_checkbox.setObjectName("sync_checkbox")
        self.vertical_layout.addWidget(self.sync_checkbox)
        self.sync_label = QtWidgets.QLabel(self.center_frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sync_label.setFont(font)
        self.sync_label.setStyleSheet("color: gray")
        self.sync_label.setWordWrap(True)
        self.sync_label.setObjectName("sync_label")
        self.vertical_layout.addWidget(self.sync_label)
        self.back_btn = QtWidgets.QPushButton(self.center_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet("background-color: \"#24AFCD\";\n"
"color: white;\n"
"font-weight: bold;\n"
"border-radius: 10px;\n"
"padding: 10px 35px;\n"
"margin-top: 20px;\n"
"margin-bottom: 30px")
        self.back_btn.setObjectName("back_btn")
        self.vertical_layout.addWidget(self.back_btn, 0, QtCore.Qt.AlignRight)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.vertical_layout)
        self.horizontalLayout.addWidget(self.center_frame)
        self.right_frame = QtWidgets.QFrame(Form)
        self.right_frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.right_frame.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(244, 194, 194, 0), stop: 1 rgba(252, 182, 182, 255));")
        self.right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_frame.setObjectName("right_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.right_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.vlayout = QtWidgets.QVBoxLayout()
        self.vlayout.setContentsMargins(-1, 84, -1, -1)
        self.vlayout.setObjectName("vlayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.avatar_icon_label = QtWidgets.QLabel(self.right_frame)
        self.avatar_icon_label.setMaximumSize(QtCore.QSize(64, 64))
        self.avatar_icon_label.setStyleSheet("background: none;")
        self.avatar_icon_label.setText("")
        self.avatar_icon_label.setPixmap(QtGui.QPixmap(":/images/avatar-rounded.png"))
        self.avatar_icon_label.setScaledContents(True)
        self.avatar_icon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.avatar_icon_label.setWordWrap(False)
        self.avatar_icon_label.setObjectName("avatar_icon_label")
        self.horizontalLayout_4.addWidget(self.avatar_icon_label)
        self.vlayout.addLayout(self.horizontalLayout_4)
        self.full_name_label = QtWidgets.QLabel(self.right_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.full_name_label.setFont(font)
        self.full_name_label.setStyleSheet("background: none;\n"
"")
        self.full_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.full_name_label.setObjectName("full_name_label")
        self.vlayout.addWidget(self.full_name_label)
        self.joined_label = QtWidgets.QLabel(self.right_frame)
        self.joined_label.setStyleSheet("background: none")
        self.joined_label.setAlignment(QtCore.Qt.AlignCenter)
        self.joined_label.setObjectName("joined_label")
        self.vlayout.addWidget(self.joined_label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vlayout.addItem(spacerItem2)
        self.security_status_label = QtWidgets.QLabel(self.right_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.security_status_label.setFont(font)
        self.security_status_label.setStyleSheet("background: none")
        self.security_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.security_status_label.setObjectName("security_status_label")
        self.vlayout.addWidget(self.security_status_label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.status_icon_label = QtWidgets.QLabel(self.right_frame)
        self.status_icon_label.setMaximumSize(QtCore.QSize(128, 128))
        self.status_icon_label.setStyleSheet("background: none")
        self.status_icon_label.setText("")
        self.status_icon_label.setPixmap(QtGui.QPixmap(":/images/security_stats.png"))
        self.status_icon_label.setScaledContents(True)
        self.status_icon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_icon_label.setObjectName("status_icon_label")
        self.horizontalLayout_5.addWidget(self.status_icon_label)
        self.vlayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.vlayout)
        self.horizontalLayout.addWidget(self.right_frame)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.menu_label.setText(_translate("Form", "Menu"))
        self.home_btn.setText(_translate("Form", "Home"))
        self.users_btn.setText(_translate("Form", "Users"))
        self.support_btn.setText(_translate("Form", "Support"))
        self.settings_btn.setText(_translate("Form", "Settings"))
        self.label.setText(_translate("Form", "Settings"))
        self.two_fa_checkbox.setText(_translate("Form", "Enable two factor authentication (2FA)"))
        self.two_fa_label.setText(_translate("Form", "Two-factor authentication, a type of multi-factor authentication (MFA), is a security process that cross-verifies users with two different forms of identification. Enable this option to enhance secure access."))
        self.sync_checkbox.setText(_translate("Form", "Enable Syncronization"))
        self.sync_label.setText(_translate("Form", "Disable this option if you don\'t want to share your personal data. "))
        self.back_btn.setText(_translate("Form", "Back"))
        self.full_name_label.setText(_translate("Form", "Full Name"))
        self.joined_label.setText(_translate("Form", "Joined 15.01.2022"))
        self.security_status_label.setText(_translate("Form", "Security Status"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
