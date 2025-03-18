import time
from machine import Pin, I2C
import adafruit_seesaw

# Define moisture and temperature thresholds
MOISTURE_THRESHOLD = 740
TEMP_THRESHOLD = 30

# Initialize I2C interface (assuming I2C bus 0)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Adjust pins if necessary for your board

# Initialize the seesaw sensor with the I2C address (0x36)
ss = adafruit_seesaw.Seesaw(i2c, addr=0x36)

def main():
    print("seesaw Soil Sensor example!")
    
    # Check if seesaw is connected
    if not ss:
        print("ERROR! seesaw not found")
        return
    
    print("seesaw started!")

    while True:
        condition_count = 0

        # Get the current temperature reading from the sensor (in Celsius)
        temp = ss.get_temp()

        # Read the capacitive touch value (soil moisture level)
        touch = ss.touch_read(0)

        # Moisture condition: check if moisture is below or equal to the threshold
        if touch <= MOISTURE_THRESHOLD:
            condition_count += 1
            print(f"Moisture condition met: {touch}")

        # Temperature condition: check if the temperature is above or equal to the threshold
        if temp >= TEMP_THRESHOLD:
            condition_count += 1
            print(f"Temperature condition met: {temp}°C")

        # Print the temperature value (can be removed if not needed)
        print(f"Temperature: {temp}°C")

        # Print the capacitive touch reading (can be removed if not needed)
        print(f"Capacitive: {touch}")

        # Delay for 100 milliseconds
        time.sleep(0.1)

if __name__ == "__main__":
    main()
