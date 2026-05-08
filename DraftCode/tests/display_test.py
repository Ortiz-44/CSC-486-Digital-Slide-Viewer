import board
import busio
import displayio
import fourwire
import adafruit_displayio_ssd1306

displayio.release_displays()

spi = busio.SPI(board.SCK, MOSI=board.MOSI)

oled_cs = board.CE0
oled_dc = board.D24
oled_rst = board.D25

display_bus = fourwire.FourWire(spi, command=oled_dc, chip_select=oled_cs, reset=oled_rst, baudrate=1000000)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Fill screen white
bitmap = displayio.Bitmap(128, 64, 1)
palette = displayio.Palette(1)
palette[0] = 0xFFFFFF
tile = displayio.TileGrid(bitmap, pixel_shader=palette)
group = displayio.Group()
group.append(tile)
display.root_group = group

print("Done - screen should be white")

import time
time.sleep(5)