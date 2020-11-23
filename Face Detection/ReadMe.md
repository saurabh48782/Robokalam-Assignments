## Face Detection Model
This project is developed to detect faces in real-time.

### Tech Stack Used:
1. **[Python](https://www.python.org/)** (Python is an interpreted, high-level and general-purpose programming language.) For more information about Python visit: **https://www.python.org/**
2. **[OpenCV](https://opencv.org/)** (OpenCV is a library of programming functions mainly aimed at real-time computer vision.)
For more information about OpenCV check out: **https://opencv.org/**
3. **[Flask](https://flask.palletsprojects.com/en/1.1.x/)** (Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.)
For more information about Flask check out: **https://flask.palletsprojects.com/en/1.1.x/**

-> '**app.py**' inside Face Detection folder contains the written source code.
I've made use of **[Haarcascades Classifier](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html)** to detect faces in real-time.

The model detects several faces in real-time and shows the output for a single face (the biggest face in terms of area) along with the named caption.

## Getting Started

### Installation of important modules and importing few libraries to be used
```
>>> pip install flask
>>> pip install opencv-python
```
Importing the libraries
```
import cv2
import numpy as np
from flask import Flask, render_template, request,redirect
```
First of all, we need to create a Flask object
```
>>> app = Flask(__name__)
```
Adding the necessary routes required for the proejct:

![Screenshot (4)](https://user-images.githubusercontent.com/44601120/99948225-23497a00-2d9f-11eb-8621-58e1db165222.png)

**Note** the render_template will render the html page into the browser.

### Face Detection function:
The function which detects face is written as:

![Screenshot (38)](https://user-images.githubusercontent.com/44601120/99951162-a2d94800-2da3-11eb-9106-0159e67ef1b7.png)

### Result

The home page looks like:
![Screenshot (7)](https://user-images.githubusercontent.com/44601120/99949226-ae773f80-2da0-11eb-8557-319712afe1ac.png)

**[index.html](https://github.com/saurabh48782/Robokalam-Assignments/blob/main/Face%20Detection/templates/index.html)** contains the source code for the html page.
After we input the name in the text box and hit enter key, the camera of the device will get accessed and a dialog box appears as shown in figure below:

![Screenshot (34)](https://user-images.githubusercontent.com/44601120/99950479-97395180-2da2-11eb-991f-458be6e4d413.png)

If the face is detected by the in the camera then, it will give a notification as **Congratulations! face(s) detection is successful. !!** after we press 'q' to stop the camera. Otherwise, it gives notification as **"Face not Detected. try again !!"**

