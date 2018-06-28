import uiinfo
from db import ControlGSM
from PyQt5 import QtWidgets
from datetime import datetime
import AddMil
import AddFill

c = ControlGSM("information.db")

class InfoWindow(QtWidgets.QMainWindow, uiinfo.Ui_InfoWindow):
    vehicle = -1
    def __init__(self, parent, vehicle):
        super().__init__()
        self.setupUi(self)
        self.vehicle = vehicle
        self.parent = parent

        self.vehicleInfo = c.vehicleInfo(self.vehicle)
        self.updateInfo()

        self.milButton.clicked.connect(self.openAddMilsForm)
        self.fillButton.clicked.connect(self.openAddFillsForm)

        self.addContextMenus()

    def addContextMenus(self):
        p = self.milList
        delAction = QtWidgets.QAction("Удалить", p)
        delAction.triggered.connect(self.delMil)

        p.addAction(delAction)

        p = self.fillList
        delAction = QtWidgets.QAction("Удалить", p)
        delAction.triggered.connect(self.delFill)

        p.addAction(delAction)

    def delMil(self):
        index = self.milList.currentItem()
        if not index:
            return

        if c.isDelete(self, "этот пункт"):
            c.delMileage(int(index.text(0)))
            self.updateInfo()

    def delFill(self):
        index = self.fillList.currentItem()
        if not index:
            return

        if c.isDelete(self, "этот пункт"):
            c.delRefill(int(index.text(0)))
            self.updateInfo()

    def openAddMilsForm(self):
        self.addMils = AddMil.AddMilWindow(self, self.vehicle)
        self.addMils.show()

    def openAddFillsForm(self):
        self.addFills = AddFill.AddFillWindow(self, self.vehicle)
        self.addFills.show()

    def showInfo(self):
        v = c.vehicleInfo(self.vehicle)
        if not v:
            print("Error vehice")
            return
        self.setWindowTitle("Информация о технике \"%s\"" % v["Name"])
        self.nameLabel.setText(v["Name"])
        self.numberLabel.setText(v["Number"])
        self.consLabel.setText("%.2f л" % v["Cons"])
        self.mileageLabel.setText("%d км" % v["Mileage"])
        self.oilLabel.setText("%.2f л" % v["Oil"])

    def updateInfo(self):
        self.showMils()
        self.showFills()
        self.showInfo()
        self.parent.typeChanged()

    def showMils(self):
        self.milList.clear()
        mils = c.getMileage(self.vehicle)
        for i, mil in enumerate(mils):
            item = QtWidgets.QTreeWidgetItem(self.milList)
            item.setText(0, str(mil["ID"]))
            item.setText(1, datetime.fromtimestamp(mil["Date"]).strftime("%d-%m-%Y %H:%M:%S"))
            item.setText(2, str(mil["Count"]))
            prev = c.getPrevItem(mils, i)
            if not prev:
                prevMils = 0
            else:
                prevMils = prev["Count"]
            nowMils = mil["Count"] - prevMils
            item.setText(3, "%.2f" % (nowMils / 100 * self.vehicleInfo["Cons"]))


            mileages = c.getMileage(self.vehicle)
            refills = c.getRefills(self.vehicle)

            data = mileages + refills
            data = sorted(data, key = lambda x: x["Date"])
            data = list(filter(lambda x: x["Date"] <= mil["Date"], data))
            oilLast = c.calcOil(data, self.vehicleInfo["Cons"])

            item.setText(4, "%.2f" % oilLast)

        for i in range(self.milList.columnCount()):
            self.milList.resizeColumnToContents(i)

    def showFills(self):
        self.fillList.clear()
        fills = c.getRefills(self.vehicle)
        for i, fill in enumerate(fills):
            item = QtWidgets.QTreeWidgetItem(self.fillList)
            item.setText(0, str(fill["ID"]))
            item.setText(1, datetime.fromtimestamp(fill["Date"]).strftime("%d-%m-%Y %H:%M:%S"))
            item.setText(2, "%.2f" % fill["Count"])

            mileages = c.getMileage(self.vehicle)
            refills = c.getRefills(self.vehicle)

            data = mileages + refills
            data = sorted(data, key = lambda x: x["Date"])
            data = list(filter(lambda x: x["Date"] <= fill["Date"], data))
            oilLast = c.calcOil(data, self.vehicleInfo["Cons"])

            item.setText(3, "%.2f" % oilLast)

        for i in range(self.fillList.columnCount()):
            self.fillList.resizeColumnToContents(i)