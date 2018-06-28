# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_fill.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddFillWindow(object):
    def setupUi(self, AddFillWindow):
        AddFillWindow.setObjectName("AddFillWindow")
        AddFillWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        AddFillWindow.resize(221, 101)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddFillWindow.sizePolicy().hasHeightForWidth())
        AddFillWindow.setSizePolicy(sizePolicy)
        AddFillWindow.setMinimumSize(QtCore.QSize(221, 101))
        AddFillWindow.setMaximumSize(QtCore.QSize(221, 101))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gas_station.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddFillWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AddFillWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.fillCountEdit = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.fillCountEdit.setMaximum(99999999999.0)
        self.fillCountEdit.setObjectName("fillCountEdit")
        self.horizontalLayout.addWidget(self.fillCountEdit)
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
        AddFillWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddFillWindow)
        QtCore.QMetaObject.connectSlotsByName(AddFillWindow)

    def retranslateUi(self, AddFillWindow):
        _translate = QtCore.QCoreApplication.translate
        AddFillWindow.setWindowTitle(_translate("AddFillWindow", "Заправка"))
        self.label.setText(_translate("AddFillWindow", "Количество"))
        self.fillCountEdit.setSuffix(_translate("AddFillWindow", " л"))
        self.okButton.setText(_translate("AddFillWindow", "Ок"))
        self.cancelButton.setText(_translate("AddFillWindow", "Отменить"))

