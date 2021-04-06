/*
Código Motor de interferómetro

Utilizando la clase Motor, para controlar uno o más motores
 */

#include <Wire.h>
#include <LCD.h>
#include <LiquidCrystal_I2C.h>

unsigned long ti,tf;
float tiempo; 

String bufferString = "";
int Velocidad;

void setup() {
  


}

void loop() {

  if(Serial.available()>0){
    
    opcion=Serial.read();
    Serial.flush();
    lcd.clear();
    lcd.print(opcion);
    
    switch(opcion){
      
      case 'C':
      
        delay(100);
        ti=millis();
        
        ciclo();
        
        tf = millis();
        tiempo=(tf-ti)/1000;
        
        Serial.print("Tiempo Transcurrido: ");
        Serial.println(tiempo, 2);
        
        break;
        
      case 'F':
      
        //for(int i=0;i<50;i++)
          avanza(1);
        break;
        
      case 'B':
        avanza(0);
        break;
        
      case 'a':
      
        abre();
        Serial.println(--cont);
        break;
        
      case 'c':
      
        cierra();
        Serial.println(++cont);
        break;  
          
      case 'P':
      
        prueba();
        break; 
         
      case 'V':
      
         delay(2000);
         
         while (Serial.available() > 0) {
             bufferString += (char)Serial.read();
         }
            
         //Se transforma el buffer a un número entero
         Velocidad = bufferString.toInt();
         //Se imprime el número que se recibe
          
         Serial.print("Vel: ");
         Serial.println(Velocidad);
            
         delay(2000);
            
         lcd.setCursor(13,3);
         lcd.print(Velocidad);         

         break;
        
      case 'x':
      
        cont=0;
        lcd.clear();
        lcd.print("Contador = 0");
        delay(10);
        break;
        
      default:
       
        analogWrite16(PWM_M1, 0);
        
        break;
        
    }//Fin de switch
    
   }//Fin de if 

}//Fin de función loop
