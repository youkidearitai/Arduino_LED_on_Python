#define X 2
#define Y 1
#define Z 0

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int x = analogRead(X);
  int y = analogRead(Y);
  int z = analogRead(Z);

  char xyz_pos[128] = {'\0'};

  snprintf(xyz_pos, 128, "%03d,%03d,%03d", x, y, z);
  Serial.println(xyz_pos);

  delay(20);
}

