from PyQt5 import QtWidgets, QtCore
from db import ControlGSM

import uiaddeditvehicle

c = ControlGSM("information.db")

class AddEditVehicleWindow(QtWidgets.QMainWindow, uiaddeditvehicle.Ui_AddEditVehicleWindow):
    Add = 0
    Edit = 1
    def __init__(self, parent, mode, type = -1, vehicle = -1):
        super().__init__()
        self.setupUi(self)
        self.type = type
        self.mode = mode
        self.vehicle = vehicle
        self.parent = parent
        if self.mode == self.Edit:
            self.pasteInfo()

        self.initButtons()
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)

    def pasteInfo(self):
        v = c.vehicleInfo(self.vehicle)
        if not v:
            return
        self.nameEdit.setText(v["Name"])
        self.numberEdit.setText(v["Number"])
        self.consEdit.setValue(v["Cons"])
        self.setWindowTitle("Изменение техники")

    def initButtons(self):
        self.okButton.clicked.connect(self.okClicked)
        self.cancelButton.clicked.connect(self.close)

    def okClicked(self):
        name = self.nameEdit.text()
        number = self.numberEdit.text()
        cons = self.consEdit.value()
        if len(name) < 1:
            self.nameEdit.setFocus()
            return
        if len(number) < 1:
            self.numberEdit.setFocus()
            return
        if cons < 0:
            self.nameEdit.setFocus()
            return

        if self.mode == self.Add:
            if c.newVehicle(self.type, name, number, cons):
                self.parent.typeChanged()
                self.close()
            else:
                s = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Ошибка", "Ошибка")
                return
        elif self.mode == self.Edit:
            if c.editVehicle(self.vehicle, name, number, cons):
                self.parent.typeChanged()
                self.close()
            else:
                s = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Ошибка", "Ошибка")
                return