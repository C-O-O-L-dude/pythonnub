import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(Commands=['start']
                     
  def start(message):
     bot.send_message(mesaage.chat.id,"Hi there 👋, You can easily get shinchan movies in hindi.🍀 just send /getlink")
                   
@bot.message_handler(Commands=['getlink']     
                     
  def getlink(mesaage):
     bot.send_message(message.chat.id,"from here you can download shinchan movies...."
