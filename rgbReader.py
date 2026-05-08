import board
import busio
import adafruit_tcs34725
import time

# ── Sensor is initialized once on first call, not at import time ──────────────
_sensor = None

def _get_sensor():
    """Initialize and return the sensor (only once)."""
    global _sensor
    if _sensor is None:
        i2c = busio.I2C(board.SCL, board.SDA)
        _sensor = adafruit_tcs34725.TCS34725(i2c)
    return _sensor

def to_rgb(r, g, b, c):
    """Normalize raw sensor values to 0-255."""
    if c == 0:
        return 0, 0, 0
    scale = 255 / c
    r255 = min(int(r * scale), 255)
    g255 = min(int(g * scale), 255)
    b255 = min(int(b * scale), 255)
    return r255, g255, b255

def get_dominant_color():
    """
    Read the RGB sensor and return the dominant color as a string.
    Returns: 'red', 'green', 'blue', or None if sensor reads all zeros.
    """
    sensor = _get_sensor()
    r, g, b, c = sensor.color_raw
    r255, g255, b255 = to_rgb(r, g, b, c)

    print(f"RGB: ({r255}, {g255}, {b255})")

    # If all channels are zero, no color detected
    if r255 == 0 and g255 == 0 and b255 == 0:
        return None

    # Return whichever channel is highest
    if r255 >= g255 and r255 >= b255:
        return "red"
    elif g255 >= r255 and g255 >= b255:
        return "green"
    else:
        return "blue"


# ── Standalone test (mirrors original behavior) ───────────────────────────────
if __name__ == "__main__":
    print("Reading color... point sensor at something colorful!")
    print("Press Ctrl+C to stop\n")
    while True:
        color = get_dominant_color()
        print(f"Dominant color: {color}\n")
        time.sleep(0.5)