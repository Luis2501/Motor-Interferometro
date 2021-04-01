class LED{

	public:
            
		int PIN;

		LED::LED(int pin);

		void LED::Encender();		
		void LED::Apagar();

};

LED::LED(int pin){

	PIN = pin;

}

void LED::Encender(){

	digitalWrite(PIN, HIGH);

}

void LED::Apagar(){

	digitalWrite(PIN, LOW);

}
