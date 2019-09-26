import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import csv
import time

import ctypes  # An included library with Python install.   


# Start webcame
cap = cv2.VideoCapture(0)
registered_people = {}

with open('PurchasedTickets.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        registered_people.update({row[0]:row[1][1:]})


while True:
    _, frame = cap.read()
    decodedObjects = pyzbar.decode(frame)

    try:
        # Read QR code data
        for obj in decodedObjects:
            print(obj.type)
            print(obj.data)
            # ID = result[0].split(":")
            # NAME = result[1].split(":")
            # if (registered_people[ID[1]] == NAME[1]):
            #     registered_people.update({ID[1]:[NAME[1], "Checked"]})
            #     ctypes.windll.user32.MessageBoxW(0, "This is an accepted ticket", "Accepted", 1)
            # else:
            #     foo = registered_people[ID[1]]
            #     if (foo[1] == "Checked"):
            #         ctypes.windll.user32.MessageBoxW(0, "This ticket has already been checked. Please make sure the person entering with this ticket is " + foo[0], "Already Checked", 1)
            #     else:
            #         ctypes.windll.user32.MessageBoxW(0, "This ticket is not recognised, reject this ticket", "Reject", 1)

    except:
        ctypes.windll.user32.MessageBoxW(0, "This ticket is not recognised, reject this ticket", "Reject", 1)
        pass

    cv2.imshow("QR Code Reader", frame)

    # Press escape to quit
    key = cv2.waitKey(1)
    if key == 27:
        break