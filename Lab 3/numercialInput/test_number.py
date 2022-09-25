#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import json

if not os.path.exists("../../../speech2text/model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("../../../speech2text/model")
# You can also specify the possible word list
rec = KaldiRecognizer(model, wf.getframerate(), '["zero one two three four five six seven eight nine ten", "[unk]"]')

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break

    
    if rec.AcceptWaveform(data):
        rec.Result()
    else:
        rec.PartialResult()


res = json.loads(rec.FinalResult())

if res["text"] != "":
    print(f"So, {res['text']} pets live at your home. Thank you.")
else:
    print("Sorry, I did not understand that number. Please try again.")
