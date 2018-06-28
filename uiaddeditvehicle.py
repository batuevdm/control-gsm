# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\add_edit_vehicle.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddEditVehicleWindow(object):
    def setupUi(self, AddEditVehicleWindow):
        AddEditVehicleWindow.setObjectName("AddEditVehicleWindow")
        AddEditVehicleWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        AddEditVehicleWindow.resize(490, 127)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddEditVehicleWindow.sizePolicy().hasHeightForWidth())
        AddEditVehicleWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gas_station.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddEditVehicleWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AddEditVehicleWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout.addWidget(self.nameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.numberEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.numberEdit.setObjectName("numberEdit")
        self.horizontalLayout_4.addWidget(self.numberEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.consEdit = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.consEdit.sizePolicy().hasHeightForWidth())
        self.consEdit.setSizePolicy(sizePolicy)
        self.consEdit.setMaximum(99999999999.0)
        self.consEdit.setObjectName("consEdit")
        self.horizontalLayout_3.addWidget(self.consEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_2.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        AddEditVehicleWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddEditVehicleWindow)
        QtCore.QMetaObject.connectSlotsByName(AddEditVehicleWindow)

    def retranslateUi(self, AddEditVehicleWindow):
        _translate = QtCore.QCoreApplication.translate
        AddEditVehicleWindow.setWindowTitle(_translate("AddEditVehicleWindow", "Новая техника"))
        self.label.setText(_translate("AddEditVehicleWindow", "Название"))
        self.label_3.setText(_translate("AddEditVehicleWindow", "Номер"))
        self.label_2.setText(_translate("AddEditVehicleWindow", "Расход на 100 км"))
        self.consEdit.setSuffix(_translate("AddEditVehicleWindow", " л"))
        self.okButton.setText(_translate("AddEditVehicleWindow", "Ок"))
        self.cancelButton.setText(_translate("AddEditVehicleWindow", "Отменить"))

