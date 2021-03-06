# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\info.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InfoWindow(object):
    def setupUi(self, InfoWindow):
        InfoWindow.setObjectName("InfoWindow")
        InfoWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        InfoWindow.resize(587, 524)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/dimab/Downloads/gas_station.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        InfoWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(InfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setText("")
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout.addWidget(self.nameLabel)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.numberLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.numberLabel.setFont(font)
        self.numberLabel.setText("")
        self.numberLabel.setObjectName("numberLabel")
        self.verticalLayout.addWidget(self.numberLabel)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.consLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.consLabel.setFont(font)
        self.consLabel.setText("")
        self.consLabel.setObjectName("consLabel")
        self.verticalLayout.addWidget(self.consLabel)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.mileageLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mileageLabel.setFont(font)
        self.mileageLabel.setText("")
        self.mileageLabel.setObjectName("mileageLabel")
        self.verticalLayout.addWidget(self.mileageLabel)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.oilLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.oilLabel.setFont(font)
        self.oilLabel.setText("")
        self.oilLabel.setObjectName("oilLabel")
        self.verticalLayout.addWidget(self.oilLabel)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setObjectName("tabWidget")
        self.milTab = QtWidgets.QWidget()
        self.milTab.setObjectName("milTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.milTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.milList = QtWidgets.QTreeWidget(self.milTab)
        self.milList.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.milList.setIndentation(0)
        self.milList.setObjectName("milList")
        self.milList.header().setCascadingSectionResizes(True)
        self.milList.header().setDefaultSectionSize(150)
        self.milList.header().setHighlightSections(True)
        self.milList.header().setMinimumSectionSize(70)
        self.milList.header().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.milList)
        self.milButton = QtWidgets.QPushButton(self.milTab)
        self.milButton.setObjectName("milButton")
        self.verticalLayout_2.addWidget(self.milButton)
        self.tabWidget.addTab(self.milTab, "")
        self.fillTab = QtWidgets.QWidget()
        self.fillTab.setObjectName("fillTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fillTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fillList = QtWidgets.QTreeWidget(self.fillTab)
        self.fillList.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.fillList.setIndentation(0)
        self.fillList.setObjectName("fillList")
        self.fillList.header().setHighlightSections(True)
        self.fillList.header().setStretchLastSection(False)
        self.verticalLayout_3.addWidget(self.fillList)
        self.fillButton = QtWidgets.QPushButton(self.fillTab)
        self.fillButton.setObjectName("fillButton")
        self.verticalLayout_3.addWidget(self.fillButton)
        self.tabWidget.addTab(self.fillTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        InfoWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(InfoWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(InfoWindow)

    def retranslateUi(self, InfoWindow):
        _translate = QtCore.QCoreApplication.translate
        InfoWindow.setWindowTitle(_translate("InfoWindow", "Информация о технике"))
        self.label.setText(_translate("InfoWindow", "Название"))
        self.label_2.setText(_translate("InfoWindow", "Номер"))
        self.label_5.setText(_translate("InfoWindow", "Расход на 100 км"))
        self.label_3.setText(_translate("InfoWindow", "Текущий пробег"))
        self.label_4.setText(_translate("InfoWindow", "Количество топлива"))
        self.milList.setSortingEnabled(True)
        self.milList.headerItem().setText(0, _translate("InfoWindow", "#"))
        self.milList.headerItem().setText(1, _translate("InfoWindow", "Дата"))
        self.milList.headerItem().setText(2, _translate("InfoWindow", "Пробег"))
        self.milList.headerItem().setText(3, _translate("InfoWindow", "Расход топлива с прошлого измерения"))
        self.milList.headerItem().setText(4, _translate("InfoWindow", "Остаток топлива"))
        self.milButton.setText(_translate("InfoWindow", "Добавить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.milTab), _translate("InfoWindow", "Пробег"))
        self.fillList.setSortingEnabled(True)
        self.fillList.headerItem().setText(0, _translate("InfoWindow", "#"))
        self.fillList.headerItem().setText(1, _translate("InfoWindow", "Дата"))
        self.fillList.headerItem().setText(2, _translate("InfoWindow", "Количество"))
        self.fillList.headerItem().setText(3, _translate("InfoWindow", "Остаток топлива"))
        self.fillButton.setText(_translate("InfoWindow", "Добавить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fillTab), _translate("InfoWindow", "Заправки"))

