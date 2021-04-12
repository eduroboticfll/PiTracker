"""
- This module saves images and a log file.
- Images are saved in a folder.
- Folder should be created manually with the name "DataCollected"
- The name of the image and the steering angle is logged
in the log file.
- Call the saveData function to start.
- Call the saveLog function to end.
- If runs independent, will save ten images as a demo.
"""

import pandas as pd
import os
import cv2
from datetime import datetime

global imgList, steeringList
countFolder = 0
count = 0
imgList = []
steeringList = []

# GET CURRENT DIRECTORY PATH
myDirectory = os.path.join(os.getcwd(), 'DataCollected')
print(myDirectory)

# CREATE A NEW FOLDER BASED ON THE PREVIOUS FOLDER COUNT
while os.path.exists(os.path.join(myDirectory, f'IMG{str(countFolder)}')):
    countFolder += 1
newPath = myDirectory + "/IMG" + str(countFolder)
os.makedirs(newPath)


# SAVE IMAGES IN THE FOLDER
def savedata(img, direccion):
    global imgList, steeringList
    now = datetime.now()
    timestamp = str(datetime.timestamp(now)).replace('.', '')
    # print("timestamp =", timestamp)
    filename = os.path.join(newPath, f'Image_{timestamp}.jpg')
    cv2.imwrite(filename, img)
    imgList.append(filename)
    steeringList.append(direccion)


# SAVE LOG FILE WHEN THE SESSION ENDS
def savelog():
    global imgList, steeringList
    rawdata = {'Image': imgList,
               'Steering': steeringList}
    df = pd.DataFrame(rawdata)
    df.to_csv(os.path.join(myDirectory, f'log_{str(countFolder)}.csv'), index=False, header=False)
    print('Log Saved')
    print('Total Images: ', len(imgList))


if __name__ == '__main__':
    cap = cv2.VideoCapture(-1)
    for x in range(10):
        _, img = cap.read()
        savedata(img, 0.5)
        cv2.waitKey(1)
        cv2.imshow("Image", img)
    savelog()