#include <Wire.h>
#include <LCD.h>
#include <LiquidCrystal_I2C.h>

unsigned long ti,tf;
float tiempo; 

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
      
        vel=vel + 100;
        Serial.print("Vel: ");
        Serial.println(vel);
        break;
        
      case 'v':
        vel=vel- 100;
        Serial.print("Vel: ");
        Serial.println(vel);
        break;
      case 'm':
        vel=9000;
        Serial.print("Vel: ");
        Serial.println(vel);
        break;
      case 'M':
        vel = VELOCIDAD;
        Serial.print("Vel: ");
        Serial.println(vel);
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
