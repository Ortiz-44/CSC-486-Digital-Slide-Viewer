import RPi.GPIO as GPIO
import time

SWITCH_A = 17
SWITCH_B = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SWITCH_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        a = GPIO.input(SWITCH_A)
        b = GPIO.input(SWITCH_B)
        print(f"A (GPIO17): {'CLOSED' if a == GPIO.LOW else 'open  '}  |  B (GPIO27): {'CLOSED' if b == GPIO.LOW else 'open  '}")
        time.sleep(0.3)

except KeyboardInterrupt:
    GPIO.cleanup()