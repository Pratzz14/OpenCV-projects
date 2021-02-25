'''
Input - 
    if q is pressed - Terminate the program.
    if c is pressed - Capture the image 
    where the background is black 
    the hand should be white 
    the reflection of white light might be problematic
'''
'''
//TODO: Apply appropriate cv on the image
	# Find cv
	# Get ROI
	# Uderstand accumulated_weight
	# Apply it for the background

//TODO: Understand clicking a  normal image
//TODO: Click multiple images
//TODO: Store in folder with correct naming
//TODO: Make a thumbs up and thumbs down dataset

'''


import cv2
import os
import numpy as np

#Fix the directory
# directory = r'D:\Computer Vision\CV\bin-test\n'
# os.chdir(directory) 

#Input from the web camera
cap = cv2.VideoCapture(0)

i=0 
while(True):
    ret, frame = cap.read()

    #To adjust yourself in the camera
    cv2.imshow("imshow",frame)
    key=cv2.waitKey(30)

    #If 'q' pressed quit the program.
    if key==ord('q'):
        break

    # #If 'c' pressed then capture.
    # if key==ord('c'):
    #     cv2.imshow("imshow2",frame)

    #     i+=1

    #     #Converting BGR to HSV
    #     hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
    #     #Here we have to set the lower and upper bounds of HSV
    #     l_b=np.array((102,102,0))
    #     u_b=np.array((160,255,255))

    #     #Masking the HSV image
    #     mask=cv2.inRange(hsv,l_b,u_b)
    #     res=cv2.bitwise_and(frame,frame,mask=mask)
    #     cv2.imshow('res',res)

    #     #Save the hsv image with the file name.
    #     filename = str(i)+'.png'
    #     cv2.imwrite(filename, res)

# release the capture
cap.release()
cv2.destroyAllWindows()
