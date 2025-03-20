//Adafruit CL53L0X QT || P3317D

import time
import board
import busio
import adafruit_vl53l0x

# Initialize I2C bus and VL53L0X sensor
i2c = busio.I2C(board.SCL, board.SDA)


tof = adafruit_vl53l0x.VL53L0X(i2c)

# Distance threshold (adjust based on setup)
THRESHOLD = 500  # mm (set to detect blade passing)
DEBOUNCE_TIME = 0.2  # seconds (to avoid multiple detections per pass)

previous_time = None

print("Measuring Wind Turbine Speed...")

while True:
    distance = tof.range  # Get distance in mm

    if distance < THRESHOLD:  # Detect blade passing
        current_time = time.monotonic()  # Use monotonic time to avoid clock issues

        if previous_time is not None:
            delta_t = current_time - previous_time
            if delta_t > DEBOUNCE_TIME:  # Avoid false multiple detections
                rpm = 60 / delta_t
                print(f"Blade Speed: {rpm:.2f} RPM")
                previous_time = current_time
        else:
            previous_time = current_time  # Set initial time

    time.sleep(0.01)  # Small delay to reduce CPU usage
