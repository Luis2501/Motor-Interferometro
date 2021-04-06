/*
 Control Motor de interferómetro 

 Sin utilizar la clase Motor, solamente usamos un motor

 Cambios: La velocidad y las demás funciones se controlan 
          mediante MotorControl GIU
 */

#include <Wire.h>
#include <LCD.h>
#include <LiquidCrystal_I2C.h>
// Direcciones de lcd 0x27 y 0x3F
#define I2C_ADDR  0x3F

LiquidCrystal_I2C lcd(I2C_ADDR,2, 1, 0, 4, 5, 6, 7);
#define VELOCIDAD 65535 //255
//25000 
//20000
#define PASOS 4000

//Definición de pines para Motor 1:
int cuenta_Hall1 = 2; //Cuenta Sensor Hall1 Motor 1 (Pin de interrupciones)
int DIR_M1 =7; //Dirección Motor 1
int PWM_M1 = 9; //PWM Motor 1
char opcion='0';
unsigned long t1, t2;
float tiempo;
int Velocidad;
int cont=0;
String bufferString = "";           //Variable para almacenar la velocidad

//Definición de variables para controlar Motor 1:
int dirM1 = 0; //Variable para introducir dirección
int dir_flagM1 = 0; //Variable para dar de alta o de baja la dirección
unsigned int pwmM1; //Variable para introducir valor de pwm
int pwm_flagM1 = 0; //Variable para dar de alta o baja el pwm
int pasos_flagM1 = 0; //Variable para dar de alta o baja el tiempo


//Definición de variables del Arduino motor 1:
volatile float ctaPWM1 = 0; //Variable que llevará la cuenta de los pasos del motor 1
float cta_antPWM1 = 0; //Variable para definir la cuenta anterior del motor 1
float pasosM1=0;
float contM1;
/*
//Definición de pines para Motor 2:
int cuenta_Hall2 = 3; //Cuenta Sensor Hall Motor 2
int DIR_M2 = 4; //Dirección Motor 2
unsigned int PWM_M2 = 10; //PWM Motor 2

//Definición de variables para controlar Motor 2:
int dirM2 = 0; //Variable para introducir dirección
int dir_flagM2 = 0; //Variable para dar de alta o de baja la dirección
unsigned int pwmM2; //Variable para introducir valor de pwm
int pwm_flagM2 = 0; //Variable para dar de alta o baja el pwm
int pasos_flagM2 = 0; //Variable para dar de alta o baja el tiempo

//Definición de variables del Arduino motor 2:
volatile float ctaPWM2 = 0; //Variable que llevará la cuenta de los pasos del motor 2
float cta_antPWM2 = 0; //Variable para definir la cuenta anterior del motor 2
float pasosM2=0;
float contM2;
*/
void setup()
{
  //lcd
       lcd.begin (16,2);    // Inicializar el display con 16 caraceres 2 lineas
       lcd.setBacklightPin(3,POSITIVE);
       lcd.setBacklight(HIGH);
       lcd.home ();                   // go home
       lcd.print("INICIALIZANDO");
       delay(1000);
       lcd.clear();
       lcd.setCursor ( 0, 0 );        // go to the 2nd line
       lcd.print("FCFM UADEC" );
       lcd.setCursor(0,1);
       lcd.print("2020 D.R.");
       delay(2000);
       lcd.clear();
       lcd.print("EN ESPERA ");
       lcd.setCursor(0,1);
       Velocidad=VELOCIDAD;
       delay(1500);
       //lcd.clear();
       //lcd.setCursor(0,0);
       
  //PWM 16 BITS
  // put your setup code here, to run once:
digitalWrite(PWM_M1,LOW); //
//digitalWrite(PWM_M2,LOW); 
delay(1000); 
DDRB |= _BV(PB1) | _BV(PB2); /* fija los pines del puerto B como salida */
TCCR1A = _BV(COM1A1) | _BV(COM1B1) /* PWM no invertido */
| _BV(WGM11); /* mode 14: fast PWM, TOP=ICR1 */
TCCR1B = _BV(WGM13) | _BV(WGM12)
| _BV(CS11); /* prescaler 1 */
ICR1 = 0xffff; //cuenta para 16 bits 
//ICR1=0x3ff;  //Cuenta para 10 Bits
//ICR1=0x0fff; // Cuenta para 12 Bits
//ICR1=0x3fff; //cuenta para 14 bits
/* TOP counter value (freeing OCR1A*/


  Serial.begin(9600); //Abre la conexión con el puerto serie 
  attachInterrupt(digitalPinToInterrupt(cuenta_Hall1), cuentaM1, FALLING);
  //attachInterrupt(digitalPinToInterrupt(cuenta_Hall2), cuentaM2, FALLING); //quitar comentario inicial para dos motores
  interrupts(); 

  //Definición de entrada o salida de los pines del Motor 1:
  pinMode(cuenta_Hall1, INPUT); //Define Cuenta Sensor Hall Motor 1 como ENTRADA
  pinMode(DIR_M1, OUTPUT); //Define Dirección del Motor 1 como SALIDA
 

  // Definición de entrada o salida de los pines del Motor 2:
  // pinMode(cuenta_Hall2, INPUT); //Define Cuenta Sensor Hall Motor 2 como ENTRADA
  // pinMode(DIR_M2, OUTPUT); //Define Dirección del Motor 2 como SALIDA
 
  dirM1=HIGH; 
  //dirM2=HIGH;
}

void cuentaM1() //RUTINA DE INTERRUPCIÓN
{
  ctaPWM1++;
}
/*
void cuentaM2() //RUTINA DE INTERRUPCIÓN
{
  ctaPWM2 ++;
}
*/

void analogWrite16(uint8_t pin, uint16_t val)  //Rutina para el PWM con resolución mayor a 8 bits
{
  switch (pin) 
  {
    case 9: OCR1A = val; break;
    case 10: OCR1B = val; break;
  }
}

void ciclo()
{ //Realiza un ciclo ida y vuelta. Usar la letra C para activarlo
    ctaPWM1 = 0;
    //ctaPWM2 = 0;
    digitalWrite(DIR_M1, dirM1); 
    //digitalWrite(DIR_M2, dirM2); 
    //analogWrite16(PWM_M2, 10000);
    lcd.clear();
    pwmM1=Velocidad;//65535;//
    lcd.print("PWM:");
    lcd.print(pwmM1);
    pwm_flagM1=1;
    dirM1=0;
    dir_flagM1=1;
    lcd.print(" Dir:");
    lcd.print(dir_flagM1);
    pasosM1=PASOS;
    pasos_flagM1=1;
    lcd.setCursor(0,1);
    lcd.print("PASOS:");
    lcd.print(pasosM1,0);
    lcd.print(" ");
    lcd.print("ON");
    digitalWrite(DIR_M1, dirM1); //Da el valor a la Dirección del Motor 1
    analogWrite16(PWM_M1, pwmM1); //Da el valor PWM al Motor 1
    while (ctaPWM1<pasosM1);
      //analogWrite16(PWM_M1, pwmM1); //Valor de pwm del Motor 1
    analogWrite16(PWM_M1, 0); //Valor de 0 al pwm para que pare
    t2=millis();
    delay(1000);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Regreso");
 
    cta_antPWM1 = ctaPWM1; //Asigna valor de cuenta a la cuenta anterior
    ctaPWM1 = 0;
    dirM1 = !dirM1; //Cambia el valor de dirección
    //dirM2= !dirM2;
    lcd.setCursor(0,1);
    lcd.print("Dir: ");
    lcd.print(dirM1);
    digitalWrite(DIR_M1, dirM1); //Da el nuevo valor de Dirección del Motor 1
    analogWrite16(PWM_M1, pwmM1); //Valor de pwm del Motor 1
    while (ctaPWM1 < cta_antPWM1); //Ciclo para regresar a la misma posición
      //analogWrite16(PWM_M1, pwmM1); //Valor de pwm del Motor 1
    analogWrite16(PWM_M1, 0); //Valor de 0 al pwm para que pare
    delay(1000);
    lcd.setCursor(0,1);
    lcd.print("FIN DEL PROCESO");
    delay(500);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("EN ESPERA ");
    delay(500);
    //lcd.clear();
}

void avanza(int dir)
{
   lcd.clear();
   lcd.print(dir);
   digitalWrite(DIR_M1, dir);
   ctaPWM1 = 0;
   analogWrite16(PWM_M1, Velocidad);
   while(ctaPWM1 < 1000);
     
     //opcion='0';
   
}
void abre(void)
{
   lcd.clear();
   lcd.print("Abre");
   digitalWrite(DIR_M1, 1);
   ctaPWM1 = 0;
   analogWrite16(PWM_M1, Velocidad);
   while(ctaPWM1 < 10);
     
     //opcion='0';
   
}

void cierra(void)
{
   lcd.clear();
   lcd.print("Cierra");
   digitalWrite(DIR_M1, 0);
   ctaPWM1 = 0;
   analogWrite16(PWM_M1, Velocidad);
   while(ctaPWM1 < 10);
     
     //opcion='0';
   
}
void prueba()
{
  int i;
  lcd.clear();
  lcd.print("PWM: ");
  for (i=0;i<=65500;i+=100)
      {
        analogWrite16(PWM_M1, i);
        lcd.setCursor(0,1);
        lcd.print(i);
        delay(200);
      }
  
}

void loop()
{
  if(Serial.available()>0)
  {
    opcion=Serial.read();
    Serial.flush();
    lcd.clear();
    lcd.print(opcion);
    switch(opcion)
    {
      case 'C':
        delay(100);
        t1=millis();
        ciclo();
        //t2=millis();
        tiempo=(t2-t1)/1000;
        Serial.print("Tiempo Transcurrido: ");
        Serial.println(tiempo,2);
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
        Serial.println(Velocidad);
    
        delay(2000);
        
      case 'x':
        cont=0;
        lcd.clear();
        lcd.print("Contador = 0");
        delay(10);
        break;
      default: 
        analogWrite16(PWM_M1, 0);
        break;
    }
  
  }
  //Inicializa las cuentas de PWM en 0
 /*/ 
  while (pwm_flagM1 == 0)
  {
    /*if (Serial.available() > 0)
    {
      lcd.clear();
      pwmM1=Serial.read();//Lee datos desde el puerto serie para el valor de PWM del Motor 1
      pwm_flagM1 = 1;
      lcd.setCursor(0,0);
      lcd.print("PWM: ");
      lcd.print(pwmM1);
      
      delay(1000);
    }
    // Quitar para prueba
    
    // fin
  }
  while (dir_flagM1 == 0)
  { /*
    if (Serial.available() > 0)
    {
      dirM1=Serial.read();
      dir_flagM1 = 1;
      lcd.print(" ");
      lcd.print(pwm_flagM1); 
      delay(1000);
    }
    //  Quitar para prueba
    
 }
 while (pasos_flagM1 == 0)
 { /*
    if (Serial.available() > 0)
    {
      pasosM1=Serial.read();
      pasos_flagM1 = 1;
      lcd.setCursor(0,1);
      lcd.print("Pasos: ");
      lcd.print(pasosM1);
      delay(1000);
    }
    
 }
 
 dir_flagM1 = 0;
 pwm_flagM1 = 0;
 pasos_flagM1 = 0;
  //Quitar para prueba
  //while(1);*/
}
