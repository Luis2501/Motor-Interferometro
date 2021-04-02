"""
Interfaz gráfica para control de interferómetro

Universidad Autonoma de Coahuila
Facultad de Ciencias Físico Matemáticas 

dom 21 mar 2021 12:11:39 CST 
"""
from datetime import datetime
from Settings import Ui_MainWindow2
from PyQt5 import QtWidgets, QtCore, uic
import serial, time
import sys

UI_CLASS, UI_BASE_CLASS = uic.loadUiType("Main.ui")

class MyApp(UI_CLASS, UI_BASE_CLASS):

	def __init__(self):

		UI_BASE_CLASS.__init__(self)

		self.setupUi(self)
	
		#Ventana de ajustes
		
		self.Window_Settings_Port = QtWidgets.QMainWindow()
		self.Settings = Ui_MainWindow2()
		self.Settings.setupUi(self.Window_Settings_Port)
		
		#--------------

		self.Arduino_Condition = False

		self.Connect_Arduino.clicked.connect(self.Connect)
		self.Disconnect_Arduino.clicked.connect(self.Disconnect)

		self.Select_Velocity.clicked.connect(self.Select)

		self.Clean_Display.clicked.connect(self.Display.clear)
		self.Display.append(">>> Interferómetro (" + str(datetime.now()) + ") \n")

		self.Linux = [f"/dev/ttyACM{i}" for i in range(21)]
		self.Windows = [f"C0M{i}" for i in range(21)]

		self.Serial_Port.triggered.connect(self.Window_Settings_Port.show)
		self.Serial_Port.setShortcut('Ctrl+S')

		self.Settings.Button_Windows.toggled.connect(self.Show_List)
		self.Settings.Button_Linux.toggled.connect(self.Show_List)

	def Show_List(self, System):

		if self.Settings.Button_Windows.isChecked():

			for k in range(len(self.Windows)):

				self.Settings.Port_list.insertItem(k, self.Windows[k]) 

		elif self.Settings.Button_Linux.isChecked():

			for k in range(len(self.Linux)):

				self.Settings.Port_list.insertItem(k, self.Linux[k]) 

		else: 

			self.Display.append(">>> Error al mostrar puertos \n")

	def Connect(self):
		
		"""
		Realiza conexión con arduino.
		"""

		self.Arduino_Condition = True
		
		self.arduino = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=1.0)
	
		self.Display.append(">>> Arduino conectado \n")

	def Disconnect(self):

		"""
		Termina la conexión con arduino		
		"""

		self.Arduino_Condition = False

		self.arduino.close()

		self.Display.append(">>> Arduino desconectado \n")

	def Select(self):

		if self.Arduino_Condition:

			self.arduino.write(b'V')
			self.arduino.write(bytes(str(self.Velocity.value()), "utf-8"))

			self.Display.append(">>> Velocidad seleccionada")
			self.Display.append(">>> Vel: " + str(self.Velocity.value()) + "\n")

		else:

			self.Display.append(">>> Arduino no conectado \n")

if __name__ == '__main__':					

	app = QtWidgets.QApplication(sys.argv)

	window = MyApp()
	#window.resize(600, 600)
	#window.move(300, 300)
	window.setWindowTitle("Control interferómetro")

	window.show()

	sys.exit(app.exec_())
	
