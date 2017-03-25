# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1123, 916)
        self.tableView_PM = QtWidgets.QTableView(Dialog)
        self.tableView_PM.setGeometry(QtCore.QRect(150, 130, 331, 681))
        self.tableView_PM.setObjectName("tableView_PM")
        self.tableView_LM = QtWidgets.QTableView(Dialog)
        self.tableView_LM.setGeometry(QtCore.QRect(620, 130, 256, 201))
        self.tableView_LM.setObjectName("tableView_LM")
        self.tableWidget_LM = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_LM.setGeometry(QtCore.QRect(620, 440, 256, 192))
        self.tableWidget_LM.setObjectName("tableWidget_LM")
        self.tableWidget_LM.setColumnCount(0)
        self.tableWidget_LM.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

