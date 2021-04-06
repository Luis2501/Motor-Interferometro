"""
Interfaz gráfica para control de interferómetro

Universidad Autonoma de Coahuila
Facultad de Ciencias Físico Matemáticas 

dom 21 mar 2021 12:11:39 CST 
"""

from PyQt5 import QtWidgets, QtCore, uic
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

