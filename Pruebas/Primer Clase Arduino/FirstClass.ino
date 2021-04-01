class LED{

  public: 

    int pin;
    void LED::Enceder();
    void LED::Apagar();

  private;
  
};

void LED::Enceder(){

  digitalWrite(pin, HIGH);
}

void LED::Apagar(){

  digitalWrite(pin, LOW);
}
