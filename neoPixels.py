import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 1, pixel_order=neopixel.RGB)
pixels[0] = (0, 0, 255)

while True:
    pixels.fill((255, 0, 0))
    time.sleep(1)
    pixels.fill((0, 255, 0))
    time.sleep(1)
    pixels.fill((0, 0, 255))
    time.sleep(1)
    pixels.fill((0, 0, 0))