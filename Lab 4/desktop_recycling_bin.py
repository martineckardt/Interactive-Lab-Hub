import time
import board
import busio

import adafruit_mpr121
from adafruit_apds9960.apds9960 import APDS9960
import qwiic_led_stick

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

i2c = board.I2C()
apds = APDS9960(i2c)

apds.enable_proximity = True
threshold = 7

item_counter = 0
cooldown = 0

print("\nSparkFun Qwiic LED Stick Example 1")
my_stick = qwiic_led_stick.QwiicLEDStick()

if my_stick.begin() == False:
    print("\nThe Qwiic LED Stick isn't connected to the sytsem. Please check your connection", \
        file=sys.stderr)

my_stick.LED_off()
my_stick.set_all_LED_brightness(5)

while True:
    if (cooldown > 0): # Don't check the sensor for 50 rounds after an item has been tossed to avoid double counting
        cooldown -= 1
    elif (apds.proximity >= threshold): # Check if something has been tossed in the box
        item_counter += 1
        cooldown = 50
        print("item tossed", item_counter)

        if (item_counter <= 10):
            my_stick.set_single_LED_color(item_counter, 255, 255, 255)

    
    # Reset counter when the ring around the box has been touched
    if mpr121[0].value:
        item_counter = 0

        # Turn off all LEDs
        my_stick.LED_off()
        print("Reset")

    time.sleep(0.01)
