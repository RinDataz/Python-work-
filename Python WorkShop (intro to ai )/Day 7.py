'''
This code performs real-time face detection using the webcam.
It captures frames from the default camera (index 0), converts each frame to grayscale, detects faces in the grayscale frame using the Haar cascade classifier, draws rectangles around the detected faces, and displays the frame with the face rectangles.
The program continues to run until the 'q' key is pressed, at which point the camera is released and all windows are closed.
'''

import cv2

# Open the default camera (index 0)
cap = cv2.VideoCapture(0)

# Load the face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Read frames from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    # scaleFactor: Parameter specifying how much the image size is reduced at each image scale.
    # minNeighbors: Parameter specifying how many neighbors each candidate rectangle should have to retain it.
    # minSize: Minimum possible object size. Objects smaller than this are ignored.
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame with face rectangles
    cv2.imshow('Face Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()