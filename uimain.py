# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 259)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gas_station.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(68, 20))
        self.label.setMaximumSize(QtCore.QSize(68, 20))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.vehicleType = QtWidgets.QComboBox(self.centralwidget)
        self.vehicleType.setObjectName("vehicleType")
        self.horizontalLayout.addWidget(self.vehicleType)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setStyleSheet("")
        self.treeWidget.setAutoExpandDelay(-1)
        self.treeWidget.setIndentation(0)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setColumnCount(5)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setCascadingSectionResizes(True)
        self.treeWidget.header().setDefaultSectionSize(100)
        self.treeWidget.header().setHighlightSections(True)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.treeWidget.header().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.treeWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_2.addWidget(self.addButton)
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout_2.addWidget(self.editButton)
        self.delButton = QtWidgets.QPushButton(self.centralwidget)
        self.delButton.setObjectName("delButton")
        self.horizontalLayout_2.addWidget(self.delButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Контроль ГСМ"))
        self.label.setText(_translate("MainWindow", "Тип техники"))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "#"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Номер"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Название"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Пробег"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Остаток топлива"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.editButton.setText(_translate("MainWindow", "Изменить"))
        self.delButton.setText(_translate("MainWindow", "Удалить"))

