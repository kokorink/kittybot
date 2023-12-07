# kittybot/send_random_image.py
import os
import requests
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TOKEN')

bot = Bot(token=secret_token)

URL = 'https://cdn2.thecatapi.com/images/3dl.jpg'

chat_id = os.getenv('CHAT_ID')
text = 'Вам телеграмма!'
# Отправка сообщения
bot.send_message(chat_id, text)
# Отправка изображения
bot.send_photo(chat_id, URL)
