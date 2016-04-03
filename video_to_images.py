from time import sleep
import numpy as np
import cv2
import os
import datetime

print('Press e to exit')

cap = cv2.VideoCapture('_videos/VID_20160228_141023.mp4')
i = 0
dir_name = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
source = '_images/' + dir_name
os.mkdir(source)

while(True):
    # Capture frame-by-frame (last picture before wait)
    ret, frame = cap.read()
    # Capture picture now
    ret, frame = cap.read()

    # Our operations on the frame come here
    # Modify image
#    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imwrite(source + '/frame' + str(i) + '.jpg', frame)
    print (datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

#    sleep(1)
    i += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
