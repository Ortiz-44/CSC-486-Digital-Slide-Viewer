import board
import busio
import adafruit_tcs34725

# Set up I2C connection
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)

# Read color
r, g, b, c = sensor.color_raw
print(f"Red: {r}, Green: {g}, Blue: {b}, Clear: {c}")