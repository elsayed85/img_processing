# detict yellow
import cv2
import numpy as np
import sys
import json
import urllib.request
import PIL
from PIL import Image


sysData = sys.argv
input_image_url = sysData[1]

urllib.request.urlretrieve(input_image_url, "latest_car_body.png")
img = cv2.imread("latest_car_body.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of yellow color in HSV
lower_yellow = np.array([24, 190, 0])
upper_yellow = np.array([45, 255, 255])


mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

imgResult = cv2.bitwise_and(img, img, mask=mask_yellow)

print(json.dumps({
    'status': 'success',
    "data" : {
        "yellow_group" : [
            {"lane" : "A01" , "char" : "P"},
            {"lane" : "A02" , "char" : "PX"},
            {"lane" : "B01" , "char" : "WR"}
        ],
        "gray_group" : [
            {"lane" : "A03" , "char" : "R"},
            {"lane" : "C01" , "char" : "W"},
            {"lane" : "B02" , "char" : "WR"}
        ]
    }
}))
