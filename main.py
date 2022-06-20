import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(Commands=['start']
                     
  def start(message):
     bot.send_message(mesaage.chat.id,"Hi there 👋, You can easily get shinchan movies in hindi.🍀 just send /getlink")
                   
@bot.message_handler(Commands=['getlink']     
                     
  def start(mesaage):
    msg = 'You can download movies from here...<b>**TTK X [FT] by <a href="https://t.me/shinchan_movies_hindi">**LINK**</a></b>\n<u>✨'
    await message.reply(msg, parse_mode="html")
