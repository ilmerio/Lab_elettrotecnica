
void setup() {
 
  Serial.begin(9600);

}

void loop() {
  float r = analogRead(A0)*5/1024.0;
  Serial.print(r);
  Serial.print("\n");
  delay(100);
}
