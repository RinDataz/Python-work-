'''
Cat face detection
'''

import cv2
import numpy as np

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Define the Haar cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_CatFrontalcatface.xml')

# Loop over the frames of the video
while True:
    # Capture the frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw a rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Write "cat" above each detected face
    for (x, y, w, h) in faces:
        cv2.putText(frame, 'cat', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('frame', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
cap.release()

# Close all windows
cv2.destroyAllWindows()
