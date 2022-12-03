# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_apds9960.apds9960 import APDS9960
from gtts import gTTS
import os
import pyglet
from time import sleep


sounds = {
    "water boiling": {
        "text": 'The water is boiling',
        "filename": '/tmp/temp1.mp3'
    },
    "pasta reminder": {
        "text": "I will remind you in 9 minutes",
        "filename": '/tmp/temp2.mp3'
    },
    "pasta done": {
        "text": "The pasta is done",
        "filename": '/tmp/temp3.mp3'
    }
}

def say(soundId):
    sound = pyglet.media.load(sounds[soundId]['filename'], streaming=False)
    sound.play()
    #prevent from killing
    sleep(sound.duration)

# Prepare sound files
for sound in sounds.values():
    tts = gTTS(text=sound['text'], lang='en')
    filename = sound['filename']
    tts.save(filename)



# ===== Interacation ========

response_ac = input("Controller: start ")

say("water boiling")

response_ac = input("Controller: pasta in pot ")

say("pasta reminder")

response_ac = input("Controller: pasta done ")

say("pasta done")


# ========= Cleanup ===========

#remove temporary files
for sound in sounds.values():
    os.remove(sound['filename']) 


print("removed all temp files")

