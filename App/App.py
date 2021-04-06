"""
Interfaz gráfica para control de interferómetro

Universidad Autonoma de Coahuila
Facultad de Ciencias Físico Matemáticas 

dom 21 mar 2021 12:11:39 CST 
"""
from PyQt5 import QtWidgets, QtCore, uic
from Settings import Ui_MainWindow2
from datetime import datetime
from Motor import Motor
import serial, time
import sys

UI_CLASS, UI_BASE_CLASS = uic.loadUiType("Main.ui")

class MyApp(UI_CLASS, UI_BASE_CLASS, Motor):

	def __init__(self):

		UI_BASE_CLASS.__init__(self)

		self.setupUi(self)
	
		#Ventana de ajustes-------------------------------
		
		self.Window_Settings_Port = QtWidgets.QMainWindow()
		self.Settings = Ui_MainWindow2()
		self.Settings.setupUi(self.Window_Settings_Port)

		self.Linux = [f"/dev/ttyACM{i}" for i in range(21)]
		self.Windows = [f"C0M{i}" for i in range(21)]

		self.Serial_Port.triggered.connect(self.Window_Settings_Port.show)

		self.Settings.Button_Windows.toggled.connect(self.Show_List)
		self.Settings.Button_Linux.toggled.connect(self.Show_List)

		self.Settings.List_Port.activated[str].connect(self.Select_Port_Serial)
		
		#Condiciones inciales------------------------------

		self.Arduino_Condition = False	

		self.Button_Connection()

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

	def Select_Port_Serial(self, Port_Serial):

		self.Port_Serial = Port_Serial

		self.Display.append(">>> Puerto seleccionado")
		self.Display.append(">>> Puerto: " + self.Port_Serial + "\n")

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

	def Show_List(self):

		if self.Settings.Button_Windows.isChecked():

			self.Settings.List_Port.clear()

			for k in range(len(self.Windows)):

				self.Settings.List_Port.addItem(self.Windows[k]) 

		elif self.Settings.Button_Linux.isChecked():

			self.Settings.List_Port.clear()	

			for k in range(len(self.Linux)):

				self.Settings.List_Port.addItem(self.Linux[k]) 

		else: 

			self.Display.append(">>> Error al mostrar puertos \n")

	def Connect(self):

		try:

			self.arduino = serial.Serial(self.Port_Serial, baudrate=9600, timeout=1.0)
	
			self.Arduino_Condition = True

			self.Display.append(">>> Arduino conectado \n")
		
		except:

			self.Display.append(">>> Fallo al conectar con arduino \n")

	def Disconnect(self):

		try: 

			self.arduino.close()
			self.Arduino_Condition = False	

		except:

			pass

		finally:		

			self.Display.append(">>> Arduino desconectado \n")


if __name__ == '__main__':					

	app = QtWidgets.QApplication(sys.argv)

	window = MyApp()
	window.setWindowTitle("MotorControl GIU")
	window.show()

	sys.exit(app.exec_())
	
