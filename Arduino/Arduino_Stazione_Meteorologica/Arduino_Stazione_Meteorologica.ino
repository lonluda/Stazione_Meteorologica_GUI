#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

// attiva la funzione I2C ( Seriale )
Adafruit_BME280 bme;

void setup() {
  // Avvia la comunicazione Seriale
  Serial.begin(9600);
  // Inizializza la variabile status per il controllo della connessione
  bool status;
  // L'indirizzo della scheda è 0x77
  status = bme.begin (0x77);
}

void loop() { 

  // Richiama la funzione di print valori
  printValues();
  // Attendi 2 secondi tra un print e l'altro
  delay(2000);
}


void printValues() {

  // Scrivi via seriale il valore della temperatura
  Serial.println(bme.readTemperature());
  // Scrivi via seriale il valore dell'umidità
  Serial.println(bme.readHumidity());
  // Scrivi via seriale il valore della pressione
  Serial.println(bme.readPressure() / 100.0F);
}
