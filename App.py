"""
Interfaz gráfica para control de interferómetro

Universidad Autonoma de Coahuila
Facultad de Ciencias Físico Matemáticas 

dom 21 mar 2021 12:11:39 CST 
"""
from PyQt5 import QtWidgets, QtCore
import serial, time
import sys

class MyApp(QtWidgets.QWidget):
    
	def __init__(self):
     
		QtWidgets.QWidget.__init__(self)

		self.edit = QtWidgets.QLineEdit("")
		self.edit.setClearButtonEnabled(False)       		

		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(self.edit)

		First_Layout = QtWidgets.QVBoxLayout()
		Second_Layout = QtWidgets.QHBoxLayout()

		self.setLayout(First_Layout)
		First_Layout.addLayout(layout)								#Ubicamos el Layout en la Widget
		First_Layout.addLayout(Second_Layout)

		self.Select_Vel = QtWidgets.QLabel("Selector de velocidad")
		self.Select_Vel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
		First_Layout.addWidget(self.Select_Vel)

		self.Velocity = QtWidgets.QSpinBox()							#Spin Box para la velocidad
		First_Layout.addWidget(self.Velocity)							#Agregamos Spin Box a layout
        
	        #Ajustes del Spin Box (Velocity)
		self.Velocity.setMaximum(20000)
		self.Velocity.setMinimum(4000)
		self.Velocity.setSingleStep(100)
		self.Velocity.setPrefix("Vel = ")
		self.Velocity.setSuffix(" steps")
		self.Velocity.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)

		self.Vel = QtWidgets.QPushButton("Seleccionar")
		First_Layout.addWidget(self.Vel) 	
		self.Vel.clicked.connect(self.Select)

		self.Conectar = QtWidgets.QPushButton('Conectar')
		Second_Layout.addWidget(self.Conectar)
		self.Conectar.clicked.connect(self.Connect)
		
		self.Encender = QtWidgets.QPushButton('Encender')
		Second_Layout.addWidget(self.Encender)
		self.Encender.clicked.connect(self.ON)

		self.Apagar = QtWidgets.QPushButton('Apagar')
		Second_Layout.addWidget(self.Apagar)
		self.Apagar.clicked.connect(self.OFF)

	def To_Select_Velocity(self):

		"""
		Crea layout donde se encontrará el selector de velocidad.
		"""

		pass

	def Connect(self):
		
		self.arduino = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=1.0)

	def Select(self):

		self.arduino.write(b'V')
		print("Velocidad Seleccionada")
		print(self.Velocity.value())	
		self.arduino.write(bytes(str(self.Velocity.value()), "utf-8"))

	def ON(self):

		self.arduino.write(b'S')

	def OFF(self):

		self.arduino.write(b'N')

if __name__ == '__main__':					

	app = QtWidgets.QApplication(sys.argv)

	window = MyApp()
	#window.resize(600, 600)
	#window.move(300, 300)
	window.setWindowTitle("Control interferómetro")

	window.show()

	sys.exit(app.exec_())
