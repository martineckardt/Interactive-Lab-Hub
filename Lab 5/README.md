# Observant Systems

**NAMES OF COLLABORATORS HERE**

Jacob Everly (je354@cornell.edu)


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

## Prep

1. Spend about 10 Minutes doing the Listening exercise as described in [ListeningExercise.md](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2022/Lab%205/ListeningExercise.md)
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2022/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:
1. Pull the new Github Repo.(Please wait until thursday morning. There are still some incompatabilities to make the assignment work.)
1. Raspberry Pi
1. Webcam 

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show the filledout answers for the Contextual Interaction Design Tool.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

The following command is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

##### Contours Detection:

With contour detection you can detect edges in an image being captured by the camera. A use case for this type of program could be used to sense the fatigue of materials over time. If you were running a fatigue experiment in a lab, you could use this software to track the materials shape over time. You could sink this feature with the amount of cycles to get qaulatative video. You could also pull the data from the image to anaylze mathmatically how the 
images change over time.

![Contours detection output](https://github.com/JacobEverly/Interactive-Lab-Hub/raw/Fall2022/Lab%205/images/contour_detection.png)

##### Face Detection:
With face detection the camera identifies faces and features of the face. A use case of this could be if you are a resatraunt you could track frequent customers orders. If the camera could recognize the customers order and then track their tendencies. The customer could be prompted then when they walk into the store what their most popular orders are and quickly order if it what they want.

![Contours detection output](https://github.com/JacobEverly/Interactive-Lab-Hub/raw/Fall2022/Lab%205/images/face_detection.png)

##### Flow-detection:
Flow detection senses points that are moving through the image and tracks their path. This is seen in our example as the cars being tracked in the video. An application of this can be used in biomechanics studies. In these studies you track multiple points on the body to anyalze dynamic kinetics and metrics such as a person's gait. If you could get the sampling rate high enough to where you could have a smoother line, this could be a soultion for this problem.

![Flow Detection Cars Person](https://github.com/JacobEverly/Interactive-Lab-Hub/raw/Fall2022/Lab%205/images/flow_detection_person.png)

![Flow Detection Cars Traffic](https://github.com/JacobEverly/Interactive-Lab-Hub/raw/Fall2022/Lab%205/images/flow_detection_traffic.png)


##### Object Detection:
Object detection can detect objects, and if given a training set can detect onjects as is. We all have that one drawer, shelf or box that is filled with an assortment of random objects. If you could provide the sensor a training set of common household objects and created a directory. You could track all of the objects in the drawer and display the objects on a screen outside the drawer on a screen. This would save you the time of hustling through a drawer and wondering if there was a blue pen in it.


![Object Detection Multiple Objects](https://github.com/JacobEverly/Interactive-Lab-Hub/raw/Fall2022/Lab%205/images/object_detection_multiple-objects.png)

![Object Detection Plant Example](https://github.com/JacobEverly/Interactive-Lab-Hub/raw/Fall2022/Lab%205/images/object_detection_plant.png)


#### Filtering, FFTs, and Time Series data. 
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU or Microphone data stream could create a simple activity classifier between walking, running, and standing.

To get the microphone working we need to install two libraries. `PyAudio` to get the data from the microphone, `sciPy` to make data analysis easy, and the `numpy-ringbuffer` to keep track of the last ~1second of audio. 
Pyaudio needs to be installed with the following comand:
``sudo apt install python3-pyaudio``
SciPy is installed with 
``sudo apt install python3-scipy`` 

Lastly we need numpy-ringbuffer, to make cintinues data anlysis easier.
``pip install numpy-ringbuffer``

Now try the audio processing example:
* Find what ID the micrpohone has with `python ListAvalibleAudioDevices.py`
    Look for a device name that includes `USB` im namen.
* Adjust the variable `DEVICE_INDEX` in the `ExampleAudioFFT.py` file.
    See if you are getting results printed out from the microphone. Try to understand how the code works.
    Then run the file by typing `python ExampleAudioFFT.py`



Using the microphone, try one of the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

We were able to detect when a signal went above a certain value. We did this by looking for loud noises in a space.

https://github.com/JacobEverly/Interactive-Lab-Hub/blob/Fall2022/Lab%205/audio_processing/threshold_detection.py

The code is here ^

[Link to video](https://youtu.be/PA3nwMi4m4c)


**2. Set up a running averaging** Can you set up a running average over one of the variables that are being calculated.[moving average](https://en.wikipedia.org/wiki/Moving_average)

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

For technical references:

* Volume Calculation with [RootMeanSqare](https://en.wikipedia.org/wiki/Root_mean_square)
* [RingBuffer](https://en.wikipedia.org/wiki/Circular_buffer)
* [Frequency Analysis](https://en.wikipedia.org/wiki/Fast_Fourier_transform)


**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***

### (Optional Reading) Introducing Additional Concepts
The following sections ([MediaPipe](#mediapipe) and [Teachable Machines](#teachable-machines)) are included for your own optional learning. **The associated scripts will not work on Fall 2022's Pis, so you can move onto part B.** However, you are welcome to try it on your personal computer. 

#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr25
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi3 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 

~~\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\*~~

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)



#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

~~**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***~~


*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


### Part B
### Construct a simple interaction.

* Pick one of the models you have tried, and experiment with prototyping an interaction.
* This can be as simple as the boat detector showen in a previous lecture from Nikolas Matelaro.
* Try out different interaction outputs and inputs.
* Fill out the ``Contextual Interaction Design Tool`` sheet.[Found here.](ThinkingThroughContextandInteraction.png)

##### Interaction being prototyped:

Have a system that can detect when water is boiling. This can be used when cooking pasta or rice as you need to boil water for both. For now we will just use the system for cooking pasta.

What the system will do is monitor the noise from the pot of water and once a threshold is met will alert the chef to put that pasta in. Once the chef says "The pasta is in". The system will then start a 10 minute timer and at the end of the timer alert the cook when the pasta is finished.

##### Context ( Situational )

Who is involved:

A Cook and the pasta they want to make.

What is making noise:

The boiling pot of water that is intended to be used to make pasta.

When:

During the meal being prepared by the chef

Where:

In the kitchen or wherever the meal is being prepared.

##### Presense ( Intent )

Task Goals:

To inform the cook of when the water is ready, so they can throw the pasta in and cook it.

When to stand out:

When the water is ready for the pasta to be thrown in

When to blend in:

All the other times when the cook is cooking.

##### Behavior ( Reaction )

Implicit Behaviors:
    -Measuring the noise coming from the pot
    -Starting timer for when the pasta is thrown in

Explicit Behaviors:
    -Letting the cook know when the water is ready for the pasta
    -Letting the cook know when the pasta is done.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

<img width="572" alt="image" src="https://user-images.githubusercontent.com/112036223/197605372-367f1787-a997-4660-9d94-57c6754a2782.png">

We ran the program within an expermientation of the actual use case. We boiled water, attached the microphoen to the pot and waited for the water to boil. After calibrating the microphone to the sound of boiling water we tested to see if the water would trigger the threshold. We wuickly realized that we should not be using a threshold and instead a running average over a certain amount of time. This will do a good job filtering out any abrupt loud noises such as someone opening the door or reaching around for a pan. We then tried to get the sensor to recognize that the box of pasta was in the frame so we will see if we need to use a sensor instead in later iterations of the system

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?
    
    When the enviroment has a sustained noise level below the sound of boiling water about a foot away from water.

3. When does it fail?
    
    When there is sustained conversaition on the background, continous loud noises, loud appliances being run to make other things in the kitchen.

5. When it fails, why does it fail?
    
    It fails because we are looking for a certain running average of the sound over a certain period of time.

7. Based on the behavior you have seen, what other scenarios could cause problems?
    
    Any sustained volume, for example if this was used in a restaraunt and there was not good isolation between the kitchen and the dining room, it could accidently trigger the system.

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system? 

The user could be aware of too much noise causing a misfire, but will be to busy to consider this bug.


3. How bad would they be impacted by a miss classification?

If the user was alerted too early before the water was boiling, they would easily see that the water wasn't boiling and ignore the sugestion

5. How could change your interactive system to address this?

We are considering more visual options such as, training a model on the images of boiling water and having a visual implementation.


7. Are there optimizations you can try to do on your sense-making algorithm.

Supply the model with a good set of images so the anaylsis system becomes more robust.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
    Automate a task in cooking for a chef that could be balancing a lot of tasks all at the same time.
* What is a good environment for X?
    A kitchen that does not have a sustained amount of noise.
* What is a bad environment for X?
    A very loud kitchen that has a sustained noise louder then the sound of boiling water.
* When will X break?
    When loud outside noises cause the object to prematurely execute.
    Ay foreign objects that the sensors think would be the pasta box being thrown into the water.
* When it breaks how will X break?
    It will prematurely que the chef
    Start the timer for the pasta too soon
    Not work at all
* What are other properties/behaviors of X?
    Can also be reporgammed and used for the purpose of cooking rice.
* How does X feel?
    The current system feels a little intrusive when mounted on the ledge of the pasta pot.

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

### Part 2.

So we decided to change the design of the system from using sound to using images captured with the webcam. These images are analyzed using a machine learning model, that has been trained using teachable machine by Google. This was becuse of numerous issues that we discovered in Part 1 that we found to cause the system to not be a viable option.

These issues were
    1) Audible failures are the main cause of failure and busy ktichens would be too loud for the device to operate properly
    2) If the system provided a false positive the user would lose confidence in the system and most likely just ignore it.
    3) The audible threshold was difficult to calibrate, and was proving to be very inconsistent in.
    
These issues have caused us to pivot away from this audible threshold design. Instead we are going to create a set of images and use that set to teach a teachable machine. The machine will still be used to detect when the water is boiling. We will also retain a feature to start a timer when the water starts boiling, to index when the pasta will be done cooking.

## Capturing images from the webcam

We used the python [OpenCV 2](https://pythonexamples.org/python-opencv-cv2-resize-image/#2) library to capture and resize the images of the webcam. In the first version we mounted the camera directly over the pot:

![Camera mounted over pot](https://github.com/JacobEverly/Interactive-Lab-Hub/raw/Fall2022/Lab%205/images/IMG_3661.jpeg)

However, when testing the prototype we were concerned for the camera since it would get really wet from all the steam coming from the pot of boiling water. Therefore, we mounted the camera close to the pot:

![Camera mounted next to pot](https://github.com/JacobEverly/Interactive-Lab-Hub/raw/Fall2022/Lab%205/images/IMG_3664.jpeg)

## Training of the model

We used the Pi to capture the image with the webcam. Firstly, we captured images of the cold water. We slightly moved the camera over and over again and changed to lights to get a training set sufficiently large and diversified. Afterwards, we repeated the steps while the water was boiling.  We tried to train it on the Pi, but the ressources were not sufficient.

![Model trained](https://github.com/JacobEverly/Interactive-Lab-Hub/raw/Fall2022/Lab%205/images/IMG_3662.jpeg)

Then we moved them to a google drive and trained the model on our laptop. 

![Model trained](https://github.com/JacobEverly/Interactive-Lab-Hub/raw/Fall2022/Lab%205/images/IMG_3663.jpeg)

The model was trained to detect three different states:
- Water not boiling
- Water boiling
- Pasta in pot
 
The trained model was then transferred back to our Pi. There it was run using Tensorflow Lite. To learn how to use Tensorflow Lite we followed [this guide](https://blog.paperspace.com/tensorflow-lite-raspberry-pi/).

## Interaction design

You can find the program [here](project/boiling_water_detection.py)

**\*\*\*Include a short video demonstrating the finished result.\*\*\***

[Video of interaction](https://youtu.be/GH0tbGkG7d0)