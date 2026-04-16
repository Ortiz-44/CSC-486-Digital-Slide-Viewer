import time
import board
import busio
import displayio
import fourwire
import adafruit_displayio_ssd1306
import RPi.GPIO as GPIO

# --- Tilt Sensor Setup ---
SWITCH_A = 17
SWITCH_B = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SWITCH_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# --- Display Setup ---
displayio.release_displays()
spi = busio.SPI(board.SCK, MOSI=board.MOSI)
bus = fourwire.FourWire(spi, command=board.D24, chip_select=board.CE0, reset=board.D25, baudrate=1000000)
screen = adafruit_displayio_ssd1306.SSD1306(bus, width=128, height=64)

# --- Color Collections ---
# OLED is monochrome so we simulate "colors" with fill patterns and labels
COLORS = ["RED", "GREEN", "BLUE"]
current_index = 0

def show_color(index):
    """Fill the screen and show the color name as text."""
    color_name = COLORS[index]
    print(f"Displaying: {color_name}")

    # Alternate fill pattern per color to visually distinguish them
    # RED   = full white screen
    # GREEN = checkerboard pattern
    # BLUE  = horizontal stripes
    bitmap = displayio.Bitmap(128, 64, 2)
    palette = displayio.Palette(2)
    palette[0] = 0x000000  # black
    palette[1] = 0xFFFFFF  # white

    if color_name == "RED":
        # Full white
        for y in range(64):
            for x in range(128):
                bitmap[x, y] = 1

    elif color_name == "GREEN":
        # Checkerboard
        for y in range(64):
            for x in range(128):
                bitmap[x, y] = 1 if (x + y) % 2 == 0 else 0

    elif color_name == "BLUE":
        # Horizontal stripes
        for y in range(64):
            for x in range(128):
                bitmap[x, y] = 1 if y % 4 < 2 else 0

    tile = displayio.TileGrid(bitmap, pixel_shader=palette)
    group = displayio.Group()
    group.append(tile)
    screen.root_group = group

def wait_for_release():
    """Wait until both tilt switches are open (back to neutral)."""
    while GPIO.input(SWITCH_A) == GPIO.LOW or GPIO.input(SWITCH_B) == GPIO.LOW:
        time.sleep(0.5)

# --- Main ---
print("Demo starting! Tilt the sensor to cycle colors.")
print("Press Ctrl+C to stop.\n")

show_color(current_index)

try:
    while True:
        a = GPIO.input(SWITCH_A)
        b = GPIO.input(SWITCH_B)

        if a == GPIO.LOW or b == GPIO.LOW:
            # Any tilt detected — advance to next color
            current_index = (current_index + 1) % len(COLORS)
            show_color(current_index)
            wait_for_release()   # debounce: wait until tilt returns to neutral
            time.sleep(0.2)      # small extra buffer

        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nStopped.")
    GPIO.cleanup()
