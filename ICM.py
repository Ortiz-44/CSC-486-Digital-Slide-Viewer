import json
import os
from PIL import Image
import board
import busio
import displayio
import fourwire
import adafruit_displayio_ssd1306

class ImageCollectionManager:
    """
    Loads the correct image collection based on detected color
    and navigates through images based on tilt input.
    """

    def __init__(self):
        self.current_collection = None
        self.current_index = 0

        # Load images.json (full project collections)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(script_dir, "images.json")
        with open(json_path, "r") as f:
            self.collections = json.load(f)

        # Setup SSD1306 OLED display (monochrome 128x64)
        displayio.release_displays()
        spi = busio.SPI(board.SCK, MOSI=board.MOSI)
        bus = fourwire.FourWire(spi, command=board.D24, chip_select=board.CE0, reset=board.D25, baudrate=1000000)
        self.screen = adafruit_displayio_ssd1306.SSD1306(bus, width=128, height=64)

    def display_image_file(self, image_path):
        """Open any image file and render it to the OLED screen."""
        print(f"Displaying: {image_path}")
        img = Image.open(image_path)
        img = img.convert("1")       # 1-bit black and white
        img = img.resize((128, 64))  # fit OLED screen

        bitmap = displayio.Bitmap(128, 64, 2)
        palette = displayio.Palette(2)
        palette[0] = 0x000000  # black
        palette[1] = 0xFFFFFF  # white

        for y in range(64):
            for x in range(128):
                pixel = img.getpixel((x, y))
                bitmap[x, y] = 1 if pixel else 0

        tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
        group = displayio.Group()
        group.append(tile_grid)
        self.screen.root_group = group

    def load_collection(self, color):
        """Load a collection by color key and show the first image."""
        if color in self.collections:
            self.current_collection = self.collections[color]
            self.current_index = 0
            print(f"Loaded '{color}' collection ({len(self.current_collection)} images)")
            self.show_image()
        else:
            print(f"Color '{color}' not found in collections.")

    def show_image(self):
        """Display the current image in the loaded collection."""
        if self.current_collection is None:
            print("No collection loaded.")
            return
        image_path = self.current_collection[self.current_index]
        self.display_image_file(image_path)
        print(f"Image {self.current_index + 1} of {len(self.current_collection)}")

    def next_image(self):
        """Advance to the next image in the collection (wraps around)."""
        if self.current_collection is None:
            print("No collection loaded.")
            return
        self.current_index = (self.current_index + 1) % len(self.current_collection)
        self.show_image()

    def prev_image(self):
        """Go back to the previous image in the collection (wraps around)."""
        if self.current_collection is None:
            print("No collection loaded.")
            return
        self.current_index = (self.current_index - 1) % len(self.current_collection)
        self.show_image()


# ── Standalone test ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    manager = ImageCollectionManager()
    manager.load_collection("red")
    print("Image displayed! Press CTRL+C to stop.")
    while True:
        pass