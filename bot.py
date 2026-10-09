import telebot


bot = telebot.TeleBot('CGEJBF0XXPFCFNZPECJNUEMQLARGJPBDUYHKMNINHDARAVSYOQQZCRRCNPINUNDK') 

                      
@bot.message_handler(func-lambda msg: msg.text =='/start' or msg.text == 'سلام')
def start(msg):
    bot.send_message(msg.chat.id,"اخوش اومدی عزیزم")

                     
@bot.message_handler(func-lambda msg: True')
def other(msg):
    bot.send_message(msg.chat.id,"نمیدانم")
 


bot.infinity_polling()
