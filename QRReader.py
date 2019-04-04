import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

# Start webcame
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    decodedObjects = pyzbar.decode(frame)

    # Read QR code data
    for obj in decodedObjects:
        result = obj.data.decode("utf-8", "ignore").split(",")
        ID = result[0].split(":")
        NAME = result[1].split(":")
        print(ID, NAME)
        exit(1)
 
    cv2.imshow("QR Code Reader", frame)

    # Press escape to quit
    key = cv2.waitKey(1)
    if key == 27:
        break