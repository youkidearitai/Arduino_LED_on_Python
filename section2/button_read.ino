#define IN 3
#define LED 9
#define CHANGEMODE 10

void setup() {
  // put your setup code here, to run once:
  pinMode(IN, INPUT);
  pinMode(CHANGEMODE, INPUT);
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int stat = digitalRead(IN);
  int changeStat = digitalRead(CHANGEMODE);
  int readSerial = 0;
  static int old_stat = LOW;
  static int old_changeStat = LOW;

  if (Serial.available() > 0) {
    readSerial = Serial.read();

    if (readSerial == '1') {
      digitalWrite(LED, HIGH);
    } else {
      digitalWrite(LED, LOW);
    }
  }

  if (stat == LOW && old_stat == HIGH) {
    Serial.println("in");
  }

  if (changeStat == LOW && old_changeStat == HIGH) {
    Serial.println("change");
  }

  old_stat = stat;
  old_changeStat = changeStat;
  
  delay(50);
}
