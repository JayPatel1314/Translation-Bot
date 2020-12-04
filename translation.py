import telebot
from googletrans import Translator
from flask import Flask, request
import os

TOKEN = '<Token>'

bot = telebot.TeleBot(TOKEN)

server = Flask(__name__)

translator = Translator(service_urls=[

        'translate.google.com',

        'translate.google.co.in',

    ])

@bot.message_handler(func=lambda message:True)

def send(message):

  while True:

    try:

      translation = translator.translate(message.text,dest='hi')

      break

    except Exception:

      continue	  bot.send_message(message.chat.id,translation.pronunciation)

@server.route('/' + TOKEN, methods=['POST'])

def getMessage():  

  bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])

  return "!", 200

@server.route("/")

def webhook():

  bot.remove_webhook()

  bot.set_webhook(url='<URL>' + TOKEN)

  return "!", 200
