import telebot
config = {
    'name': 'echosuperbot_bot',
    'token': '5790645448:AAE5PTjv3qkV8NBrNAw2H18tgCcMepcSVwE'
}
sanktum = telebot.TeleBot(config['token'])
@sanktum.message_handler(content_types= ['text'])
# def get_txt(message):
#     if message.text == "Hello":
#         sanktum.send_message(message.chat.id, "hello user!")
def repeat_all_messages(message):
    sanktum.send_message(message.chat.id, message.text)
if __name__ == '__main__':
     sanktum.infinity_polling()
sanktum.polling(none_stop=True, interval=0)