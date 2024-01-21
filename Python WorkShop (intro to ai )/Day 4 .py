'''
This code checks whether someone is holding a phone or not when a picture is sent to the bot
'''
import cv2
import numpy as np
import telebot
from telebot import types

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
   
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("photo.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    image = cv2.imread("photo.jpg")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_roi = gray[y:y + h, x:x + w]
        edges = cv2.Canny(face_roi, 50, 150)
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=30, maxLineGap=10)

        if lines is not None:
         
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imwrite("result.jpg", image)

            with open("result.jpg", 'rb') as result_file:
                bot.send_photo(message.chat.id, result_file, "Phone detected!")

            return

    bot.reply_to(message, "no phone detected in the photo")

if __name__ == "__main__":
    bot.polling(none_stop=True)
