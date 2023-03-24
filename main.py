import telebot

# Replace YOUR_BOT_TOKEN with your own bot's token
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hi there! I am your new bot.')

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

bot.polling()
