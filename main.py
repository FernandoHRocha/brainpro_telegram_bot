import telebot
from telebot.types import ReplyKeyboardRemove
import recursos
import os

bot = telebot.TeleBot(os.environ['BRAINPRO_BOT_TOKEN'], parse_mode=None)
canal = os.environ['BRAINPRO_ID_CANAL']
saudacao = recursos.saudacao

produtos =['Aqui estão alguns dos nossos melhores produtos:','Mouse gamer','Teclado mecânico','Estação de trabalho']

@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def boas_vindas(message):
    if(message.chat.id == canal):
        bot.send_message(canal,saudacao)

@bot.message_handler(commands=['start'])
def enviar_saudacao(message):
    bot.send_message(message.from_user.id,saudacao,reply_markup=recursos.markup_saudacao())

@bot.message_handler(lambda m: True)
def enviar_produtos(message):
    for produto in produtos:
        bot.send_message(message.from_user.id,produto,reply_markup=ReplyKeyboardRemove())

bot.polling()