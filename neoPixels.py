import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 1, pixel_order=neopixel.RGB)
pixels[0] = (0, 0, 255)

framerate = 30
brightness = 1

try:
    while True:
        for i in range(framerate):
            brightness = 1 - i / framerate
            print (brightness)
            pixels.fill((255 * brightness, 0, 0))
            time.sleep(1 / framerate)
        for i in range(framerate):
            brightness = 1 - i / framerate
            pixels.fill((255 * brightness, 255 * brightness, 0))
            time.sleep(1 / framerate)
        for i in range(framerate):
            brightness = 1 - i / framerate
            pixels.fill((0, 0, 255 * brightness))
            time.sleep(1 / framerate)
except KeyboardInterrupt:
    pixels.fill((0, 0, 0))
