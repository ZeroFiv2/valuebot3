import telebot
from extensions import APIException, CurrencyConverter

bot = telebot.TeleBot('6711984271:AAHmY7gB8x5b_WF5bdZc6yXFFwjhmT2cklQ')

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.reply_to(message, "Привет! Я могу помочь узнать цену на определенное количество валюты. Просто напиши мне сообщение в формате <имя валюты1> <имя валюты2> <количество>.")

@bot.message_handler(commands=['values'])
def handle_values(message):
    bot.reply_to(message, "Доступные валюты: евро, доллар, рубль")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        base, quote, amount = message.text.split()
        converted_amount = CurrencyConverter.get_price(base, quote, amount)
        bot.reply_to(message, f"{amount} {base} = {converted_amount} {quote}")
    except APIException as e:
        bot.reply_to(message, f"Ошибка: {e}")

bot.polling()