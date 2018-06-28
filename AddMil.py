from db import ControlGSM
from PyQt5 import QtWidgets, QtCore
import time
import uiaddmil
import Info as iw

c = ControlGSM("information.db")

class AddMilWindow(QtWidgets.QMainWindow, uiaddmil.Ui_AddMilWindow):
    def __init__(self, parent, vehicle):
        super().__init__()
        self.setupUi(self)

        self.parent = parent
        self.vehicle = vehicle
        self.vehicleInfo = c.vehicleInfo(self.vehicle)

        self.initButtons()
        self.milsEdit.setValue(c.lastMils(self.vehicle))
        self.milsEdit.setMinimum(c.lastMils(self.vehicle))

        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)

    def initButtons(self):
        self.okButton.clicked.connect(self.okClicked)
        self.cancelButton.clicked.connect(self.close)

    def okClicked(self):
        mils = self.milsEdit.value()
        if mils < c.lastMils(self.vehicle):
            QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Пробег не может быть меньше предыдущего", "Ошибка")
            return
        if c.newMileage(self.vehicle, mils, round(time.time())):
            self.parent.updateInfo()
            self.close()
        else:
            QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Ошибка добавления", "Ошибка")