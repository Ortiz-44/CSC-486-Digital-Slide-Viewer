import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Tilt SW1 and watch. Ctrl+C to stop.")

try:
    while True:
        val = GPIO.input(17)
        print(f"SW1: {val}")
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()