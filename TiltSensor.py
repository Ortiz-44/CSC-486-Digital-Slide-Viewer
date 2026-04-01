

# Maybe aqui tiene que ir el codigo para los inputs de los sensores
# Averiguar que es ese codigo!!!


class TiltSensor:
    """
    Function: Detect and execute right or left tilt action.
    variables: RS - LS 
    """
    Sensor = ""

class TiltSensor:
    """
    Function: Detect and execute right or left tilt action.
    """

    def read_direction(self):
        while True:
            sn = input("left or right? ").lower()

            if sn == "left":
                print("sensor rotated left")
                return "left"

            elif sn == "right":
                print("sensor rotated right")
                return "right"

            else:
                print("Try again!")

reader = TiltSensor()
reader.read_direction()