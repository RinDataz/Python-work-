'''
This code performs car detection in an image using OpenCV's Haar cascade classifier.
It loads the classifier file, downloads an image from a URL, resizes the image, converts it to grayscale, and applies the cascade classifier to detect cars.
It then draws rectangles around the detected cars and displays the image with the rectangles.
Finally, it prints the number of detected cars.
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
import requests
from PIL import Image

car_cascade = cv2.CascadeClassifier('haarcascade_car.xml')

image = Image.open(requests.get('https://media.wired.com/photos/593256b42a990b06268a9e21/master/pass/traffic-jam-getty.jpg', stream=True).raw)
image = image.resize((450, 250))
image_arr = np.array(image)

gray = cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY)
cars = car_cascade.detectMultiScale(gray, 1.1, 1)

car_count = 0

for (x, y, w, h) in cars:
    cv2.rectangle(image_arr, (x, y), (x + w, y + h), (0, 0, 255), 2)
    car_count += 1

plt.imshow(cv2.cvtColor(image_arr, cv2.COLOR_BGR2RGB))
plt.title("Car Detection")
plt.show()

print("Number of cars detected:", car_count)