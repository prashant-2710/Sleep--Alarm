# Sleep-Alarm
# Real-Time Drowsiness Detection System

A lightweight, efficient Python application designed to detect fatigue and drowsiness in real-time using a computer webcam. This project is ideal for students pulling all-nighters or as a prototype for driver safety systems.

## 🚀 Features
* **Real-Time Tracking:** Uses webcam feed to monitor face and eye states continuously.
* **Lightweight Architecture:** Built using OpenCV's native Haar Cascade Classifiers, eliminating the need for heavy AI/ML frameworks.
* **Automated Audio Alert:** Automatically triggers a looping Windows system alarm (`winsound`) when continuous eye-closure is detected for a specific number of frames.
* **Visual Alerts:** Displays a prominent **"DROWSINESS ALERT!"** warning on the screen interface.

## 🛠️ Built With
* **Language:** Python 3.x
* **Core Library:** OpenCV (`opencv-python`)
* **Audio System:** Winsound (Native Windows Module)
