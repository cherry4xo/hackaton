import telebot
import menu
from data.db_session import global_init, create_session
import secret
from data import test
import menu


global_init("main.sqlite")

bot = telebot.TeleBot(secret.API_TOKEN)

class User:
    def __init__(self):
        self.name = 'Name'
        self.surname = 'Surname'
        self.accept = False
        self.tg_user_id = 0
        
    @property
    def full_name(self):
        return f'{self.name} {self.surname}'.title()


@bot.message_handler(commands=['getobjects'])
def get_objects(msg: telebot.types.Message):
    res = test.get_all_objects()
    bot.send_message(msg.chat.id, res)


@bot.message_handler(commands=['addobject'])
def add_object(msg: telebot.types.Message):
    res = test.add_new_test_object()

    bot.send_message(msg.chat.id, res)

@bot.message_handler(commands=['start'])
def start(msg: telebot.types.Message):
    chat_id = msg.chat.id
    user_name = msg.from_user.first_name
    bot.send_message(chat_id, f"Welcome, {user_name}", reply_markup=menu.main_menu())

@bot.message_handler(content_types=['text'])
def reply_text(msg: telebot.types.Message):
    bot.send_message(msg.chat.id, msg.text.upper())


if __name__ == '__main__':
    bot.enable_save_next_step_handlers(delay=2)
    bot.load_next_step_handlers()   
    bot.infinity_polling()
