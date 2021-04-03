"""
Interfaz gráfica para control de interferómetro

Universidad Autonoma de Coahuila
Facultad de Ciencias Físico Matemáticas 

dom 21 mar 2021 12:11:39 CST 
"""
from PyQt5 import QtWidgets, QtCore, uic
from Settings import Ui_MainWindow2
from datetime import datetime
import serial, time
import sys

UI_CLASS, UI_BASE_CLASS = uic.loadUiType("Main.ui")

class MyApp(UI_CLASS, UI_BASE_CLASS):

	def __init__(self):
		
		"""
		Parámetros:
	
		Arduino_Condition: Indica el estado de conexión con arduino
		"""

		UI_BASE_CLASS.__init__(self)

		self.setupUi(self)
	
		#Ventana de ajustes-------------------------------
		
		self.Window_Settings_Port = QtWidgets.QMainWindow()
		self.Settings = Ui_MainWindow2()
		self.Settings.setupUi(self.Window_Settings_Port)
		
		#-------------------------------------------------

		self.Arduino_Condition = False	

		self.Connect_Arduino.clicked.connect(self.Connect)					#Botón "Conectar"
		self.Disconnect_Arduino.clicked.connect(self.Disconnect)				#Botón "Desconectar"
	
		self.Select_Velocity.clicked.connect(self.Select)					#Botón "Seleccionar" velocidad

		self.Clean_Display.clicked.connect(self.Display.clear)
		self.Display.append(">>> Interferómetro (" + str(datetime.now()) + ") \n")

		self.Linux = [f"/dev/ttyACM{i}" for i in range(21)]
		self.Windows = [f"C0M{i}" for i in range(21)]

		self.Serial_Port.triggered.connect(self.Window_Settings_Port.show)
		self.Serial_Port.setShortcut('Ctrl+S')

		self.Settings.Button_Windows.toggled.connect(self.Show_List)
		self.Settings.Button_Linux.toggled.connect(self.Show_List)

		self.Settings.Select_Port.clicked.connect(self.Select_Port_Serial)

	def Select_Port_Serial(self):

		self.Port_Serial = (self.Settings.Port_list.currentItem()).text()

		self.Display.append(">>> Puerto seleccionado")
		self.Display.append(">>> Puerto: " + self.Port_Serial + "\n")

	def Show_List(self):

		if self.Settings.Button_Windows.isChecked():

			self.Settings.Port_list.clear()

			for k in range(len(self.Windows)):

				self.Settings.Port_list.insertItem(k, self.Windows[k]) 

		elif self.Settings.Button_Linux.isChecked():

			self.Settings.Port_list.clear()	

			for k in range(len(self.Linux)):

				self.Settings.Port_list.insertItem(k, self.Linux[k]) 

		else: 

			self.Display.append(">>> Error al mostrar puertos \n")

	def Connect(self):
		
		"""
		Realiza conexión con arduino.
		"""

		try:

			self.arduino = serial.Serial(self.Port_Serial, baudrate=9600, timeout=1.0)
	
			self.Arduino_Condition = True

			self.Display.append(">>> Arduino conectado \n")
		
		except:

			self.Display.append(">>> Fallo al conectar con arduino \n")

	def Disconnect(self):

		"""
		Termina la conexión con arduino		
		"""

		try: 

			self.arduino.close()
			self.Arduino_Condition = False	

		except:

			pass

		finally:		

			self.Display.append(">>> Arduino desconectado \n")

	def Select(self):

		"""
		Selecciona la velocidad del motor
		"""

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
	
