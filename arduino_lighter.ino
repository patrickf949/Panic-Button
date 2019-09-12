void setup() {
  pinMode(2, INPUT_PULLUP);
  pinMode(10, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int pushed = digitalRead(2);
  if(pushed == LOW){
      digitalWrite(10, HIGH);
  }else{
    digitalWrite(10, LOW);
  }
}
