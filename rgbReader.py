import board
import busio
import adafruit_tcs34725
import time

# Setup
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)

def to_rgb(r, g, b, c):
    if c == 0:
        return 0, 0, 0
    # Normalize to 0-255 using clear channel
    scale = 255 / c
    r255 = min(int(r * scale), 255)
    g255 = min(int(g * scale), 255)
    b255 = min(int(b * scale), 255)
    return r255, g255, b255

def to_hex(r, g, b):
    return f"#{r:02X}{g:02X}{b:02X}"

print("Reading color... point sensor at something colorful!")
print("Press Ctrl+C to stop\n")

while True:
    r, g, b, c = sensor.color_raw
    r255, g255, b255 = to_rgb(r, g, b, c)
    hex_color = to_hex(r255, g255, b255)

    print(f"RGB: ({r255}, {g255}, {b255})  |  Hex: {hex_color}  |  Clear: {c}")
    time.sleep(0.5)