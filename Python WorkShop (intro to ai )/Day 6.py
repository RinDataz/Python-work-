'''
This code uses OpenCV to detect faces in a video.
It loads a face detection classifier, opens a video file, reads frames from the video, converts each frame to grayscale, detects faces in the frame, draws rectangles around the detected faces, and displays the frame with the rectangles.
The code continues looping until the 'ESC' key is pressed, and it releases the video file and closes the display window.
'''
import cv2

face_detector = cv2.CascadeClassifier('myfacedetector.xml')

cape = cv2.VideoCapture('vid.mp4')

if not cape.isOpened():
    print('unable to play video')
    exit()

color = (255, 0, 0)
thickness = 5

while True:
    ret, img = cape.read()

    if not ret:
        print('unable to read frame')
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness)

    cv2.imshow('Video', img)

    cv2.waitKey(30)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cape.release()
cv2.destroyAllWindows()