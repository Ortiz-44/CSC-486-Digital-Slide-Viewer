import RPi.GPIO as GPIO

# ── Pin setup ─────────────────────────────────────────────────────────────────
SWITCH_A = 17   # tilt → next image
SWITCH_B = 27   # tilt → previous image

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SWITCH_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Track previous states to detect transitions (open → closed)
_prev_a = GPIO.HIGH
_prev_b = GPIO.HIGH

def get_tilt():
    """
    Check both tilt switches and return action if triggered.
    Returns: 'next', 'prev', or None.
    """
    global _prev_a, _prev_b

    a = GPIO.input(SWITCH_A)
    b = GPIO.input(SWITCH_B)

    triggered = None

    # Switch A falling edge → next image
    if a == GPIO.LOW and _prev_a == GPIO.HIGH:
        print("Tilt detected on Switch A → next image")
        triggered = "next"

    # Switch B falling edge → previous image
    elif b == GPIO.LOW and _prev_b == GPIO.HIGH:
        print("Tilt detected on Switch B → previous image")
        triggered = "prev"

    _prev_a = a
    _prev_b = b

    return triggered

def cleanup():
    """Call this when the program exits to release GPIO pins."""
    GPIO.cleanup()


# ── Standalone test ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    import time
    print("Tilt sensor test. Ctrl+C to stop.")
    print("GPIO 17 = next | GPIO 27 = previous")
    print("Raw state every 0.2s (1=open, 0=closed)\n")
    try:
        while True:
            raw_a = GPIO.input(SWITCH_A)
            raw_b = GPIO.input(SWITCH_B)
            print(f"GPIO17: {raw_a} ({'OPEN' if raw_a else 'CLOSED'})  |  GPIO27: {raw_b} ({'OPEN' if raw_b else 'CLOSED'})")
            action = get_tilt()
            if action:
                print(f">>> Action triggered: {action}")
            time.sleep(0.4)
    except KeyboardInterrupt:
        cleanup()
        print("\nDone.")