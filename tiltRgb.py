import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

import time
while True:
    print(f"GPIO17: {GPIO.input(17)}  GPIO27: {GPIO.input(27)}")
    time.sleep(0.3)
