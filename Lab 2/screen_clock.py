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
font_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# setup the code for our buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

sun_radius = 5
hour = 0

location = [
    {"name": "HAW", "time_offset": -6}, 
    {"name": "LAX", "time_offset": -3}, 
    {"name": "NYC", "time_offset": 0},
    {"name": "HAM", "time_offset": 6}, 
    {"name": "BKK", "time_offset": 11},
    {"name": "PVG", "time_offset": 12},
    {"name": "AKL", "time_offset": 16},
    ]

current_location_index = 2

color1 = "#FFFFFF"
color2 = "#000001"

while True:

    # swap colors between Light & dark mode using both buttons
    if not buttonA.value and not buttonB.value:
        temp = color1
        color1 = color2
        color2 = temp
    
    else:
        # just button A pressed
        if buttonB.value and not buttonA.value:  
            current_location_index = current_location_index + 1 if (current_location_index + 1) < len(location) else 0

        # just button B pressed
        if buttonA.value and not buttonB.value:
            current_location_index = current_location_index - 1 if (current_location_index -1) > -1 else len(location)-1

    # Draw a filled box (black or white) to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=color2)    

    # Get current time for the location
    hour = (dt.now().hour + (dt.now().minute / 60) + location[current_location_index]["time_offset"]) % 24

    # simulate faster sun movement
    #hour = hour % 24 + 1

    y = top

    # show current location at the bottom
    draw.text((width/2, height-20), location[current_location_index]["name"], font=font, fill=color1)

    # navigation on the side
    draw.text((x+1, height/4), location[current_location_index + 1 if (current_location_index + 1) < len(location) else 0]["name"], font=font_small, fill=color1)
    draw.text((x+1, 3*height/4-10), location[current_location_index - 1 if (current_location_index -1) > -1 else len(location)-1]["name"], font=font_small, fill=color1)
    draw.text((x, y), "⬆", font=font_big, fill=color1)
    draw.text((x, height-30), "⬇", font=font_big, fill=color1)

    # Draw horizontal line
    draw.line((24,height/2, width,height/2), fill=color1, width=1)
    
    # draw the course of the sun
    draw.line([(24+h*9, height/2+math.cos(h/24*math.pi*2)*40) for h in range(25)], fill=color1, width=1)

    # calculate the postion of the sun
    sun_x_offset = 24 + hour * 9
    sun_y_offset = math.cos(hour/24*math.pi*2)*40

    # draw the sun
    draw.ellipse([(sun_x_offset-sun_radius, height/2-sun_radius+sun_y_offset), (sun_x_offset+sun_radius, height/2+sun_radius+sun_y_offset)], fill=(color1 if 6 <= hour <= 18 else color2), outline=color1, width=1)

    # Display image.
    disp.image(image, rotation)
    time.sleep(0.1)

    

