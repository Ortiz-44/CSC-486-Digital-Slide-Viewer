

class ImageCollectionManager:
    """
    Function: Load the correct collection --> Execute next image or previous one depending tilt.
    """
    def load_collection(self):
        pass
    def next_image(self):
        pass
    def previous_image(self):
        pass

    pass

class LCDDisplay:
    """
    Fucntion: Display loaded collection to the display.
    """
    def display_image(self):
        pass

    pass

class DigitalSlideViewerController:
    """
    Main Class where everything is going to run
    """
    def __init__(self, tilt_sensor, rgb_reader, image_manager, display):
        self.tilt_sensor = tilt_sensor
        self.rgb_reader = rgb_reader
        self.image_manager = image_manager
        self.display = display
        # self.gyroscope = gyroscope

    def run(self):
        """Main loop"""
        pass