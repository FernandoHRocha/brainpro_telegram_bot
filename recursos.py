import telebot
from telebot import types

#BOT
nome = 'brainpro_telegram_bot'
saudacao = "Olá, seja bem - vindo (a) ao Canal da Brainpro no Telegram! Somos especialistas em proporcionar soluções de tecnologia através da venda de produtos de Realidade Virtual e equipamentos de informática. Então falaremos muito sobre esse universo por aqui, esperamos que goste! 🧠"

#DADOS
retorno={  
   "retorno":{  
      "produtos":[  
         {
            "produto":{  
               "codigo":"001",
               "descricao":"RX 550 4GB GDDR5 128 BITS SINGLE-FAN",
               "preco":"2253.1000000000",
               "marca":"AMD Radeon",
               "imagem":[
                  {
                    "link": "https://cdn.awsli.com.br/1000x1000/1628/1628166/produto/122163329/c0ba90a69c.jpg",
                  }],
               "estoqueAtual":2,
            }
        },{
            "produto":{  
               "codigo":"002",
               "descricao":"RX 560 4GB GDDR5 128 BITS",
               "preco":"2024.0000000000",
               "marca":"AMD Radeon",
               "imagem":[
                  {
                    "link": "https://cdn.awsli.com.br/1000x1000/1628/1628166/produto/122162448/1fdaad202b.jpg",
                  }],
               "estoqueAtual":3,
            }
        },{
            "produto":{  
               "codigo":"003",
               "descricao":"RTX 3060 TI 8GB GDDR6 256 BITS",
               "preco":"9649.0000000000",
               "marca":"NVIDIA GeForce",
               "imagem":[
                  {
                    "link": "https://cdn.awsli.com.br/1000x1000/1628/1628166/produto/118794486/42240f583b.jpg",
                  }],
               "estoqueAtual":1,
            }
        }
    ]
   }
}

def markup_vazio():
    return types.ReplyKeyboardRemove()

def markup_site():
    """Retorna um botão um com o link da loja."""
    keyboard = [
    [
        types.InlineKeyboardButton("Brainpro Tecnologia",url='www.brainpro.com.br'),
    ]
    ]
    return types.InlineKeyboardMarkup(keyboard)

def markup_saudacao():
    """Retorna as opções primárias de categorias."""
    markup = types.ReplyKeyboardMarkup(row_width=3)
    markup.add(
        types.KeyboardButton('Produtos'),
        types.KeyboardButton('Serviços'),
        types.KeyboardButton('Oportunidades')
        )
    return markup

def markup_categorias_produto():
    """Retorna as categorias de produtos."""
    markup = types.ReplyKeyboardMarkup(row_width=3)
    markup.add(
        types.KeyboardButton('Placa de video'),
        types.KeyboardButton('Monitor'),
        types.KeyboardButton('Periféricos')
        )
    return markup

