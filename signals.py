from PyQt5 import QtCore

class MySignal(QtCore.QObject):
    signal_intruder_detected = QtCore.pyqtSignal()
    signal_state_changed = QtCore.pyqtSignal()
    signal_qr_code = QtCore.pyqtSignal()