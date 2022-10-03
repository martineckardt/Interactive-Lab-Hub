import time
import board
from adafruit_apds9960.apds9960 import APDS9960
from gtts import gTTS
import os
import pyglet
from time import sleep

i2c = board.I2C()
apds = APDS9960(i2c)

apds.enable_proximity = True

sounds = {
    "User Tired?": {
        "text": 'Are you tired?',
        "filename": '/tmp/temp1.mp3'
    },
    "coffee?": {
        "text": "Do you like coffee?",
        "filename": '/tmp/temp2.mp3'
    },
    "coffee today?": {
        "text": "Have you had a coffee today?",
        "filename": '/tmp/temp3.mp3'
    },
    "drinks?": {
        "text": "Do you like energy drinks?",
        "filename": '/tmp/temp4.mp3'
    },
    "weather?": {
        "text": "Is the weather nice?",
        "filename": '/tmp/temp5.mp3'
    },
        "done": {
        "text": "Have a good day!",
        "filename": '/tmp/temp6.mp3'
    },
        "energy drink": {
        "text": "Grab your favorite energy drink!",
        "filename": '/tmp/temp6.mp3'
    },
        "Break": {
        "text": "Take a quick brain break for yourself",
        "filename": '/tmp/temp6.mp3'
    },
        "grab coffee": {
        "text": "Grab yourself a coffee and have a great day!",
        "filename": '/tmp/temp6.mp3'
    },
        "walk": {
        "text": "Go for a walk and enjoy the weather!",
        "filename": '/tmp/temp6.mp3'
    },
}

def say(soundId):
    sound = pyglet.media.load(sounds[soundId]['filename'], streaming=False)
    sound.play()
    #prevent from stopping the script in all, so it can be used for the interaction
    sleep(sound.duration)

# Prepare sound files for use in the script
for sound in sounds.values():
    tts = gTTS(text=sound['text'], lang='en')
    filename = sound['filename']
    tts.save(filename)

# Planned interaction being prompted by sensor or user

print("Waiting for user to be tired")
while apds.proximity <= 5:
    time.sleep(1)

print("User is tired")
say("User Tired?")

response_ac = input("Is the user tired (y/n) ")

if response_ac == "n":
    say("done")

else:
    say("coffee?")
    tworesponse_ac = input("Do you like coffee? (y/n)")
    if tworesponse_ac == "y":

        say("coffee today?")

        thresponse_ac = input("Do you like coffee? (y/n)")
        if thresponse_ac == "y":
            say("Break")
        else:
            say("grab coffee")

    else:
        say("drinks?")
        thresponse_ac = input("Do you like energy drinks? (y/n)")
        if thresponse_ac == "y":
            say("energy drink")
        else:
            say("weather?")
            thresponse_ac = input("Is the weather nice outside (y/n)")
            if thresponse_ac == "y":
                say("walk")
            else:
                say("Break")


    