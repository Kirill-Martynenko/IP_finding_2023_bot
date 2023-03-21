from telebot import types
import telebot
import config
import virustotal
import abuse
import twoip

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

ip = '0.0.0.0'

def check_ip(ip_addr):#проверка правильности IP-адреса
    if (len(ip_addr)) == 0:
        return False
    k = 0
    t = 0
    for i in range(0, len(ip_addr)):
        if ((ip_addr[i] >= '0') and (ip_addr[i] <= '9')):
            k += 1
        else:
            if ip_addr[i] == '.':
                if(k > 3):
                    return False
                else:
                    t += 1
                    k = 0
            else:
                return False
        if(t > 4):
            return False
    return True

@bot.message_handler(commands=['start'])
def send(message):
    bot.reply_to(message, 'Чат-бот запущен', reply_markup=markup_menu)

@bot.message_handler(commands=['get_ip'])
def send(message):
    ip_addr = message.text[8:len(message.text)].split()
    while(1):
        if check_ip(ip_addr) is True:
            bot.reply_to(message, 'IP-адрес получен', reply_markup=markup_menu)
            ip = ip_addr
            break
        else:
            bot.reply_to(message, 'Ошибка ввода', reply_markup=markup_menu)
            break

@bot.message_handler(commands=['show_abuse'])
def send(message):
    result = abuse.abuse(ip, config.Abuse_API)
    bot.reply_to(message, 'Данные получены', reply_markup=markup_menu)

@bot.message_handler(commands=['show_virus_total'])
def send(message):
    result = virustotal.getVirusTotal(ip, config.VT_API)
    bot.reply_to(message, 'Данные получены', reply_markup=markup_menu)

@bot.message_handler(commands=['show_2IP'])
def send(message):
    result = twoip.twoip(ip)
    bot.reply_to(message, 'Данные получены', reply_markup=markup_menu)

@bot.message_handler(func=lambda m:True)
def send(message):
    bot.reply_to(message, 'Данное сообщение не является командой', reply_markup=markup_menu)

bot.polling(none_stop=True)