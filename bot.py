import telebot
import os

# Pegando o token do ambiente (Railway vai guardar isso pra nós)
TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Oi! Eu sou o MatchMe 🤖✨ Seu assistente para encontrar conexões especiais!")

# Resposta padrão
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "Recebi sua mensagem: " + message.text)

print("Bot rodando...")

bot.polling()
