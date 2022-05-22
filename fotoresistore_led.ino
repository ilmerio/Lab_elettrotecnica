void setup() {

  Serial.begin(9600);
  pinMode(13, OUTPUT);

}

void loop() {
  float fotor = analogRead(A0) * 5 / 1024.0;
  Serial.print(fotor);
  Serial.print("\n");
  char led = Serial.read();
  if ( led == 'a')
  {
    digitalWrite(13, HIGH);
  }
  if ( led == 's')
  {
    digitalWrite(13, LOW);
  }

  delay(100);
}
