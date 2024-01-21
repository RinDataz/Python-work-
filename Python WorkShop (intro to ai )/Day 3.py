'''
this code sets up a Telegram bot that can receive photo messages, detect faces in the photos using OpenCV's Haar cascade classifier, and send back the processed images with rectangles around the detected faces.
'''
import telebot
import cv2
import numpy as np
from io import BytesIO

TOKEN = ''  # Token removed for privacy and security reasons
bot = telebot.TeleBot(TOKEN)

# Handler for processing photo messages
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # Get the file ID of the received photo
    file_id = message.photo[-1].file_id

    # Retrieve file information from Telegram Bot API
    file_info = bot.get_file(file_id)

    # Download the file
    file = bot.download_file(file_info.file_path)

    # Convert the downloaded file into a NumPy array
    np_array = np.frombuffer(file, dtype=np.uint8)

    # Decode the NumPy array into an image using OpenCV
    img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load the face cascade classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces on the original image
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Save the processed image
    processed_image_path = "processed_image.jpg"
    cv2.imwrite(processed_image_path, img)

    # Open the processed image in binary mode
    processed_image = open(processed_image_path, "rb")

    # Send the processed image as a photo message
    bot.send_photo(message.chat.id, processed_image)

    # Send a text message indicating that faces have been detected
    bot.send_message(message.chat.id, "Face detected")

# Start the bot and keep it running
bot.polling()