import time
import os
import board
import busio
import displayio
import fourwire
import adafruit_displayio_ssd1306
import RPi.GPIO as GPIO
from PIL import Image, ImageEnhance

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

# --- Image Collection ---
IMAGES = [
    "/home/gd2026/Pictures/BW/IMG-44.jpg",
    "/home/gd2026/Pictures/BW/IMG-441.png",
    "/home/gd2026/Pictures/BW/IMG1.jpg",
    "/home/gd2026/Pictures/BW/img22.png",
]

current_index = 0

def load_image(path):
    """Load, convert and display an image with dithering on the OLED."""
    print(f"Loading: {os.path.basename(path)}")
    img = Image.open(path)
    img = img.convert("L")                        # grayscale
    img = ImageEnhance.Contrast(img).enhance(1.4) # boost contrast
    img = img.resize((128, 64), Image.LANCZOS)    # fit screen
    img = img.convert("1")                        # 1-bit with dithering

    bitmap = displayio.Bitmap(128, 64, 2)
    palette = displayio.Palette(2)
    palette[0] = 0x000000  # black
    palette[1] = 0xFFFFFF  # white

    for y in range(64):
        for x in range(128):
            bitmap[x, y] = 1 if img.getpixel((x, y)) else 0

    tile = displayio.TileGrid(bitmap, pixel_shader=palette)
    group = displayio.Group()
    group.append(tile)
    screen.root_group = group
    print(f"Showing image {current_index + 1} of {len(IMAGES)}: {os.path.basename(path)}")

def wait_for_release():
    """Wait until tilt sensor returns to neutral."""
    while GPIO.input(SWITCH_A) == GPIO.LOW or GPIO.input(SWITCH_B) == GPIO.LOW:
        time.sleep(0.05)

# --- Main ---
print("Demo starting! Tilt to cycle through images.")
print("Press Ctrl+C to stop.\n")

load_image(IMAGES[current_index])

try:
    while True:
        a = GPIO.input(SWITCH_A)
        b = GPIO.input(SWITCH_B)

        if a == GPIO.LOW or b == GPIO.LOW:
            current_index = (current_index + 1) % len(IMAGES)
            load_image(IMAGES[current_index])
            wait_for_release()
            time.sleep(0.2)

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nStopped.")
    GPIO.cleanup()