"""
Interfaz gráfica para control de interferómetro

Universidad Autonoma de Coahuila
Facultad de Ciencias Físico Matemáticas 

dom 21 mar 2021 12:11:39 CST 
"""

from datetime import datetime
from PyQt5 import QtWidgets, QtCore, uic
import serial, time
import sys

UI_CLASS, UI_BASE_CLASS = uic.loadUiType("Main.ui")

class MyApp(UI_CLASS, UI_BASE_CLASS):

	def __init__(self):

		UI_BASE_CLASS.__init__(self)

		self.setupUi(self)
	
		self.Arduino_Condition = False

		self.Connect_Arduino.clicked.connect(self.Connect)
		self.Disconnect_Arduino.clicked.connect(self.Disconnect)

		self.Select_Velocity.clicked.connect(self.Select)

		self.Clean_Display.clicked.connect(self.Display.clear)
		self.Display.append(">>> Interferómetro (" + str(datetime.now()) + ") \n")

	def Connect(self):

		self.Arduino_Condition = True
		
		self.arduino = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=1.0)
	
		self.Display.append(">>> Arduino conectado \n")

	def Disconnect(self):
	
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
	
