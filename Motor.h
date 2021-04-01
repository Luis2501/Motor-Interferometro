/*
Clase Motor para controlar multiples motores

Universidad Autonoma de Coahuila
Facultad de Ciencias Físico Matemáticas 

mié 31 mar 2021 17:18:56 CST 
*/

class Motor{

	public: 
	
		//Definición de pines
		int Cuenta_Hall;		//Cuenta sensor Hall (Pin de interrupciones)
        	int Direccion;			//Dirección motor (pin)
        	int PWM;                	//PWM motor (pin)

		volatile int Cuenta_PWM;			//Cuenta PWM

		Motor(int cta_h, int dir, int pwm);
		void Motor::Cuenta();
        	void Motor::Ciclo(); 
		void Motor::Prueba();

};

/*Constructor de la clase*/

Motor::Motor(int cta_h, int dir, int pwm){

	Cuenta_Hall = cta_h;
	Direccion = dir;
	PWM = pwm;
	Cuenta_PWM = 0;
	
	digitalWrite(PWM, LOW); 
	delay(1000); 

	DDRB |= _BV(PB1) | _BV(PB2); 		/* fija los pines del puerto B como salida */
	TCCR1A = _BV(COM1A1) | _BV(COM1B1) 	/* PWM no invertido */
	| _BV(WGM11); 				/* mode 14: fast PWM, TOP=ICR1 */
	TCCR1B = _BV(WGM13) | _BV(WGM12)
	| _BV(CS11); 				/* prescaler 1 */
	ICR1 = 0xffff; 				//cuenta para 16 bits 

	attachInterrupt(digitalPinToInterrupt(Cuenta_Hall), Cuenta, FALLING);
	interrupts(); 

	//Definición de entrada o salida de los pines del Motor:

  	pinMode(Cuenta_Hall, INPUT); 		//Define Cuenta Sensor Hall Motor 1 como ENTRADA
  	pinMode(Direccion, OUTPUT); 		//Define Dirección del Motor 1 como SALIDA

}

void Motor::Cuenta(){

	Cuenta_PWM++;
}

void Motor::Prueba(){

	lcd.clear();
	lcd.print("PWM: ");
		
	for(int i=0; i<= 65500; i+=100){
			
		analogWrite16(PWM, i);
		lcd.setCursor(0,1);
		lcd.print(i);
		delay(200);

	}//Fin de ciclo for

}//Fin de función prueba 
