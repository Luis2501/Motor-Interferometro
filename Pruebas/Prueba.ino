char opcion1 = '0';

void setup() {
  
  Serial.begin(9600);
  pinMode(13, OUTPUT);

}

void loop(){
  
  if(Serial.available()>0){
    
    opcion1=Serial.read();
    Serial.flush();
    
    switch(opcion1){
      
      case 'S':
      
        digitalWrite(13, HIGH);
      
        break;
        
      case 'N':
      
           digitalWrite(13, LOW);
           
        break;

      default:

           Serial.print("No se selecciono nada ");

       break;
        
    }//Fin Switch
    
  }
  
}
