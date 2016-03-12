
#include "Arduino.h"
#include "HardwareSerial.h"

//#include "Configuration.hh"

#define X_STEPPER_DIR A0
#define X_STEPPER_STEP A1
#define X_STEPPER_EN A2
#define X_STEPPER_POT A3

/* Simple Serial ECHO script : Written by ScottC 03/07/2012 */

/* Use a variable called byteRead to temporarily store
   the data coming from the computer */
byte byteRead;

void setup() {
// Turn the Serial Protocol ON
  Serial.begin(115200);
}

void loop() {
   /*  check if data has been sent from the computer: */
  if (Serial.available()) {
    /* read the most recent byte */
    byteRead = Serial.read();

    pinMode(X_STEPPER_DIR, OUTPUT);
    pinMode(X_STEPPER_STEP, OUTPUT);
    pinMode(X_STEPPER_EN, OUTPUT);
    //pinMode(X_STEPPER_POT, OUTPUT);

    digitalWrite(X_STEPPER_DIR, !digitalRead(X_STEPPER_DIR));
    //digitalWrite(X_STEPPER_POT, 0);
    digitalWrite(X_STEPPER_EN, 0);

    for (int i = 0; i < 10; i++) {
      //digitalWrite(X_STEPPER_STEP, !digitalRead(X_STEPPER_STEP));
    }

    tone(X_STEPPER_STEP, 400, 300);


    Serial.write("ACK");
  }
}
