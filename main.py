from telebot import types
import telebot
import config

bot = telebot.TeleBot(config.Token)

@bot.message_handler(commands=['start'])
def send(message):
    bot.reply_to(message, 'Чат-бот запущен')

bot.polling(none_stop=True)