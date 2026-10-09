import telebot


bot telebot.TeleBot('8859824190:AAGI4z0-JTuIIjd4Go9gOupghcHH4UNNxpU')


@bot.message_handler(func-lambda msg: msg.txt='/start' or msg.txt == 'سلام')
def start(msg):
bot.send_message(msg.chat.id ,"اخوش اومدی عزیزم")
