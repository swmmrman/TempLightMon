#include <DHT.h>

int numReadings = 25;
int vals[25];
int counter = 0;
int total = 0;

DHT dht1(2, DHT11);
DHT dht2(7, DHT11);

void setup() {
  Serial.begin(115200);
  pinMode(A0, INPUT);
  pinMode(2, INPUT);
  pinMode(7, INPUT);
  dht1.begin();
  dht2.begin();
  int v = analogRead(A0); 
  for(int i=0; i < numReadings; i++) {
    vals[i] = v;
    total += v;
  }
}

void loop() {
  int oldV = vals[counter];
  int curV = analogRead(A0);
  vals[counter] = curV;
  total = total - oldV + curV;
  counter = (counter + 1) % numReadings;
  if(counter % 5 == 0){
    float d1Temp = dht1.readTemperature(true);
    float d2Temp = dht2.readTemperature(true);
    float d1Humid = dht1.readHumidity();
    float d2Humid = dht2.readHumidity();
    Serial.print(d1Temp);
    Serial.print(F(","));
    Serial.print(d2Temp);
    Serial.print(F(","));
    Serial.print(d1Humid);
    Serial.print(F(","));
    Serial.print(d2Humid);
    Serial.print(F(","));
    Serial.println(total/numReadings);
  }
  delay(200);
}
