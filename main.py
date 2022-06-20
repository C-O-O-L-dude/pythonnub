import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.add_event_handler(
          start_handler, events.NewMessage(pattern=command_process(get_command("START")))
     )
