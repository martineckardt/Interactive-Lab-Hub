import cv2
from tflite_runtime.interpreter import Interpreter 
from PIL import Image
import numpy as np
import time
from gtts import gTTS

def load_labels(path): 
  with open(path, 'r') as f:
    return [line.strip() for i, line in enumerate(f.readlines())]

def set_input_tensor(interpreter, image):
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = image

def classify_image(interpreter, image):
  set_input_tensor(interpreter, image)

  interpreter.invoke()
  output_details = interpreter.get_output_details()[0]
  output = np.squeeze(interpreter.get_tensor(output_details['index']))

  scale, zero_point = output_details['quantization']
  output = scale * (output - zero_point)

  ordered = np.argpartition(-output, 1)
  return [(i, output[i]) for i in ordered[:1]][0]

def say(soundId):
    sound = pyglet.media.load(sounds[soundId]['filename'], streaming=False)
    sound.play()
    #prevent from killing
    sleep(sound.duration)

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

# Prepare sound files
for sound in sounds.values():
    tts = gTTS(text=sound['text'], lang='en')
    filename = sound['filename']
    tts.save(filename)

data_folder = "/home/pi/Interactive-Lab-Hub/Lab 5/project/model"

model_path = data_folder + "boiling_water_detection.tflite"
label_path = data_folder + "labels_boiling_water_detection.txt"

# Read class labels.
labels = load_labels(label_path)

interpreter = Interpreter(model_path)
print("Model Loaded Successfully.")

interpreter.allocate_tensors()
_, height, width, _ = interpreter.get_input_details()[0]['shape']
print("Image Shape (", width, ",", height, ")")

water_boiling = False

while(water_boiling)
    # Capture image with webcam and resize
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resizedImgRGB = cv2.resize(imgRGB, (width, height));

    # Classify the image.
    label_id, prob = classify_image(interpreter, resizedImgRGB)
    classification_label = labels[label_id]

    print("Image Label is :", , ", with Accuracy :", np.round(prob*100, 2), "%.")

    water_boiling = (classification_label == "1 Water boiling")

say("water boiling")

input("Controller: pasta put in? (press any key)")

say("pasta reminder")

time.sleep(9*60)

say("pasta done")


# ========= Cleanup ===========

#remove temporary files
for sound in sounds.values():
    os.remove(sound['filename']) 

print("removed all temp files")

    