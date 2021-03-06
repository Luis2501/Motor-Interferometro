# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 333)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Connect_Arduino = QtWidgets.QPushButton(self.centralwidget)
        self.Connect_Arduino.setObjectName("Connect_Arduino")
        self.horizontalLayout.addWidget(self.Connect_Arduino)
        self.Disconnect_Arduino = QtWidgets.QPushButton(self.centralwidget)
        self.Disconnect_Arduino.setObjectName("Disconnect_Arduino")
        self.horizontalLayout.addWidget(self.Disconnect_Arduino)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Display = QtWidgets.QTextBrowser(self.centralwidget)
        self.Display.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Display.sizePolicy().hasHeightForWidth())
        self.Display.setSizePolicy(sizePolicy)
        self.Display.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Display.setObjectName("Display")
        self.verticalLayout_4.addWidget(self.Display)
        self.Clean_Display = QtWidgets.QPushButton(self.centralwidget)
        self.Clean_Display.setObjectName("Clean_Display")
        self.verticalLayout_4.addWidget(self.Clean_Display, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Motor_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.Motor_1.setObjectName("Motor_1")
        self.horizontalLayout_5.addWidget(self.Motor_1)
        self.Motor_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.Motor_2.setObjectName("Motor_2")
        self.horizontalLayout_5.addWidget(self.Motor_2)
        self.Both_Motor = QtWidgets.QRadioButton(self.centralwidget)
        self.Both_Motor.setObjectName("Both_Motor")
        self.horizontalLayout_5.addWidget(self.Both_Motor)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Select_Velocity_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Select_Velocity_1.setEnabled(True)
        self.Select_Velocity_1.setObjectName("Select_Velocity_1")
        self.gridLayout.addWidget(self.Select_Velocity_1, 0, 1, 1, 1)
        self.Velocity_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.Velocity_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Velocity_1.setSuffix("")
        self.Velocity_1.setMinimum(4000)
        self.Velocity_1.setMaximum(65535)
        self.Velocity_1.setSingleStep(100)
        self.Velocity_1.setProperty("value", 9000)
        self.Velocity_1.setObjectName("Velocity_1")
        self.gridLayout.addWidget(self.Velocity_1, 0, 0, 1, 1)
        self.Cycle_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Cycle_1.setObjectName("Cycle_1")
        self.gridLayout.addWidget(self.Cycle_1, 1, 0, 1, 1)
        self.Test_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Test_1.setObjectName("Test_1")
        self.gridLayout.addWidget(self.Test_1, 1, 1, 1, 1)
        self.Open_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Open_1.setObjectName("Open_1")
        self.gridLayout.addWidget(self.Open_1, 3, 0, 1, 1)
        self.Close_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Close_1.setObjectName("Close_1")
        self.gridLayout.addWidget(self.Close_1, 3, 1, 1, 1)
        self.Advance0_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Advance0_1.setObjectName("Advance0_1")
        self.gridLayout.addWidget(self.Advance0_1, 2, 1, 1, 1)
        self.Advance1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Advance1_1.setObjectName("Advance1_1")
        self.gridLayout.addWidget(self.Advance1_1, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Velocity_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.Velocity_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Velocity_2.setMinimum(4000)
        self.Velocity_2.setMaximum(65535)
        self.Velocity_2.setSingleStep(100)
        self.Velocity_2.setProperty("value", 9000)
        self.Velocity_2.setObjectName("Velocity_2")
        self.gridLayout_2.addWidget(self.Velocity_2, 0, 0, 1, 1)
        self.Test_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Test_2.setObjectName("Test_2")
        self.gridLayout_2.addWidget(self.Test_2, 1, 1, 1, 1)
        self.Cycle_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Cycle_2.setObjectName("Cycle_2")
        self.gridLayout_2.addWidget(self.Cycle_2, 1, 0, 1, 1)
        self.Select_Velocity_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Select_Velocity_2.setObjectName("Select_Velocity_2")
        self.gridLayout_2.addWidget(self.Select_Velocity_2, 0, 1, 1, 1)
        self.Open_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Open_2.setObjectName("Open_2")
        self.gridLayout_2.addWidget(self.Open_2, 3, 0, 1, 1)
        self.Close_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Close_2.setObjectName("Close_2")
        self.gridLayout_2.addWidget(self.Close_2, 3, 1, 1, 1)
        self.Advance1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Advance1_2.setObjectName("Advance1_2")
        self.gridLayout_2.addWidget(self.Advance1_2, 2, 0, 1, 1)
        self.Advance0_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Advance0_2.setObjectName("Advance0_2")
        self.gridLayout_2.addWidget(self.Advance0_2, 2, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 20))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuAjustes = QtWidgets.QMenu(self.menubar)
        self.menuAjustes.setObjectName("menuAjustes")
        self.menuAcerca_de = QtWidgets.QMenu(self.menubar)
        self.menuAcerca_de.setObjectName("menuAcerca_de")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Serial_Port = QtWidgets.QAction(MainWindow)
        self.Serial_Port.setObjectName("Serial_Port")
        self.Quit_App = QtWidgets.QAction(MainWindow)
        self.Quit_App.setObjectName("Quit_App")
        self.menuArchivo.addAction(self.Quit_App)
        self.menuAjustes.addAction(self.Serial_Port)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAjustes.menuAction())
        self.menubar.addAction(self.menuAcerca_de.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Connect_Arduino.setText(_translate("MainWindow", "Conectar"))
        self.Disconnect_Arduino.setText(_translate("MainWindow", "Desconectar"))
        self.Clean_Display.setText(_translate("MainWindow", "Limpiar"))
        self.Motor_1.setText(_translate("MainWindow", "Motor 1"))
        self.Motor_2.setText(_translate("MainWindow", "Motor 2"))
        self.Both_Motor.setText(_translate("MainWindow", "Ambos"))
        self.Select_Velocity_1.setText(_translate("MainWindow", "Seleccionar"))
        self.Velocity_1.setPrefix(_translate("MainWindow", "Velocidad: "))
        self.Cycle_1.setText(_translate("MainWindow", "Ciclo"))
        self.Test_1.setText(_translate("MainWindow", "Prueba"))
        self.Open_1.setText(_translate("MainWindow", "Abre"))
        self.Close_1.setText(_translate("MainWindow", "Cierra"))
        self.Advance0_1.setText(_translate("MainWindow", "Avanzar (0)"))
        self.Advance1_1.setText(_translate("MainWindow", "Avanzar (1)"))
        self.Velocity_2.setPrefix(_translate("MainWindow", "Velocidad: "))
        self.Test_2.setText(_translate("MainWindow", "Prueba"))
        self.Cycle_2.setText(_translate("MainWindow", "Ciclo"))
        self.Select_Velocity_2.setText(_translate("MainWindow", "Seleccionar"))
        self.Open_2.setText(_translate("MainWindow", "Abre"))
        self.Close_2.setText(_translate("MainWindow", "Cierra"))
        self.Advance1_2.setText(_translate("MainWindow", "Avanzar (1)"))
        self.Advance0_2.setText(_translate("MainWindow", "Avanzar (0)"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAjustes.setTitle(_translate("MainWindow", "Ajustes"))
        self.menuAcerca_de.setTitle(_translate("MainWindow", "Acerca de "))
        self.Serial_Port.setText(_translate("MainWindow", "Puerto "))
        self.Quit_App.setText(_translate("MainWindow", "Salir"))

