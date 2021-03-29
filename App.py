"""
Interfaz gráfica

Universidad Autonoma de Coahuila
Facultad de Ciencias Físico Matemáticas 

dom 21 mar 2021 12:11:39 CST 
"""
import sys
import serial, time
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

class MyApp(QtWidgets.QWidget):
    
	def __init__(self):
     
		QtWidgets.QWidget.__init__(self)

		layout = QtWidgets.QGridLayout()
		self.setLayout(layout)

		menubar = QtWidgets.QMenuBar()
		layout.addWidget(menubar, 0, 0)
		actionFile = menubar.addMenu("File")
		actionFile.addAction("New")
		actionFile.addAction("Open")
		actionFile.addAction("Save")
		actionFile.addSeparator()
		actionFile.addAction("Quit")
		menubar.addMenu("Edit")
		menubar.addMenu("View")
		menubar.addMenu("Help")

		Encender = QtWidgets.QPushButton('Encender', self)
		Encender.clicked.connect(self.ON)
		Encender.move(200, 200)
		Encender.show()

		Apagar = QtWidgets.QPushButton('Apagar', self)
		Apagar.clicked.connect(self.OFF)
		Apagar.move(300, 200)
		Apagar.show()

	def ON(self):

		arduino.write(b'S')

	def OFF(self):

		arduino.write(b'N')

if __name__ == '__main__':					

	app = QtWidgets.QApplication(sys.argv)

	#arduino = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=1.0)

	window = MyApp()

	window.resize(600, 600)
	#window.move(300, 300)
	window.setWindowTitle("Control interferómetro")

	window.show()

	sys.exit(app.exec_())
