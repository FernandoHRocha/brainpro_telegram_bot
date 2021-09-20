import telebot
from telebot import types
#BOT
nome = 'brainpro_telegram_bot'
saudacao = "Olá, seja bem - vindo (a) ao Canal da Brainpro no Telegram! Somos especialistas em proporcionar soluções de tecnologia através da venda de produtos de Realidade Virtual e equipamentos de informática. Então falaremos muito sobre esse universo por aqui, esperamos que goste! 🧠"

def markup_saudacao():
    """
    Retorna as opções primárias de categorias.
    """
    markup = types.ReplyKeyboardMarkup(row_width=3)
    markup.add(
        types.KeyboardButton('Produtos'),
        types.KeyboardButton('Serviços'),
        types.KeyboardButton('Oportunidades')
        )
    return markup