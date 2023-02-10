import time
import board
import busio
import adafruit_icm20x
import math

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ICM-20948 object
sensor = adafruit_icm20x.ICM20948(i2c)

# Set the gyroscope range
sensor.gyro_range = adafruit_icm20x.GyroRange.RANGE_2000_DPS

# Set the accelerometer range
sensor.accel_range = adafruit_icm20x.AccelRange.RANGE_8G

# Define the filter constant
alpha = 0.98

# Set the initial orientation
orientation = [0.0, 0.0, 0.0]

# Get the initial time
t_prev = time.monotonic()

while True:
    # Read the accelerometer data
    accel_x, accel_y, accel_z = sensor.acceleration

    # Convert the accelerometer data into roll and pitch angles
    roll = math.atan2(accel_y, accel_z)
    pitch = math.atan2(-accel_x, math.sqrt(accel_y**2 + accel_z**2))

    # Read the gyroscope data
    gyro_x, gyro_y, gyro_z = sensor.gyro

    # Get the current time
    t_curr = time.monotonic()

    # Calculate the time difference
    dt = t_curr - t_prev

    # Integrate the gyroscope data to get the angular velocity
    orientation[0] += gyro_x * dt
    orientation[1] += gyro_y * dt
    orientation[2] += gyro_z * dt

    # Blend the accelerometer data and the gyroscope data using a complementary filter
    orientation[0] = (1 - alpha) * (orientation[0] + dt * gyro_x) + alpha * roll
    orientation[1] = (1 - alpha) * (orientation[1] + dt * gyro_y) + alpha * pitch

    # Print the orientation
    print(
        "Roll: {:.2f} degrees, Pitch: {:.2f} degrees, Yaw: {:.2f} degrees".format(
            math.degrees(orientation[0]),
            math.degrees(orientation[1]),
            math.degrees(orientation[2]),
        )
    )

    # Update the previous time
    t_prev = t_curr

    # Sleep for a short time
    time.sleep(0.01)
