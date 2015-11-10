#define IN 3
#define LED 9

void setup() {
  // put your setup code here, to run once:
  pinMode(IN, INPUT);
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int stat = digitalRead(IN);
  int readSerial = 0;
  static int old_stat = LOW;

  if (Serial.available() > 0) {
    readSerial = Serial.read();

    if (readSerial == '1') {
      digitalWrite(LED, HIGH);
    } else {
      digitalWrite(LED, LOW);
    }
  }

  if (stat == HIGH && old_stat == LOW) {
    Serial.println("in");
  }

  old_stat = stat;
  
  delay(50);
}
