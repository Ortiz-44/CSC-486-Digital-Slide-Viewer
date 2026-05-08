import time
from rgbReader import get_dominant_color
from tilt import get_tilt, cleanup
from ICM import ImageCollectionManager

# ── Constants ─────────────────────────────────────────────────────────────────
HELLO_IMAGE = "/home/gd2026/Pictures/BW/hello-1.png"

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("Digital Slide Viewer starting...")

    manager = ImageCollectionManager()

    # Show hello screen on startup
    manager.display_image_file(HELLO_IMAGE)
    print("Waiting for color input...\n")

    current_color = None  # no collection loaded yet

    try:
        while True:

            # 1. Read dominant color from RGB sensor
            detected = get_dominant_color()

            # 2. If no color detected, show hello and reset
            if detected is None:
                if current_color is not None:
                    print("No color detected. Returning to hello screen.")
                    manager.display_image_file(HELLO_IMAGE)
                    current_color = None

            # 3. New color detected → switch collection
            elif detected != current_color:
                print(f"Color changed: {current_color} → {detected}")
                current_color = detected
                manager.load_collection(current_color)

            # 4. Check tilt → navigate images
            action = get_tilt()
            if action == "next":
                manager.next_image()
            elif action == "prev":
                manager.prev_image()

            time.sleep(0.5)  # adjust as needed for responsiveness

    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        cleanup()
        print("GPIO cleaned up. Goodbye!")

if __name__ == "__main__":
    main()