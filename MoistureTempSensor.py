

#include "Adafruit_seesaw.h"
#include <Arduino.h>

// Create an instance of the Adafruit_seesaw class to interact with the sensor
Adafruit_seesaw ss;

const int MOISTURE_THRESHOLD = 740; // Threshold for moisture (below this = dry soil)
const int TEMP_THRESHOLD = 30;     // Threshold for temperature (above this = hot)

void setup() {
  // Start serial communication with a baud rate of 115200 for debugging
  Serial.begin(115200);

  // Print a message to indicate the start of the program
  Serial.println("seesaw Soil Sensor example!");

  // Initialize the seesaw sensor with the I2C address of 0x36
  // If initialization fails, print an error and halt the program
  if (!ss.begin(0x36)) {
    Serial.println("ERROR! seesaw not found");
    while (1) delay(1);  // Infinite loop to halt the program if sensor is not found
  } else {
    // If the sensor is found, print a success message and the sensor version
    Serial.print("seesaw started! version: ");
    Serial.println(ss.getVersion(), HEX);  // Print the sensor's firmware version in hexadecimal format
  }
}

void loop() {
  // Get the current temperature reading from the sensor in Celsius
  float temp = ss.getTemp();

  // Read the capacitive touch value (soil moisture level)
  uint16_t touch = ss.touchRead(0);

  // Print the temperature value to the serial monitor
  Serial.print("Temperature: "); 
  Serial.print(temp); 
  Serial.println(" *C");

  // Print the capacitive touch reading, which is a measure of the soil moisture level
  Serial.print("Capacitive: "); 
  Serial.println(touch);

  // Optional: Print a message if the moisture level is below the threshold (dry soil)
  if (touch <= MOISTURE_THRESHOLD) {
    Serial.println("Moisture condition met: Dry soil");
  }

  // Optional: Print a message if the temperature is above the threshold (hot)
  if (temp >= TEMP_THRESHOLD) {
    Serial.println("Temperature condition met: Hot");
  }

  // Delay for 100 milliseconds before repeating the loop (adjustable for faster/slower updates)
  delay(100);
}
