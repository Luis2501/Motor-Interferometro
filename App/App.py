#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Interfaz gráfica para control de interferómetro

Universidad Autonoma de Coahuila
Facultad de Ciencias Físico Matemáticas 

dom 21 mar 2021 12:11:39 CST 
"""
from PyQt5 import QtWidgets, QtCore, QtGui, uic
#from Settings import Ui_MainWindow2
from Main import Ui_MainWindow
from datetime import datetime
import serial, time
import sys

class Motor:

	def Select(self):

		if self.Arduino_Condition:

			self.arduino.write(b'V')
			self.arduino.write(bytes(str(self.Velocity_1.value()), "utf-8"))

			self.Display.append(">>> Velocidad seleccionada")
			self.Display.append(">>> Vel: " + str(self.Velocity_1.value()) + "\n")

		else:

			self.Display.append(">>> Arduino no conectado \n")

	def Select_Cycle(self):

		if self.Arduino_Condition:

			self.arduino.write(b'C')

			self.Display.append(">>> Iniciando ciclo")

		else:

			self.Display.append(">>> Arduino no conectado \n")

	def Test(self):

		if self.Arduino_Condition:

			self.arduino.write(b'P')

			self.Display.append(">>> Iniciando prueba")

		else:

			self.Display.append(">>> Arduino no conectado \n")

	def Advance1(self):

		if self.Arduino_Condition:

			self.arduino.write(b'F')

			self.Display.append(">>> Avanzando")

		else:

			self.Display.append(">>> Arduino no conectado \n")

	def Advance0(self):

		if self.Arduino_Condition:

			self.arduino.write(b'B')

			self.Display.append(">>> Avanzando")

		else:

			self.Display.append(">>> Arduino no conectado \n")

	def Open(self):

		if self.Arduino_Condition:

			self.arduino.write(b'a')

			self.Display.append(">>> Abriendo")

		else:

			self.Display.append(">>> Arduino no conectado \n")

	def Close(self):

		if self.Arduino_Condition:

			self.arduino.write(b'c')

			self.Display.append(">>> Cerrando")

		else:

			self.Display.append(">>> Arduino no conectado \n")


#UI_CLASS, UI_BASE_CLASS = uic.loadUiType("Main.ui")				#Se utiliza siempre que se hacen cambios

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow, Motor):

#class MyApp(UI_CLASS, UI_BASE_CLASS, Motor):

	def __init__(self):

		#UI_BASE_CLASS.__init__(self)
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)

		self.setupUi(self)
	
		self.setWindowIcon(QtGui.QIcon('Motor.png'))	
		
		#Ventana de ajustes------------------------------- **Si se requiere**
		
		#self.Window_Settings_Port = QtWidgets.QMainWindow()
		#self.Settings = Ui_MainWindow2()
		#self.Settings.setupUi(self.Window_Settings_Port)

		#self.Serial_Port.triggered.connect(self.Window_Settings_Port.show)

		#self.Settings.Button_Windows.toggled.connect(self.Show_List)
		#self.Settings.Button_Linux.toggled.connect(self.Show_List)

		#self.Settings.List_Port.activated[str].connect(self.Select_Port_Serial)
		
		#Botón de Archivo----------------------------------

		self.Quit_App.triggered.connect(app.quit)

		#Condiciones inciales------------------------------

		self.Arduino_Condition = False	

		self.Button_Connection() 

		self.Serial = [f"/dev/ttyACM{i}" for i in range(21)] + [f"COM{i}" for i in range(21)]  
		self.Serial += [f"/dev/ttyUSB{i}" for i in range(21)]

		self.Clean_Display.clicked.connect(self.Clean)
		self.Display.append(">>> MotorControl GIU (" + str(datetime.now()) + ") \n")		
	
	def Button_Connection(self):

		self.Buttons = [self.Select_Velocity_1, self.Cycle_1, self.Test_1, 
				self.Advance1_1, self.Advance0_1, self.Open_1, self.Close_1,
				self.Select_Velocity_2, self.Cycle_2, self.Test_2, 
				self.Advance1_2, self.Advance0_2, self.Open_2, self.Close_2,]

		self.Connect_Arduino.clicked.connect(self.Connect)					#Botón "Conectar"
		self.Disconnect_Arduino.clicked.connect(self.Disconnect)				#Botón "Desconectar"
	
		#Solo emiten señales los botones del motor 1
		self.Select_Velocity_1.clicked.connect(self.Select)					
		self.Cycle_1.clicked.connect(self.Select_Cycle)
		self.Test_1.clicked.connect(self.Test)
		self.Advance1_1.clicked.connect(self.Advance1)
		self.Advance0_1.clicked.connect(self.Advance0)
		self.Open_1.clicked.connect(self.Open)
		self.Close_1.clicked.connect(self.Close)

		for Button in self.Buttons:

			Button.setEnabled(False)

		self.Motor_1.toggled.connect(self.Select_Motor)
		self.Motor_2.toggled.connect(self.Select_Motor)
		self.Both_Motor.toggled.connect(self.Select_Motor)


	def Clean(self):

		self.Display.clear()
		self.Display.append(">>> MotorControl GIU (" + str(datetime.now()) + ") \n")

	def Select_Motor(self):

		if self.Motor_1.isChecked():

			for i in range(14):

				if i < 7: self.Buttons[i].setEnabled(True)
				else: self.Buttons[i].setEnabled(False)

		elif self.Motor_2.isChecked():

			for i in range(14):

				if i < 7: self.Buttons[i].setEnabled(False)
				else: self.Buttons[i].setEnabled(True)

		elif self.Both_Motor.isChecked():
		
			for i in range(14):

				self.Buttons[i].setEnabled(True)		

	def Connect(self):

		for Port, i in zip(self.Serial, range(len(self.Serial))):

			try:

				self.arduino = serial.Serial(Port, baudrate=9600, timeout=1.0)
	
				self.Display.append(">>> Puerto seleccionado")
				self.Display.append(">>> Puerto: " + Port + "\n")
		
				self.Arduino_Condition = True

				self.Display.append(">>> Arduino conectado \n")
		
				break

			except:
			
				if i == (len(self.Serial) -1):

					self.Display.append(">>> Fallo al conectar con arduino \n") 

				pass

	def Disconnect(self):

		try: 

			self.arduino.close()
			self.Arduino_Condition = False	

			self.Display.append(">>> Arduino desconectado \n")

		except:

			self.Display.append(">>> Arduino no conectado \n")		

if __name__ == '__main__':					

	app = QtWidgets.QApplication(sys.argv)

	window = MyApp()
	window.setWindowTitle("MotorControl GIU")
	window.show()

	sys.exit(app.exec_())
	
