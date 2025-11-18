import telebot

bot = telebot.TeleBot('7024503878:AAF-vE9cLNVam9NzrhXmQPwqZR5yAxBtrn4')
print('hey')

#start command
@bot.message_handler(commands=['start'])
def start_message(message):
    user = message.chat.id
    bot.send_message(user,'Hello \n give . ')

#main code
@bot.message_handler(content_types=['text'])
def send_text(message):
    user = message.chat.id
    
    if message.text == "help":
        bot.send_message(user,'instruction ... ')

    elif message.text == '🤍':
        bot.send_message(user, 'you too ⛄')

    elif message.text == 'bye':
        bot.send_message(user, 'well')
        bot.send_message(user, 'see you')
    else:
        bot.send_message(message.chat.id, '¯\_(ツ)_/¯ ')

bot.infinity_polling()

   


# bot.send_photo(message.chat.id, 'https://drive.google.com/file/d/1DuCZu_U4R2xA0ZNzr6ln2EczkWKHyaiE/view?usp=sharing')



