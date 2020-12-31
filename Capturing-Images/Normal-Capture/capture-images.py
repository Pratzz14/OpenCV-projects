'''
Input - 
    if q is pressed - Terminate the program.
    if c is pressed - Capture the image.
'''

import cv2
import os

#Fix the directory
directory = r'D:\Computer Vision\CV\bin-test\n'
os.chdir(directory) 

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

    #If 'c' pressed then capture.
    if key==ord('c'):

        #Show the captured image
        cv2.imshow("imshow2",frame)

        #Save the image with the file name.
        filename = str(i)+'.png'
        cv2.imwrite(filename, frame)

# release the capture
cap.release()
cv2.destroyAllWindows()
