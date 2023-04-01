from telebot import types
from pythonping import ping
import telebot
import ipaddress
import subprocess

import virustotal
import abuse
import twoip

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv('config.env')

Token = os.environ.get("Token")
Abuse_API = os.environ.get("Abuse_API")
VT_API = os.environ.get("VT_API")

bot = telebot.TeleBot(Token)

markup_menu=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_start = types.KeyboardButton('/start')
btn_help = types.KeyboardButton('/help')
btn_ip = types.KeyboardButton('/get_ip')
btn_abuse = types.KeyboardButton('/show_abuse')
btn_vt = types.KeyboardButton('/show_vt')
btn_2ip = types.KeyboardButton('/show_2ip')
markup_menu.row(btn_start, btn_help, btn_ip)
markup_menu.row(btn_abuse, btn_vt, btn_2ip)

@bot.message_handler(commands=['start'])
def send(message):
    bot.reply_to(message, 'Чат-бот запущен', reply_markup=markup_menu)

@bot.message_handler(commands=['help'])
def send(message):
    bot.reply_to(message, 'Команды:\n/start - запуск чат-бота\n/help - вывод списка команд\n'
                          '/get_ip - ввод IP-адреса\n/show_abuse - вывод информации с сервиса Abuse\n'
                          '/show_vt - вывод информации с сервиса VirusTotal\n'
                          '/show_2ip - вывод информации с сервиса 2IP', reply_markup=markup_menu)

@bot.message_handler(commands=['get_ip'])
def send(message):
    msg = bot.send_message(message.chat.id, 'введите IP')
    ip = msg
    bot.register_next_step_handler(ip,get)

def check_ip_address(ip_address):
    command = ['ping', '-w', '1', ip_address]
    try:
        subprocess.check_output(command)
        return True
    except subprocess.CalledProcessError:
        return False

def get(message):
    global ip
    ip_addr = message.text
    while(1):
        if check_ip(ip_addr) is True:
            bot.reply_to(message, 'IP-адрес получен', reply_markup=markup_menu)
            bot.send_message(message.chat.id, 'Идёт проверка на доступность')
            if check_ip_address(ip_addr) is True:
                bot.reply_to(message, 'IP-адрес доступен', reply_markup=markup_menu)
            else:
                bot.reply_to(message, 'IP-адрес недоступен', reply_markup=markup_menu)
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
    try:
        result = abuse.abuse(ip, Abuse_API)
        bot.reply_to(message, 'Данные получены', reply_markup=markup_menu)
        bot.send_message(message.chat.id, result)
    except NameError:
        bot.reply_to(message, 'Вы не указали IP-адрес', reply_markup=markup_menu)

@bot.message_handler(commands=['show_vt'])
def send(message):
    try:
        result = virustotal.getVirusTotal(ip, VT_API)
        bot.reply_to(message, 'Данные получены', reply_markup=markup_menu)
        bot.send_message(message.chat.id, result)
    except NameError:
        bot.reply_to(message, 'Вы не указали IP-адрес', reply_markup=markup_menu)

@bot.message_handler(commands=['show_2ip'])
def send(message):
    try:
        result = twoip.twoip(ip)
        bot.reply_to(message, 'Данные получены', reply_markup=markup_menu)
        bot.send_message(message.chat.id, result)
    except NameError:
        bot.reply_to(message, 'Вы не указали IP-адрес', reply_markup=markup_menu)

@bot.message_handler(func=lambda m:True)
def send(message):
    bot.reply_to(message, 'Данное сообщение не является командой', reply_markup=markup_menu)

bot.polling(none_stop=True)
