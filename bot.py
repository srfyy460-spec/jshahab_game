import telebot

bot = telebot.TeleBot('8859824190:AAFq1Hz_WQ91MEfZovRsv7Z4ba8DW5hCEYI')

@bot.message_handler(func=lambda msg: msg.text in ['/start', 'سلام'])
def other(msg):
    bot.send_message(msg.chat.id, "خوش اومدی عزیزم ❤️")

bot.infinity_polling()
