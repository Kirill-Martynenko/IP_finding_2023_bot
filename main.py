from telebot import types
import telebot
import config
<<<<<<< HEAD
<<<<<<< HEAD
import virustotal
import abuse
import twoip
import ipaddress
bot = telebot.TeleBot(config.Token)

markup_menu=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_start = types.KeyboardButton('/start')
btn_help = types.KeyboardButton('/help')
btn_ip = types.KeyboardButton('/get_ip')
btn_abuse = types.KeyboardButton('/show_abuse')
btn_vt = types.KeyboardButton('/show_virus_total')
btn_2ip = types.KeyboardButton('/show_2IP')
markup_menu.row(btn_start, btn_help, btn_ip)
markup_menu.row(btn_abuse, btn_vt, btn_2ip)




@bot.message_handler(commands=['start'])
def send(message):
    bot.reply_to(message, 'Чат-бот запущен', reply_markup=markup_menu)

@bot.message_handler(commands=['get_ip'])
def send(message):
    msg = bot.send_message(message.chat.id, 'введите IP')
    ip = msg
    bot.register_next_step_handler(ip,get)

def get(message):
    global ip
    ip_addr = message.text
    while(1):

        if check_ip(ip_addr) is True:
            bot.reply_to(message, 'IP-адрес получен', reply_markup=markup_menu)
            ip = ip_addr
            break
        else:
            bot.reply_to(message, 'Ошибка ввода', reply_markup=markup_menu)
            break

def check_ip(ip_addr):#проверка правильности IP-адреса
    try:
        ipaddress.ip_address(ip_addr)
    except ValueError:
        return False
    else:
        return True


@bot.message_handler(commands=['show_abuse'])
def send(message):

    result = abuse.abuse(ip, config.Abuse_API)
    bot.reply_to(message, 'Данные получены', reply_markup=markup_menu)
    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=['show_virus_total'])
def send(message):
    result = virustotal.getVirusTotal(ip, config.VT_API)
    bot.reply_to(message, 'Данные получены', reply_markup=markup_menu)
    bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['show_2IP'])
def send(message):
    result = twoip.twoip(ip)
    bot.reply_to(message, 'Данные получены', reply_markup=markup_menu)
    bot.send_message(message.chat.id, result)

@bot.message_handler(func=lambda m:True)
def send(message):
    bot.reply_to(message, 'Данное сообщение не является командой', reply_markup=markup_menu)
=======
=======

bot = telebot.TeleBot(config.Token)

@bot.message_handler(commands=['start'])
def send(message):
    bot.reply_to(message, 'Чат-бот запущен')
>>>>>>> parent of e34a3f3 (bot can get IP)

bot = telebot.TeleBot(config.Token)

@bot.message_handler(commands=['start'])
def send(message):
    bot.reply_to(message, 'Чат-бот запущен')
>>>>>>> parent of e34a3f3 (bot can get IP)

bot.polling(none_stop=True)
