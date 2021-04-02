# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(349, 347)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_Windows = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_Windows.setObjectName("Button_Windows")
        self.horizontalLayout.addWidget(self.Button_Windows)
        self.Button_Linux = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_Linux.setObjectName("Button_Linux")
        self.horizontalLayout.addWidget(self.Button_Linux)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.Port_list = QtWidgets.QListWidget(self.centralwidget)
        self.Port_list.setObjectName("Port_list")
        self.verticalLayout.addWidget(self.Port_list)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.Select_Port = QtWidgets.QPushButton(self.centralwidget)
        self.Select_Port.setObjectName("Select_Port")
        self.verticalLayout.addWidget(self.Select_Port)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 349, 20))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "Puerto serie"))
        self.label.setText(_translate("MainWindow2", "<html><head/><body><p><span style=\" font-size:16pt;\">Conexión puerto</span></p></body></html>"))
        self.Button_Windows.setText(_translate("MainWindow2", "Windows"))
        self.Button_Linux.setText(_translate("MainWindow2", "Linux"))
        self.Select_Port.setText(_translate("MainWindow2", "Seleccionar"))

