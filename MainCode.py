def Gio(x):
    v = x + 49
    if v >= 40:
        print("Ahora es!")
    else:
        print("No papi")
    return v
print(Gio(1))

class TiltSensor:
    """
    Function: Detect and execute right or left tilt action.
    variables: RS - LS 
    """
    def read_direction(self):
        pass

    pass

class RGBReader:
    """
    Function: detect color from the slides inserted.
    """
    def read_color_code(self):
        pass

    pass

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

    def run(self):
        """Main loop"""
        pass