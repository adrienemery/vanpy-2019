
#include <Servo.h> 

#define SONAR_PIN A0

Servo servo;
int pos = 0;    // variable to store the servo position 
long distance = 0; // variabel to store sonar reading
unsigned long start_time;


void setup() {
  servo.attach(9);  // attaches the servo on pin 9 to the servo object 
  Serial.begin(9600);    // start serial at 9600 baud  
  delay(100);
  start_time = millis();
}

int read_sensor(){
  /*
  Scale factor is (Vcc/512) per inch. A 5V supply yields ~9.8mV/in
  Arduino analog pin goes from 0 to 1024, so the value has to be divided by 2 to get the actual inches
  */
  distance = analogRead(SONAR_PIN)/2;
}


void loop() {
  ///////////////////////////////////////
  // Update analog pin at 10 Hz
  ///////////////////////////////////////
  if (millis() - start_time > 100) {
    Serial.println(read_sensor());
    start_time = millis();
  }

  ///////////////////////////////////////
  // Process Serial Input
  ///////////////////////////////////////
  if(Serial.available()) { 
    char cmd = Serial.read();    
    if (cmd == 's') {
      pos = Serial.parseInt();   // Parse an Integer from Serial
      servo.write(pos);          // tell servo to go to position in variable 'pos' 
    }
    
  }
}
