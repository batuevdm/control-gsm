from db import ControlGSM
from PyQt5 import QtWidgets, QtCore
import time
import uiaddfill
import Info as iw

c = ControlGSM("information.db")

class AddFillWindow(QtWidgets.QMainWindow, uiaddfill.Ui_AddFillWindow):
    def __init__(self, parent, vehicle):
        super().__init__()
        self.setupUi(self)

        self.parent = parent
        self.vehicle = vehicle
        self.vehicleInfo = c.vehicleInfo(self.vehicle)

        self.initButtons()
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)

    def initButtons(self):
        self.okButton.clicked.connect(self.okClicked)
        self.cancelButton.clicked.connect(self.close)

    def okClicked(self):
        fills = self.fillCountEdit.value()
        if fills < 0.01:
            QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Количество должно быть больше нуля", "Ошибка")
            return
        if c.newRefill(self.vehicle, fills, round(time.time())):
            self.parent.updateInfo()
            self.close()
        else:
            QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Ошибка добавления", "Ошибка")