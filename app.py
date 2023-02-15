import telebot
from config import keys, TOKEN
from utils import class ConvertionException, Converter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, 'Вас приветствует бот курса валют. Данный бот даёт актуальную информацию по конвертации валюты на сегодняшний день. \n 1. Введите из какой валюты необходима конвертация. \n 2. В какую валюту необходила конвертация. \n 3. Введите количество первой валюты. \n ВВедите команду </value> чтобы узнать список доступных валют')



@bot.message_handler(commands=['value'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values=message.text.split('')

    if len(values) > 3:
        raise ConvertionException('слишком много параметров')

    quote, base, amount = values

    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tiker]}&tsyms={base_tiker}')
    total_base = json.loads(r.content)[keys[base]]
    text = f'Цена {amount} {quote} в {base} = {total_base}'
    bot.send_message(message.chat.id, text)

bot.polling()

