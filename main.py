import uimain
from Info import InfoWindow
from db import ControlGSM
from AddEditVehicle import AddEditVehicleWindow

import sys
from PyQt5 import QtWidgets, QtCore

c = ControlGSM("information.db")

class App(QtWidgets.QMainWindow, uimain.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.treeWidget.itemDoubleClicked.connect(self.openVehicleInfo)
        self.setTypesBox()
        self.vehicleType.currentIndexChanged.connect(self.typeChanged)
        self.typeChanged()

        self.addButton.clicked.connect(self.addButtonClick)
        self.editButton.clicked.connect(self.editButtonClick)
        self.delButton.clicked.connect(self.delButtonClick)

    def addButtonClick(self):
        self.addForm = AddEditVehicleWindow(self, AddEditVehicleWindow.Add, self.vehicleType.currentData())
        self.addForm.show()

    def editButtonClick(self):
        v = self.treeWidget.currentItem()
        if not v:
            return
        self.addForm = AddEditVehicleWindow(self, AddEditVehicleWindow.Edit, vehicle = int(v.text(0)))
        self.addForm.show()

    def delButtonClick(self):
        v = self.treeWidget.currentItem()
        if not v:
            return
        if c.isDelete(self, "эту технику из базы"):
            if c.delVehicle(int(v.text(0))):
                self.typeChanged()
            else:
                s = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Ошибка", "Ошибка")
                return

    def openVehicleInfo(self):
        self.info = InfoWindow(self, int(self.treeWidget.currentItem().text(0)))
        self.info.show()

    def typeChanged(self):
        index = self.vehicleType.currentData()
        vehicles = c.getVehicles(index)
        self.treeWidget.clear()

        for v in vehicles:
            item = QtWidgets.QTreeWidgetItem(self.treeWidget)
            info = c.vehicleInfo(v["ID"])
            item.setText(0, str(v["ID"]))
            item.setText(1, info["Number"])
            item.setText(2, info["Name"])
            item.setText(3, str(info["Mileage"]))
            item.setText(4, "%.2f" % info["Oil"])

        for i in range(self.treeWidget.columnCount()):
            self.treeWidget.resizeColumnToContents(i)

    def setTypesBox(self):
        items = c.getTypes()
        if items:
            for item in items:
                self.vehicleType.addItem(item['Name'], item['ID'])

def main():
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = App()
        window.show()
        app.exec_()
    except Exception as err:
        print("Error: %s" % err)
        raise

if __name__ == "__main__":
    main()