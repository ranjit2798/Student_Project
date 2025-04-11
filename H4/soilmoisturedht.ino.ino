#include <DHT.h>

#define DHTPIN 2     
#define DHTTYPE DHT11 
DHT dht(DHTPIN, DHTTYPE);

int soilMoisturePin = A0; 

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  // Read DHT11 values
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  // Read Soil Moisture
  int soilValue = analogRead(soilMoisturePin);

  // Print values
  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.print("°C  Humidity: ");
  Serial.print(hum);
  Serial.print("%  Soil Moisture: ");
  Serial.println(soilValue);

  delay(2000);
}
