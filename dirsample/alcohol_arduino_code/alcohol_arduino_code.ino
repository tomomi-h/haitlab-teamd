#define analogInDatPin 0

#define heaterSelPin 15

int sensorValue = 0;

void setup()
{
    pinMode(heaterSelPin,OUTPUT);               
    digitalWrite(heaterSelPin,HIGH);            
    Serial.begin(9600);                        
}

void loop()
{
    digitalWrite(heaterSelPin,LOW);             
    sensorValue = analogRead(analogInDatPin);         
    Serial.println(1023-sensorValue);           
    delay(1000);
}
