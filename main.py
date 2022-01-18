import imp
import logging
import re
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QDialog, QDialogButtonBox, QLabel, QVBoxLayout
from PyQt5.QtGui import QCursor, QValidator
from PyQt5 import QtCore
from invalid_credentials import InvalidCredentialsDialog
from keystroke_tracker import get_duration_keystroke, get_error_rate, get_flight_time, get_pressure, get_seek_time, get_typing_speed, get_typings_speed, start_tracking
import login_widget
from otp import generate_qr_image
import register_widget2
import main_widget2, settings_widget
import two_factor_widget
from dtos import UserDto, UserLoginDto
from intruder_alert import IntruderAlertDialog
from auth import register, login
from signals import MySignal

logging.basicConfig(level=logging.DEBUG,  format='%(asctime)s:%(name)s:%(message)s', datefmt="%m/%d/%Y %I:%M:%S %p")
logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.state = False
        self.login = login_widget.LoginWidget()
        self.register = register_widget2.RegisterWidget()
        self.two_factor_page = two_factor_widget.TwoFactorWidget()
        self.main_page = main_widget2.MainWidget()
        self.settings_page = settings_widget.SettingsWidget()

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.login)
        self.stacked_widget.addWidget(self.register)
        self.stacked_widget.addWidget(self.two_factor_page)
        self.stacked_widget.addWidget(self.main_page)
        self.stacked_widget.addWidget(self.settings_page)

        self.setCentralWidget(self.stacked_widget)

        self.login.ui.sign_up_btn.clicked.connect(self.go_to_second)
        self.register.ui.login_btn.clicked.connect(self.go_to_first)
        self.login.ui.login_btn.clicked.connect(self.login_user)

        self.register.ui.login_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.register.ui.sign_up_btn.clicked.connect(self.register_user)

        self.two_factor_page.ui.continue_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.two_factor_page.ui.continue_btn.clicked.connect(self.two_factor_continue)

        self.login.ui.sign_up_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.login.ui.login_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        

        self.main_page.ui.home_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.main_page.ui.users_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))        
        self.main_page.ui.support_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.main_page.ui.settings_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.main_page.ui.settings_btn.clicked.connect(self.go_to_settings)

        self.settings_page.ui.home_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_page.ui.home_btn.clicked.connect(self.go_to_main)

        self.settings_page.ui.back_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_page.ui.back_btn.clicked.connect(self.go_to_main)

        self.signal = MySignal()
        self.signal.signal_intruder_detected.connect(self.show_alert)
        self.signal.signal_state_changed.connect(self.change_state)

        

    def go_to_first(self):
        print('going to login page...')
        self.user = None
        self.stacked_widget.setCurrentIndex(0)
    
    def go_to_second(self):
        print('going to register page...')
        self.stacked_widget.setCurrentIndex(1)

    def go_to_two_factor_scan(self):
        print('going to two factor page...')
        self.stacked_widget.setCurrentIndex(2)
        qr_img = generate_qr_image(self.user.otp_secret, self.user.email)
        self.two_factor_page.display_qr_code(qr_img)

    def go_to_main(self):
        print('going to main page...')
        self.stacked_widget.setCurrentIndex(3)

        self.main_page.ui.full_name_label.setText(self.user.name)

        typing_speed = get_typings_speed(self.user.id)
        seek_time = get_seek_time(self.user.id)
        flight_time = get_flight_time(self.user.id)
        error_frequency = get_error_rate(self.user.id)
        pressure = get_pressure(self.user.id)
        duration_keystroke = get_duration_keystroke(self.user.id)
        
        if pressure:
            pressure_str = f'{error_frequency:.2f}'
        else:
            pressure_str = 'N/A'

        self.main_page.ui.value1.setText(str(typing_speed))
        self.main_page.ui.value2.setText(f'{seek_time:.2f}')
        self.main_page.ui.value3.setText(f'{flight_time:.2f}')
        self.main_page.ui.value4.setText(f'{error_frequency:.2f}')
        self.main_page.ui.value5.setText(pressure_str)
        self.main_page.ui.value6.setText(f'{duration_keystroke:.2f}')

    
    def go_to_settings(self):
        print('going to settings...')
        self.stacked_widget.setCurrentIndex(4)

        self.settings_page.ui.full_name_label.setText(self.user.name)


    def login_user(self):
        email = self.login.ui.email_le.text()
        password = self.login.ui.password_le.text()
        two_fa_code = self.login.ui.two_fa_le.text()

        user_login_dto = UserLoginDto(email, password, two_fa_code)

        self.user = login(user_login_dto)
        print('.........')
        print(self.user)
        print('...........')

        if self.user is None:
            dlg = InvalidCredentialsDialog("Incorrect credentials", "Please verify entered data and try again`")
            dlg.exec()
        else:
            threading.Thread(target=lambda: start_tracking(self.user.id, self.signal), daemon=True).start()
            self.go_to_main()

    def two_factor_continue(self):
        self.go_to_first()


    def show_alert(self):
        print('state:', self.state)
        if self.state:
            dlg = IntruderAlertDialog()
            dlg.exec()


    def register_user(self):
        mess = None

        name = self.register.ui.name_le.text()
        email = self.register.ui.email_le.text()
        phone_number = self.register.ui.phone_number_le.text()
        country = self.register.ui.country_le.text()
        city = self.register.ui.city_le.text()
        password = self.register.ui.password_le.text()
        cpassword = self.register.ui.cpassword_le.text()
        enable_2fa = self.register.ui.checkBox.isChecked()

        gender = None
        if self.register.ui.male_radiobtn.isChecked():
            gender = 'Male'
        elif self.register.ui.female_radiobtn.isChecked():
            gender = 'Female'

        if self.register.ui.name_le.validator().validate(name, 0)[0] != QValidator.State.Acceptable:
            mess = 'Invalid name!'

        if self.register.ui.email_le.validator().validate(email, 0)[0] != QValidator.State.Acceptable:
            mess = 'Invalid email!'

        if self.register.ui.phone_number_le.validator().validate(phone_number, 0)[0] != QValidator.State.Acceptable:
            mess = 'Invalid phone number!'

        if password != cpassword:
            mess = 'Invalid confirmation password!'

        if not country:
            mess = 'Country not entered'

        if not city:
            mess = 'City not entered'

        if not gender:
            mess = 'Gender not selected'

        if mess is None:
            user = UserDto(name=name, email=email, phone=phone_number, password=password, gender=gender, country=country, city=city, otp_secret=None, enable_2fa=enable_2fa)
            self.user = user = register(user)
#self.register.ui.checkBox.isChecked()
            if user is None:
                mess = 'Email already registered'


        if mess is not None:
           dlg = InvalidCredentialsDialog("Invalid fields detected", mess)
           dlg.exec()
        else:
            if enable_2fa:
                self.go_to_two_factor_scan()
            else:
                self.go_to_first()

    
    def change_state(self):
        self.state = not self.state

class AlertDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Alert')


class MessageDialog(QDialog):
    def __init__(self, message):
        super().__init__()

        self.setWindowTitle("Failure...")

        QBtn = QDialogButtonBox.Ok 

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message_label = QLabel(message)
        self.layout.addWidget(message_label)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    #app.exec_()

    app.setQuitOnLastWindowClosed(False)
  
    # Adding an icon
    icon = QIcon("k.png")
    
    # Adding item on the menu bar
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)
    tray.window = window
    
    # Creating the options
    menu = QMenu()
    option1 = QAction("Open")
    
    option1.triggered.connect(lambda: window.show())
    menu.addAction(option1)
    
    # To quit the app
    quit = QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)
    
    # Adding options to the System Tray
    tray.setContextMenu(menu)
    
    app.exec_()