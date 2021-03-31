#include<LCD.h>
#include <Wire.h>  // Lo trae Arduino IDE
#include <LiquidCrystal_I2C.h> // Incluimos la libreria del LCD
#include "LED.h"

LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);  // Seteamos la direccion I2C

LED led;

char opcion1 = '0';
int data;

void setup() {

  lcd.begin(20,4); 
  Serial.begin(9600);
  Serial.setTimeout(1000);
  pinMode(13, OUTPUT);
 
  lcd.setCursor(3,0); //Empiezo en la posicion 1 (caracter) sobre la linea 0
  lcd.print("Bienvenido");
  lcd.setCursor(1,1);
  lcd.print("Esto es una prueba");  

}

int Suma(int num){
  return num + num;
}

void loop(){
  
  if(Serial.available()>0){
    
    opcion1=Serial.read();
    Serial.flush();
    
    switch(opcion1){
      
      case 'S':
      
            led.Encender(13);
      
        break;
        
      case 'N':
      
           led.Apagar(13);
           
        break;

      case 'V':

            lcd.setCursor(1,3);
            lcd.print("Velocidad: "); 
            
            delay(2000);
            String bufferString = "";

            while (Serial.available() > 0) {
                bufferString += (char)Serial.read();
            }
            
            //Se transforma el buffer a un número entero
            int num = bufferString.toInt();
            //Se imprime el número que se recibe
            //Serial.print("Numero recibido: ");
            Serial.println(num);

            Serial.println(Suma(num));
            
            delay(2000);
            lcd.setCursor(13,3);
            lcd.print(num);         

            break;

      default:

           Serial.println("No se selecciono nada");

           break;
        
    }//Fin Switch
    
  }
  
}
