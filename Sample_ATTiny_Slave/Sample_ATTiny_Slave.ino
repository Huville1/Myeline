#include <TinyWireS.h>
void setup() {
 TinyWireS.begin(11);                /* join i2c bus with address 8 */
 TinyWireS.onReceive(receiveEvent); /* register receive event */
 TinyWireS.onRequest(requestEvent); /* register request event */
 Serial.begin(9600);           /* start serial for debug */
}

void loop() {
 //delay(100);
}

// function that executes whenever data is received from master
void receiveEvent(int howMany) {
 while (TinyWireS.available()) {
    char c = TinyWireS.read();      /* receive byte as a character */
    //Wire.flush();
    Serial.print(c);           /* print the character */
  }
 Serial.println();             /* to newline */
}

// function that executes whenever data is requested from master
void requestEvent() {
 TinyWireS.write("Hello Pi");  /*send string on request */
}
