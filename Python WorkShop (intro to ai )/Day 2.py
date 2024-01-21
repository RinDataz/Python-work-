'''
this code sets up a Telegram bot that responds to three commands: /start, /help, and /python. 
When a user sends the /start or /help command, the bot responds with a greeting message.
When a user sends the /python command, the bot responds with a message containing a link to a Python course on YouTube.
'''

import telebot

TOKEN = '' #Token removed for privacy and security reasons 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    helo_message = "Hello, I'm Adnan. To see the Python course, click /python."
    bot.send_message(message.chat.id, helo_message)

@bot.message_handler(commands=['python'])
def handle_python_command(message):
    linkpython = "\nHere you go! \nhttps://www.youtube.com/live/l3V5hcPdFTw?si=o7jt6qszI54D9mKX"
    bot.send_message(message.chat.id, linkpython)

bot.polling()
