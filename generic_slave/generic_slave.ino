//This code is generic spi slave code for arduino nano
/* Pins to remember:
D10 - SS
D11 - MOSI
D12 - MISO
D13 - SCK
*/

#include <SPI.h>

int counter = 0;


void setup() {
  // have to send on master in, *slave out*
  pinMode(MISO, OUTPUT);

  // turn on SPI in slave mode
  SPCR |= _BV(SPE);

  // turn on interrupts
  SPI.attachInterrupt();
}

// SPI interrupt routine
ISR (SPI_STC_vect)
{
  byte c = SPDR;

  SPDR = counter;
}  // end of interrupt service routine (ISR) for SPI

void loop () { 
  counter++;
  delay(1);
