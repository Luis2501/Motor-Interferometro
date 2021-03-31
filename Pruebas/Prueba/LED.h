class LED{

	public:
            
		void LED::Encender(int pin){

  			digitalWrite(pin, HIGH);
		}

		void LED::Apagar(int pin){

  		digitalWrite(pin, LOW);
		}
		

};
