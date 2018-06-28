# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_mil.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddMilWindow(object):
    def setupUi(self, AddMilWindow):
        AddMilWindow.setObjectName("AddMilWindow")
        AddMilWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        AddMilWindow.resize(221, 101)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddMilWindow.sizePolicy().hasHeightForWidth())
        AddMilWindow.setSizePolicy(sizePolicy)
        AddMilWindow.setMinimumSize(QtCore.QSize(221, 101))
        AddMilWindow.setMaximumSize(QtCore.QSize(221, 101))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gas_station.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddMilWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AddMilWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.milsEdit = QtWidgets.QSpinBox(self.centralwidget)
        self.milsEdit.setPrefix("")
        self.milsEdit.setMaximum(999999999)
        self.milsEdit.setSingleStep(1)
        self.milsEdit.setObjectName("milsEdit")
        self.horizontalLayout.addWidget(self.milsEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_2.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        AddMilWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddMilWindow)
        QtCore.QMetaObject.connectSlotsByName(AddMilWindow)

    def retranslateUi(self, AddMilWindow):
        _translate = QtCore.QCoreApplication.translate
        AddMilWindow.setWindowTitle(_translate("AddMilWindow", "Добавить пробег"))
        self.label.setText(_translate("AddMilWindow", "Пробег"))
        self.milsEdit.setSuffix(_translate("AddMilWindow", " км"))
        self.okButton.setText(_translate("AddMilWindow", "Ок"))
        self.cancelButton.setText(_translate("AddMilWindow", "Отменить"))

