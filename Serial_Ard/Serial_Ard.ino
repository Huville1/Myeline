int i =0;
void setup() {
  Serial.begin(9600);
}
void loop() {
  Serial.write(i);
  i++;
  delay(1000);
}
