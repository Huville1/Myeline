int i =0;
void setup() {
  Serial.begin(9600);
}
void loop() {
  Serial.print(i);
  Serial.print(',');
  Serial.print(i);
  Serial.println();
  i++;
  delay(1000);
}
