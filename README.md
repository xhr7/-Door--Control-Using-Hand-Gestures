# -Door-Control-Using-Hand-Gestures



https://github.com/xhr7/-Door-Control-Using-Hand-Gestures/assets/102740867/e72619a5-f286-4bde-8cd7-92b291c985f3



<img width="349" alt="image" src="https://github.com/xhr7/-Door-Control-Using-Hand-Gestures/assets/102740867/b6da7401-afc6-4f04-8346-2abc64e90eee">






<img width="469" alt="image" src="https://github.com/xhr7/-Door-Control-Using-Hand-Gestures/assets/102740867/99a6d35c-ade7-4842-b6ed-0548e8ac5c91">






## Introduction

In This project we have developed a door control system using hand gestures and servo motors, The traditional methods of door control often involve physical contact or the use of buttons or switches. However, by leveraging advancements in computer vision, gesture recognition, and servo motor technology, this project seeks to provide a touchless and intuitive way of controlling doors, and our project is designed to provide a touchless and hygienic way of controlling doors, making it suitable for various environments, including public spaces, commercial buildings, or homes. It offers convenience and ease of use, as users can simply perform a hand gesture to open or close the door without the need for physical contact or manual operation.


## Project Overview

This project integrates hand gesture recognition with a servo motor control using Python, OpenCV, MediaPipe, and an Arduino. The goal is to adjust the angle of a servo motor based on the relative positions of the thumb and index 

## Workflow:

Video Capture: The webcam captures video frames, which are processed in real-time.

Hand Detection: MediaPipe detects hand landmarks from the video frames.

Gesture Recognition: The script calculates the distance between the thumb and index finger to estimate the hand gesture's scale.

Servo Control: Based on the calculated distance, an angle is determined and sent to the Arduino to adjust the servo motor's positio

## Methodology:


<img width="420" alt="image" src="https://github.com/xhr7/-Door-Control-Using-Hand-Gestures/assets/102740867/905cb7b1-546c-40c6-9c80-4656cb65d0ec">


## Hardware:


<img width="615" alt="image" src="https://github.com/xhr7/-Door-Control-Using-Hand-Gestures/assets/102740867/2beef0c5-91c7-4b7f-b539-888c51153169">

## Software (Code):
 Modules and libraries used :

CV2 (OpenCV): Used for capturing and processing video frames to detect and track hand movements.
PyFirmata2: Allows Python to control an Arduino, sending commands to adjust servo positions based on hand gestures.

MediaPipe: Provides tools for robust hand and finger tracking in real-time from video input.

NumPy: Supports mathematical operations, especially calculating distances between hand landmarks to determine servo angles.

Math: Used for basic mathematical calculations necessary for determining the positions and movements of hand gestures.



## before run code must Loading Standard Firmata onto Arduino:
Objective:
To facilitate communication between the Arduino board and your Python script using the PyFirmata2 library, you must first upload the Standard Firmata sketch to the Arduino. Firmata is a protocol for communicating with microcontrollers from software on a computer (or smartphone/tablet/etc).

In the Arduino IDE, navigate to File > Examples > Firmata > StandardFirmata.
This opens the Standard Firmata sketch, which is a pre-written program designed to accept commands from your computer.

then upload to your Arduino after that run the python code
