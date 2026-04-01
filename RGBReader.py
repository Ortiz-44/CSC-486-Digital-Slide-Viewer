# Lo mismo que los sensores

import random

class RGBReader:
    """
    Function: detect color from the slides inserted.
    """
    colors = ["red", "green", "yellow", "blue"]
    def read_color_code(self):
        rd = random.choice(self.colors)
        print("The color inserted is " + rd)
        return rd

reader = RGBReader()
print(reader.read_color_code())