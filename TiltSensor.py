

# Maybe aqui tiene que ir el codigo para los inputs de los sensores
# Averiguar que es ese codigo!!!
from gpiozero import Button
import time

class TiltSensor:
    def __init__(self, pin):
        self.sensor = Button(pin, pull_up=True)

    def read_direction(self):
        while True:
            if not self.sensor.is_pressed:
                print("Tilt detected")

                while not self.sensor.is_pressed:
                    time.sleep(0.5)

                return "right"
            time.sleep(0.5)

# class TiltSensor:
#     """
#     Function: Detect and execute right or left tilt action.
#     """

#     def read_direction(self):
#         while True:
#             sn = input("left or right? ").lower()

#             if sn == "left":
#                 print("sensor rotated left")
#                 return "left"

#             elif sn == "right":
#                 print("sensor rotated right")
#                 return "right"

#             else:
#                 print("Try again!")

if __name__ == "__main__":
    tilt = TiltSensor(17)

    while True:
        direction = tilt.read_direction()
        print("Direction:", direction)

    # This will go later in the main loop

