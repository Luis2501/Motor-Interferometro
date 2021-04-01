"""
Interfaz gráfica para control de interferómetro (Demo) con Tkinter

Universidad Autonoma de Coahuila
Facultad de Ciencias Físico Matemáticas 

dom 21 mar 2021 12:11:39 CST 
"""

from tkinter import *  
import serial, time

def ON():

	time.sleep(2)

	arduino.write(b'S')


def OFF():

	time.sleep(2)

	arduino.write(b'N')

def Velocity():

	print(Velocidad.get())

root = Tk()
root.title("Motor interferómetro")
#arduino = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=1.0)

Velocidad = Scale(root, label = "Velocidad", from_= 4000, to =10000, tickinterval= 1000, resolution = 100, 
			length= 400, orient = "horizontal")
Velocidad.pack(padx = 20, pady = 20)

Encendido = Button(root, text = "INICIAR", command = ON).pack(padx = 20, pady = 20)
Apagado = Button(root, text = "APAGAR", command = OFF).pack(padx = 20, pady = 20)

Set_Velocity = Button(root, text = "Aceptar", command = Velocity).pack(padx = 20, pady = 20)

root.mainloop()
