const double offset = (0.6 / 5) * 1024;
const double base_temp = 5 / 1024.0;
const double mv_to_v = 100.0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int level = analogRead(0);
  double temperature = (double)(level - offset) * base_temp * mv_to_v;
  char temperature_str[32] = {'\0'};
  char output[128] = {'\0'};
  dtostrf(temperature, 8 + 3, 8, temperature_str);

  snprintf(output, 128, "serial,%s", temperature_str);
  
  Serial.println(output);
  delay(100);
}
