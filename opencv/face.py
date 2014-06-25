'''
    Facial Detection
        - Aim is to be able to detect faces and eyes in images
        - Then to save the face into a directory so we can perform some sort of recognition training on them later
        - We will take images from certain places of similar people, trim their faces off, and then save them
'''

import sys, cv2
import cv2.cv as cv

# global paths
haarPath = './haarcascades/'
facePath = 'haarcascade_frontalface_alt.xml'
eyePath = 'haarcascade_eye.xml'

# Train Haar-cascade Classifier
face_cascade = cv2.CascadeClassifier(haarPath + facePath)
eye_cascade = cv2.CascadeClassifier(haarPath + eyePath)

# Detecting the faces on the image
def detect(path):
    # Read image, and process into opencv
    color = cv2.imread(path)
    gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))

    # Error Checking, and return
    if len(faces) == 0:
        return [], gray
    faces[:, 2:] += faces[:, :2]
    return faces, gray, color

# Drawing a face on the image
def faceBox(faces, gray, color, path):

    # Draw a face in black&white and in color image
    # black and white
    for x1, y1, x2, y2 in faces:
        cv2.rectangle(gray, (x1, y1), (x2, y2), (127, 255, 0), 2)
    # color
    for x1, y1, x2, y2 in faces:
        cv2.rectangle(color, (x1, y1), (x2, y2), (127, 255, 0), 2)

    imageToPrint = path.split('.')[0]

    # save each face in the image
    count = 0
    for x1, y1, x2, y2 in faces:
        print x1, y1, x2, y2
        width = x2 - x1
        height = y2 - y1
        crop_img = color[y1:y1 + height, x1:x1 + width]
        cv2.imwrite(imageToPrint + "_face_" + str(count) + ".jpg", crop_img)
        count = count + 1

    # Save and show the image
    imageToPrint = path.split('.')[0]
    # cv2.imshow(imageToPrint + "_detect.jpg", gray)
    cv2.imwrite(imageToPrint + "_color_detect.jpg", color)
    cv2.imwrite(imageToPrint + "_gray_detect.jpg", gray)

# Drawing a face and eyes on the image
def faceEyeBox(faces, gray, color, imageName):
    for (x, y, w, h) in faces:
        cv2.rectangle(color, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = color[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow(imageName + "_detect.jpg", color)
    cv2.imwrite(imageName + "_gray_detect.jpg", color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    if len(sys.argv) is 1:
        print "Please provide a image name"
    else:
        imageName = sys.argv[1]
        faces, img, color = detect(imageName)
        faceBox(faces, img, color, imageName)
