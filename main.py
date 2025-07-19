import cv2
import numpy as np

def get_color_name(h, s, v):
    if s < 50 and v > 200:
        return "White"
    elif v < 50:
        return "Black"
    elif h < 10 or h > 160:
        return "Red"
    elif 10 <= h <= 25:
        return "Orange"
    elif 26 <= h <= 34:
        return "Yellow"
    elif 35 <= h <= 85:
        return "Green"
    elif 86 <= h <= 125:
        return "Blue"
    elif 126 <= h <= 160:
        return "Purple"
    else:
        return "Unknown"

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_frame = cv2.cvtColor(param, cv2.COLOR_BGR2HSV)
        h, s, v = hsv_frame[y, x]
        color = get_color_name(h, s, v)
        print(f"Color: {color}  (HSV: {h}, {s}, {v})")
        cv2.putText(param, color, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)


cap = cv2.VideoCapture(0)
cv2.namedWindow("Color Recognition")

while True:
    ret, frame = cap.read()
    if not ret:
        break


    cv2.setMouseCallback("Color Recognition", click_event, frame.copy())
    cv2.imshow("Color Recognition", frame)

    if cv2.waitKey(1) & 0xFF == 27: 
        break

cap.release()
cv2.destroyAllWindows()


