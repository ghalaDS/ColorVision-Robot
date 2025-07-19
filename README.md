# Color Recognition Robot using OpenCV

## Project Overview

This project implements a real-time color recognition system using Python and OpenCV.  
The robot captures live video through a webcam, and when the user clicks on a point in the video, it displays the detected color name.

This is ideal for:
- Color-sorting robots
- Educational demonstrations
- Computer vision beginners

---

## Features

- Real-time webcam feed
- Click-to-detect color from any pixel
- HSV-based color detection for better accuracy
- Supports recognition of:
  - 🔴 Red
  - 🟠 Orange
  - 🟡 Yellow
  - 🟢 Green
  - 🔵 Blue
  - 🟣 Purple
  - ⚫ Black
  - ⚪ White

---

## Example Screenshot
![Robot Preview](robot-image.jpg)

---

## Folder Contents
main.py – Main script for running the camera and detecting colors

README.md – This documentation file

robot-image.jpg – Picture of your robot setup (optional)
## Technologies Used

- Python 3.x
- OpenCV (cv2)

---

## How to Run

1. Install OpenCV if not already installed:
   
bash
   pip install opencv-python
Run the script:

bash
نسخ
تحرير
python main.py
Click anywhere on the webcam window to detect the color at that point.

Press ESC to close the window.

---

 ## Notes
Lighting conditions may affect detection, HSV helps reduce inaccuracy.

You can expand this to control hardware like servos or motors based on detected color.

Make sure your webcam is connected and accessible.
