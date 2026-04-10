import TiltSensor
import json
from PIL import Image
import board
import busio
import digitalio
import displayio
import fourwire
import adafruit_st7789

class ImageCollectionManager:
    """
    Function: Load the correct collection and move through images
    depending on tilt direction.
    """

    def __init__(self):
        self.current_collection = None
        self.current_index = 0
        
        # Load the JSON file
        with open("Images.json", "r") as f:
            self.collections = json.load(f)
        
        # Setup ST7789 color display
        displayio.release_displays()
        spi = busio.SPI(board.SCK, MOSI=board.MOSI)
        bus = fourwire.FourWire(spi, command=board.D24, chip_select=board.CE0, reset=board.D25)
        self.screen = adafruit_st7789.ST7789(bus, width=128, height=128, auto_refresh=True)

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
        img = img.convert("RGB")
        img = img.resize((128, 128))
        
        # Convert PIL image to displayio bitmap
        bitmap = displayio.Bitmap(128, 128, 65536)
        palette = displayio.Palette(65536)
        for y in range(128):
            for x in range(128):
                r, g, b = img.getpixel((x, y))
                color_565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
                palette[color_565] = (r << 16) | (g << 8) | b
                bitmap[x, y] = color_565
        
        tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
        group = displayio.Group()
        group.append(tile_grid)
        self.screen.root_group = group
        print(f"Showing image {self.current_index + 1} of {len(self.current_collection)}")

    def next_image(self):
        direction = TiltSensor.read_direction()
        if direction == "right" and self.current_collection:
            if self.current_index < len(self.current_collection) - 1:
                self.current_index += 1
                self.show_image()
            else:
                print("Already at last image")

# Test code
if __name__ == "__main__":
    r = ImageCollectionManager()
    r.load_collection("red")  # change to "blue" to test blue collection
    
    while True:
        r.next_image()