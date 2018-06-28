import sqlite3
from PyQt5 import QtWidgets

class ControlGSM:
    def __init__(self, file):
        self.file = file
        self.connect()
    
    def connect(self):
        try:
            self.conn = sqlite3.connect(self.file)
            self.conn.row_factory = self.dict_factory;
            self.cur = self.conn.cursor()
        except Exception as e:
            print("Connect error!\n%s" % e)
            exit()

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def sql(self, sql, params = {}):
        try:
            self.cur.execute(sql, params)
            return self.cur.fetchall()
        except sqlite3.DatabaseError as e:
            print("SQL Query Error: %s" % e)
            return False

    def sqlInsert(self, sql, params = {}):
        try:
            self.cur.execute(sql, params)
            self.conn.commit()
            return True
        except Exception as e:
            print("SQL Query Error: %s" % e)
            return False

    def getTypes(self):
        return self.sql("SELECT * FROM types")

    def getVehicles(self, type = -1):
        if type < 0:
            where = ("types.ID > -1")
        else:
            where = ("types.ID = " + str(type))
        return self.sql("""
                SELECT vehicles.ID, vehicles.Name, vehicles.Consumption, types.Name AS Type
                FROM vehicles
                JOIN types ON vehicles.Type = types.ID
                WHERE """ + where)

    def getRefills(self, vehicle = -1):
        if vehicle < 0:
            where = ("vehicle > -1")
        else:
            where = ("vehicle = " + str(vehicle))
        where += " ORDER BY `Date`"
        return self.sql("SELECT *, 0 AS `Type` FROM refill WHERE " + where)

    def newRefill(self, vehicle, count, date):
        return self.sqlInsert("INSERT INTO refill (Vehicle, Count, Date) VALUES (?, ?, ?)", (vehicle, count, date))

    def delRefill(self, id):
        return self.sqlInsert("DELETE FROM refill WHERE `ID` = ?", (id,))

    def getMileage(self, vehicle = -1):
        if vehicle < 0:
            where = ("vehicle > -1")
        else:
            where = ("vehicle = " + str(vehicle))
        where += " ORDER BY `Date`"
        return self.sql("SELECT *, 1 AS `Type` FROM mileage WHERE " + where)

    def newMileage(self, vehicle, count, date):
        return self.sqlInsert("INSERT INTO mileage (Vehicle, Count, Date) VALUES (?, ?, ?)", (vehicle, count, date))

    def delMileage(self, id):
        return self.sqlInsert("DELETE FROM mileage WHERE `ID` = ?", (id,))

    def newVehicle(self, type, name, number, cons):
        return self.sqlInsert("INSERT INTO vehicles (`Type`, `Name`, `Number`, `Consumption`) VALUES (?, ?, ?, ?)", (type, name, number, cons))
    
    def editVehicle(self, vehicle, name, number, cons):
        return self.sqlInsert("UPDATE vehicles SET `Name` = ?, `Number` = ?, `Consumption` = ? WHERE `ID` = ?", (name, number, cons, vehicle))

    def delVehicle(self, vehicle):
        self.sqlInsert("DELETE FROM refill WHERE `Vehicle` = ?", (vehicle,))
        self.sqlInsert("DELETE FROM mileage WHERE `Vehicle` = ?", (vehicle,))
        return self.sqlInsert("DELETE FROM vehicles WHERE `ID` = ?", (vehicle,))

    def vehicleInfo(self, id):
        result = {}
        main = self.sql("SELECT * FROM vehicles WHERE ID = ?", (id,))
        if not main or len(main) == 0:
            return False
        milleage = self.sql("SELECT `Count` FROM mileage WHERE vehicle = ? ORDER BY `Date` DESC LIMIT 1", (id, ))
        if not milleage or len(milleage) == 0:
            result["Mileage"] = 0
        else:
            result["Mileage"] = milleage[0]["Count"]
        result["Name"] = main[0]["Name"]
        result["Number"] = main[0]["Number"]
        result["Cons"] = main[0]["Consumption"] 

        mileages = self.getMileage(id)
        refills = self.getRefills(id)

        data = mileages + refills
        data = sorted(data, key = lambda x: x["Date"])

        result["Oil"] = self.calcOil(data, main[0]["Consumption"])

        return result

    def calcOil(self, data, c):
        oil = 0.0

        for i, item in enumerate(data):
            if item["Type"] == 0:
                oil += item["Count"]
            else:
                res = 0.0
                prev = self.getPrevItem(data, i)
                if prev:
                    res += item["Count"] - prev["Count"]
                oil -= (res / 100) * c
        return oil

    def getPrevItem(self, items, i):
        if items[i-1] and i - 1 > -1:
            if items[i-1]["Type"] == 1:
                return items[i-1]
            else:
                return self.getPrevItem(items, i-1)
        else:
            return False

    def lastMils(self, vehicle):
        mils = self.getMileage(vehicle)
        if mils and len(mils) > 0:
            return mils[len(mils) - 1]["Count"]
        else:
            return 0

    def isDelete(self, parent, text = ""):
        dlg = QtWidgets.QMessageBox.question(parent, "Удаление", "Удалить %s?\nОтменить действие будет невозможно!" % text, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        return dlg == QtWidgets.QMessageBox.Yes