# CSC-486 Digital Slide Viewer

A physical, offline photo album viewer built on a Raspberry Pi 4. 3D-printed tokens with color-coded strips act as "slides" — insert one, and the device loads the photo collection tied to that color. Tilt right to advance, tilt left to go back.

The project sits at the intersection of hardware, firmware, and a research question: *how do we hold onto digital memories in a physical way?* Most photos live in the cloud, scattered and forgotten. This device brings them back into the physical world — like an old photo album you take down from a shelf.

## How It Works

1. Power on — the Raspberry Pi boots and waits for input.
2. Insert a token — a colored 3D-printed slide goes into the reader slot.
3. Color is read — the RGB sensor (TCS34725FN) reads the strip on the token and matches it to an album in `images.json`.
4. Display loads — the SSD-1306 LCD shows the first image of that collection.
5. Tilt to navigate — tilt right for the next image, tilt left for the previous.

Image collections live locally on the Raspberry Pi. No cloud, no internet, no accounts.

## Hardware

- Raspberry Pi 4 (controller)
- TCS34725FN RGB color sensor (token detection)
- Tilt sensors + Adafruit breakout board (navigation)
- SSD-1306 LCD (display — black & white)
- 3D-printed ABS enclosure and color-coded tokens

## Code Structure

The codebase is organized in layers: **Hardware Input → Logic/Controller → Data/Model → Display/Output.**

| File | Purpose |
|------|---------|
| `MainCode.py` | Entry point. Wires the components together. |
| `tilt.py` | Reads tilt sensor GPIO input, returns direction. |
| `rgbReader.py` | Reads RGB sensor, maps values to album IDs. |
| `ICM.py` | Image collection manager — loads and steps through albums. |
| `images.json` | Maps color values to image collections. |
| `DraftCode/` | Test scripts and earlier prototypes. |

## Running It

On the Raspberry Pi:

```bash
cd ~/CSC-486-Digital-Slide-Viewer
source ~/.venv/bin/activate
python MainCode.py
```

Make sure the sensors are wired to the correct GPIO pins (see code comments in each file).

## Project Context

Built for CSC-486 (Spring 2026) as a research-grounded prototype exploring digital memory, inheritance, and physical computing. Inspired by Odom et al.'s work on slow technology and the "afterlife" of digital content — devices that ask questions instead of solving problems.

##Team

- Giovanny - Code Architecture, Display, User flow
- Dia - Tilt Sensors, Hardware wiring, 3D printed enclosure/tokens


## Status

In progress. Core components (RGB reader, tilt sensor, LCD) wired and tested individually. Currently integrating all three into a single loop with image collections.
