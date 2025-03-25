#include <Wire.h>
#include <Adafruit_VL53L0X.h>

// Initialize the VL53L0X sensor
Adafruit_VL53L0X lox = Adafruit_VL53L0X();

// Distance threshold (adjust based on setup)
const int THRESHOLD = 500;  // mm (set to detect blade passing)
const float DEBOUNCE_TIME = 0.2;  // seconds (to avoid multiple detections per pass)

unsigned long previousTime = 0; // Variable to store the previous time in milliseconds

void setup() {
  // Start serial communication for debugging
  Serial.begin(115200);
  while (!Serial); // Wait for the serial to initialize

  // Initialize I2C communication
  Wire.begin();

  // Initialize the VL53L0X sensor
  if (!lox.begin()) {
    Serial.println("Failed to initialize VL53L0X sensor!");
    while (1);
  }

  // Print a message
  Serial.println("Measuring Wind Turbine Speed...");
}

void loop() {
  // Read the current distance in mm
  uint16_t distance = lox.readRange();  // Use readRange() instead of readRangeSingleMillimeters()

  // Check if the distance is below the threshold (indicating blade passing)
  if (distance < THRESHOLD) {
    unsigned long currentTime = millis();  // Get the current time in milliseconds

    if (previousTime != 0) {
      unsigned long deltaTime = currentTime - previousTime; // Calculate the time difference

      // Avoid false multiple detections using debounce time
      if (deltaTime > DEBOUNCE_TIME * 1000) {  // Convert debounce time to milliseconds
        float rpm = 60000.0 / deltaTime;  // Calculate RPM (60,000 ms / deltaTime)
        Serial.print("Blade Speed: ");
        Serial.print(rpm, 2);  // Print RPM with 2 decimal places
        Serial.println(" RPM");

        // Update the previous time
        previousTime = currentTime;
      }
    } else {
      // Set initial time
      previousTime = currentTime;
    }
  }

  delay(3);  // Small delay to reduce CPU usage
}
