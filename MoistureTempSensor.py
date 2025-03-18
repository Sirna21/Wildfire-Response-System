

//CURRENTLY IN C++
// Include the Adafruit Seesaw library which provides easy access to the Seesaw sensor
#include "Adafruit_seesaw.h"

// Create an instance of the Adafruit_seesaw class to interact with the sensor
Adafruit_seesaw ss;

const int MOISTURE_THRESHOLD = 740; // Threshold for moisture (below this = dry soil)

//200(very dry)-2000(very wet) = 1800
//1800 * 0.3 = 540
//540 + 200 = 740 (threshold for the "30% or less" humidity)

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
    while(1) delay(1);  // Infinite loop to halt the program if sensor is not found
  } else {
    // If the sensor is found, print a success message and the sensor version
    Serial.print("seesaw started! version: ");
    Serial.println(ss.getVersion(), HEX);  // Print the sensor's firmware version in hexadecimal format
  }
}

void loop() {
  int condition_count = 0;  // To count how many conditions are met (must equal 2 for both moisture and temp)

  // Get the current temperature reading from the sensor in Celsius
  float temp = ss.getTemp(); 


  // Read the capacitive touch value (soil moisture level)
  // The first parameter (0) refers to the first capacitive touch pin
  uint16_t touch = ss.touchRead(0);


   // Moisture condition: check if moisture is below or equal to the threshold
    if (touch <= MOISTURE_THRESHOLD) {
      condition_count++;  // Increment if moisture is below threshold (dry soil)

      // Print the capacitive touch reading ONLY IF IT MEETS CONDITION, which is a measure of the soil moisture level 
      Serial.print("Moisture condition met: ");
      Serial.println(touch);
    }

    // Temperature condition: check if the temperature is above or equal to the threshold
    if (temp >= TEMP_THRESHOLD) {
      condition_count++;  // Increment if temperature is higher than threshold (hot)
      
      // Print the temperature value to the serial monitor ONLY IF IT MEETS CONDITION
      Serial.print("Temperature condition met: ");
      Serial.println(temp);
      Serial.println("*C");
    }

  // Print the temperature value to the serial monitor (CAN BE REMOVED)
  Serial.print("Temperature: "); Serial.print(temp); Serial.println("*C");
  
  // Print the capacitive touch reading, which is a measure of the soil moisture level (CAN BE REMOVED)
  Serial.print("Capacitive: "); Serial.println(touch);

  // Delay for 100 milliseconds before repeating the loop
  delay(100);


}






