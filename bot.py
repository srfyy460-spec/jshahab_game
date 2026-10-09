import telebot


bot = telebot.TeleBot('8859824190:AAFq1Hz_WQ91MEfZovRsv7Z4ba8DW5hCEYI) 

                      
@bot.message_handler(func-lambda msg: msg.text =='/start' or msg.text == 'سلام')
def start(msg):
    bot.send_message(msg.chat.id,"اخوش اومدی عزیزم")

                     
@bot.message_handler(func-lambda msg: True')
def other(msg):
    bot.send_message(msg.chat.id,"نمیدانم")
 


bot.infinity_polling()
