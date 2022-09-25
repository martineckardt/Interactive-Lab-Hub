#https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)

#!/bin/bash
say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; }
#say $*
say " Please give me a number between 1 and 10"

arecord -D hw:2,0 -f cd -c1 -r 16000 -d 2 -t wav recorded_mono.wav
RES=$(python3 test_number.py recorded_mono.wav)

say $RES 
say " Thank you"