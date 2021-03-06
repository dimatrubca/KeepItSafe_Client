# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(927, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.centralwidget_hlayout = QtWidgets.QHBoxLayout()
        self.centralwidget_hlayout.setSpacing(0)
        self.centralwidget_hlayout.setObjectName("centralwidget_hlayout")
        self.left_frame = QtWidgets.QFrame(self.centralwidget)
        self.left_frame.setAutoFillBackground(False)
        self.left_frame.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(14, 201, 242, 107), stop: 1 rgba(34, 173, 204, 255));")
        self.left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_frame.setObjectName("left_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.left_frame_vlayout = QtWidgets.QVBoxLayout()
        self.left_frame_vlayout.setObjectName("left_frame_vlayout")
        self.logo = QtWidgets.QLabel(self.left_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMaximumSize(QtCore.QSize(290, 90))
        self.logo.setStyleSheet("background: none")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../../../../../Users/dimat/OneDrive/??????????????????????/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.left_frame_vlayout.addWidget(self.logo)
        self.ellipse = QtWidgets.QFrame(self.left_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ellipse.sizePolicy().hasHeightForWidth())
        self.ellipse.setSizePolicy(sizePolicy)
        self.ellipse.setMinimumSize(QtCore.QSize(350, 350))
        self.ellipse.setMaximumSize(QtCore.QSize(350, 350))
        self.ellipse.setStyleSheet("border-radius: 175")
        self.ellipse.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ellipse.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ellipse.setObjectName("ellipse")
        self.ellipse_icon = QtWidgets.QLabel(self.ellipse)
        self.ellipse_icon.setGeometry(QtCore.QRect(70, 60, 201, 241))
        self.ellipse_icon.setStyleSheet("background: none\n"
"\n"
"")
        self.ellipse_icon.setText("")
        self.ellipse_icon.setPixmap(QtGui.QPixmap("../../../../../Users/dimat/OneDrive/??????????????????????/phone.png"))
        self.ellipse_icon.setScaledContents(True)
        self.ellipse_icon.setObjectName("ellipse_icon")
        self.left_frame_vlayout.addWidget(self.ellipse, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.left_frame_vlayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.left_frame_vlayout)
        self.centralwidget_hlayout.addWidget(self.left_frame)
        self.right_frame = QtWidgets.QFrame(self.centralwidget)
        self.right_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_frame.setObjectName("right_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.right_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setContentsMargins(20, 20, 40, 20)
        self.grid_layout.setHorizontalSpacing(12)
        self.grid_layout.setObjectName("grid_layout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid_layout.addItem(spacerItem1, 8, 2, 1, 1)
        self.password_label = QtWidgets.QLabel(self.right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_label.sizePolicy().hasHeightForWidth())
        self.password_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("margin: 10px 0;")
        self.password_label.setObjectName("password_label")
        self.grid_layout.addWidget(self.password_label, 3, 0, 1, 7)
        self.email_le = QtWidgets.QLineEdit(self.right_frame)
        self.email_le.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email_le.setFont(font)
        self.email_le.setStyleSheet("borde-color: none;\n"
"background-color: rgb(149, 231, 249, 38);\n"
"border-radius: 15px;\n"
"padding: 0 8px;")
        self.email_le.setObjectName("email_le")
        self.grid_layout.addWidget(self.email_le, 2, 0, 1, 7)
        self.login_btn = QtWidgets.QPushButton(self.right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setMinimumSize(QtCore.QSize(150, 44))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet("background-color: \"#24AFCD\";\n"
"color: white;\n"
"font-weight: bold;\n"
"border-radius: 10px;")
        self.login_btn.setObjectName("login_btn")
        self.grid_layout.addWidget(self.login_btn, 6, 4, 1, 3)
        self.forgot_password_btn = QtWidgets.QLabel(self.right_frame)
        self.forgot_password_btn.setMinimumSize(QtCore.QSize(0, 44))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.forgot_password_btn.setFont(font)
        self.forgot_password_btn.setStyleSheet("color: \"#2EB6D3\";\n"
"font-weight: bold")
        self.forgot_password_btn.setObjectName("forgot_password_btn")
        self.grid_layout.addWidget(self.forgot_password_btn, 5, 4, 1, 3, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.login_label = QtWidgets.QLabel(self.right_frame)
        self.login_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("color: \"#28B1D0\";\n"
"font-weight: bold;\n"
"margin: 10px 0 ")
        self.login_label.setTextFormat(QtCore.Qt.AutoText)
        self.login_label.setScaledContents(False)
        self.login_label.setWordWrap(False)
        self.login_label.setIndent(-3)
        self.login_label.setObjectName("login_label")
        self.grid_layout.addWidget(self.login_label, 0, 0, 1, 2, QtCore.Qt.AlignTop)
        self.password_le = QtWidgets.QLineEdit(self.right_frame)
        self.password_le.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_le.setFont(font)
        self.password_le.setStyleSheet("borde-color: none;\n"
"background-color: rgb(149, 231, 249, 38);\n"
"border-radius: 15px;\n"
"padding: 0 8px;")
        self.password_le.setObjectName("password_le")
        self.grid_layout.addWidget(self.password_le, 4, 0, 1, 7)
        self.sign_up_question_label = QtWidgets.QLabel(self.right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sign_up_question_label.sizePolicy().hasHeightForWidth())
        self.sign_up_question_label.setSizePolicy(sizePolicy)
        self.sign_up_question_label.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.sign_up_question_label.setFont(font)
        self.sign_up_question_label.setObjectName("sign_up_question_label")
        self.grid_layout.addWidget(self.sign_up_question_label, 7, 3, 1, 2)
        self.email_label = QtWidgets.QLabel(self.right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_label.sizePolicy().hasHeightForWidth())
        self.email_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("margin: 10px 0;")
        self.email_label.setObjectName("email_label")
        self.grid_layout.addWidget(self.email_label, 1, 0, 1, 7)
        self.remember_me_checkbox = QtWidgets.QCheckBox(self.right_frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.remember_me_checkbox.setFont(font)
        self.remember_me_checkbox.setStyleSheet("margin: 15px 0;\n"
"")
        self.remember_me_checkbox.setObjectName("remember_me_checkbox")
        self.grid_layout.addWidget(self.remember_me_checkbox, 5, 0, 1, 4, QtCore.Qt.AlignTop)
        self.sign_up_btn = QtWidgets.QPushButton(self.right_frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.sign_up_btn.setFont(font)
        self.sign_up_btn.setStyleSheet("border: none;\n"
"color: \"#27B1CF\";\n"
"font-weight: bold")
        self.sign_up_btn.setObjectName("sign_up_btn")
        self.grid_layout.addWidget(self.sign_up_btn, 7, 5, 1, 1)
        self.grid_layout.setRowMinimumHeight(0, 60)
        self.grid_layout.setRowMinimumHeight(5, 60)
        self.grid_layout.setRowMinimumHeight(7, 80)
        self.gridLayout_2.addLayout(self.grid_layout, 0, 0, 1, 1)
        self.centralwidget_hlayout.addWidget(self.right_frame)
        self.horizontalLayout_3.addLayout(self.centralwidget_hlayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.forgot_password_btn.setText(_translate("MainWindow", "Forgot Password?"))
        self.login_label.setText(_translate("MainWindow", "LOGIN"))
        self.sign_up_question_label.setText(_translate("MainWindow", "Don\'t have an account?"))
        self.email_label.setText(_translate("MainWindow", "Email"))
        self.remember_me_checkbox.setText(_translate("MainWindow", "Remember me"))
        self.sign_up_btn.setText(_translate("MainWindow", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
