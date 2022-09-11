import time
from datetime import datetime as dt
import math
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

sun_radius = 5
hour = 0

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    
    # Get current time
    #hour = dt.now().hour + (dt.now().minute / 60)

    # Simulate faster sun movement
    hour = hour % 24 + 1

    y = top

    # Show titel at the top
    draw.text((x, y), "☀️ Sun Clock", font=font, fill="#FFFFFF")

    # Draw horizontal line
    draw.line((x/2,height/2, width,height/2), fill="#FFFFFF", width=1)
    
    # draw the course of the sun
    draw.line([(h*10, 67.5+math.cos(h/24*math.pi*2)*40) for h in range(25)], fill="#FFFFFF", width=1)

    # calculate the postion of the sun
    sun_x_offset = hour * 10
    sun_y_offset = math.cos(hour/24*math.pi*2)*40

    # draw the sun
    draw.ellipse([(sun_x_offset-sun_radius, height/2-sun_radius+sun_y_offset), (sun_x_offset+sun_radius, height/2+sun_radius+sun_y_offset)], fill=("#FFFFFF" if 6 <= hour <= 18 else "#000001"), outline="#FFFFFF", width=1)

    # Display image.
    disp.image(image, rotation)
    time.sleep(0.3)
