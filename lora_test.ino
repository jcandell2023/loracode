/*
  Module      Arduino
  M0          4
  M1          5
  Rx          3 (This is the MCU Tx lined)
  Tx          2 (This is the MCU Rx line)
  Aux         6
  Vcc         3V3
  Gnd         Gnd
*/

#include <SoftwareSerial.h>

char input[100];
int i = 0;

//Should be rx pin then tx pin
SoftwareSerial ESerial(3, 2);

void setup() {


  Serial.begin(9600);

  ESerial.begin(9600);
  ESerial.listen();
  Serial.println("Starting Reader");

}

void loop() {

  if (ESerial.available() > 0) {
    Serial.println("Message received");
    char curRead = ESerial.peek();
    if (i < 100 && curRead != '~') {
      input[i] = ESerial.read();
      i++;
    }
  } else if (i > 10) {
    Serial.println(String(input));
  }
  
}
