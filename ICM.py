import RGBReader
import TiltSensor

class ImageCollectionManager:
    """
    Function: Load the correct collection and move through images
    depending on tilt direction.
    """

    def __init__(self):
        self.current_collection = None

    def load_collection(self):
        color_read = RGBReader.read_color_code()

        if color_read == "blue":
            self.current_collection = "blue"
            print("Insert blue collection")
        elif color_read == "green":
            self.current_collection = "green"
            print("Insert green collection")
        elif color_read == "red":
            self.current_collection = "red"
            print("Insert red collection")
        elif color_read == "yellow":
            self.current_collection = "yellow"
            print("Insert yellow collection")
        else:
            print("Try again")

    def next_image(self):
        direction = TiltSensor.read_direction()
        if direction == "right":
            print("Show next image")

    def previous_image(self):
        direction = TiltSensor.read_direction()
        if direction == "left":
            print("Show previous image")

r = ImageCollectionManager()
r.load_collection()