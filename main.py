import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
import recursos
import os

bot = telebot.TeleBot(os.environ['BRAINPRO_BOT_TOKEN'], parse_mode=None)
canal = os.environ['BRAINPRO_ID_CANAL']
saudacao = recursos.saudacao

@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def boas_vindas(message):
    if(message.chat.id == canal):
        bot.send_message(canal,saudacao)

@bot.message_handler(commands=['start'])
def enviar_saudacao(message):
    bot.send_message(message.from_user.id,saudacao,reply_markup=recursos.markup_saudacao())

@bot.message_handler(func=lambda m: m.text == "Produtos")
def enviar_produtos(m):
    bot.send_message(m.chat.id,'Escolha uma categoria de produtos.',reply_markup=recursos.markup_categorias_produto())

@bot.message_handler(func=lambda m: m.text == "Placa de video")
def categoria_placa_video(m):
    bot.send_message(m.chat.id,'Os nossos produtos são:',reply_markup=recursos.markup_vazio())
    enviar_produtos(m)

def enviar_produtos(m):
    for produto in recursos.retorno['retorno']['produtos']:
        marca = produto['produto']['marca']
        descricao = produto['produto']['descricao']
        imagem = produto['produto']['imagem'][0]['link']
        preco = str('R$ '+str(round(float(produto['produto']['preco']),2)))
        bot.send_photo(m.chat.id,imagem,marca+'\n'+descricao+'\n'+preco,reply_markup=recursos.markup_site())

def printar():
    print('produto')

bot.polling()