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
    Function: Load the correct collection and move through images
    depending on tilt direction.
    """

    def __init__(self):
        self.current_collection = None
        self.current_index = 0
        
        # Load the JSON file relative to this script's location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(script_dir, "Images.json")
        with open(json_path, "r") as f:
            self.collections = json.load(f)
        
        # Setup SSD1309 OLED display (monochrome 128x64)
        displayio.release_displays()
        spi = busio.SPI(board.SCK, MOSI=board.MOSI)
        bus = fourwire.FourWire(spi, command=board.D24, chip_select=board.CE0, reset=board.D25, baudrate=1000000)
        self.screen = adafruit_displayio_ssd1306.SSD1306(bus, width=128, height=64)

    def load_collection(self, color):
        if color in self.collections:
            self.current_collection = self.collections[color]
            self.current_index = 0
            print(f"Loaded {color} collection")
            self.show_image()
        else:
            print("Color not recognized, try again")

    def show_image(self):
        image_path = self.current_collection[self.current_index]
        print(f"Trying to open: {image_path}")
        img = Image.open(image_path)

        # Convert to monochrome and resize to fit OLED (128x64)
        img = img.convert("1")        # 1-bit black and white
        img = img.resize((128, 64))   # fit the OLED screen size

        # Convert PIL image to displayio bitmap (2 colors: black and white)
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
        print(f"Showing image {self.current_index + 1} of {len(self.current_collection)}")

    def next_image(self):
        if self.current_collection is None:
            print("No collection loaded")
            return
        self.current_index = (self.current_index + 1) % len(self.current_collection)
        self.show_image()

    def prev_image(self):
        if self.current_collection is None:
            print("No collection loaded")
            return
        self.current_index = (self.current_index - 1) % len(self.current_collection)
        self.show_image()


# Test code - just display first image, no tilt sensor
if __name__ == "__main__":
    r = ImageCollectionManager()
    r.load_collection("red")
    
    print("Image displayed! Press CTRL+C to stop")
    while True:
        pass