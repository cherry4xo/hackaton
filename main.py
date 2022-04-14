import telebot
import menu
from data.db_session import global_init, create_session
import secret
from data import test


global_init("main.sqlite")

bot = telebot.TeleBot(secret.API_TOKEN)


@bot.message_handler(commands=['start'])
def start(msg: telebot.types.Message):
    bot.send_message(msg.chat.id, "Hello, dodik")


@bot.message_handler(commands=['getobejcts'])
def start(msg: telebot.types.Message):
    res = test.get_all_objects()
    bot.send_message(msg.chat.id, res)


@bot.message_handler(commands=['addobject'])
def start(msg: telebot.types.Message):
    res = test.add_new_test_object()

    bot.send_message(msg.chat.id, res)


@bot.message_handler(content_types=['text'])
def start(msg: telebot.types.Message):
    bot.send_message(msg.chat.id, msg.text.upper())


if __name__ == '__main__':
    bot.enable_save_next_step_handlers(delay=2)
    bot.load_next_step_handlers()
    bot.infinity_polling()
