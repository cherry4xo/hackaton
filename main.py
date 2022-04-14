from data.db_session import global_init
from data.task import *
from data.headhunter import *
from data.headhunter import *
from data.seeker import *
from data.job import *
from data.replies import *

from datetime import date
from data.db_session import create_session

from data.tools import *

import telebot
import menu
import secret
import texts
import json


global_init("main.sqlite")

session = create_session()

temp_seekers = {}
temp_headhunters = {}
temp_jobs = {}
temp_tasks = {}

bot = telebot.TeleBot(secret.API_TOKEN)


def register_new_seeker_3(message: telebot.types.Message):
    if message.text.isdigit():
        temp_seekers[str(message.chat.id)].age = int(message.text)
    else:
        new_msg = bot.send_message(message.chat.id,
                                   "Кажется это не возраст(, пожауйста попробуй еще раз:")
        bot.register_next_step_handler(new_msg, register_new_seeker_3)
        return
    new_seeker = temp_seekers[str(message.chat.id)]
    session.add(new_seeker)
    session.commit()

    new_msg = bot.send_message(message.chat.id,
                               "Твой профиль готов, можешь приступать к поиску вакансий или заданий и откликаться на них", reply_markup=menu.main_seeker_menu())
    bot.register_next_step_handler(new_msg, register_new_seeker_3)


def register_new_seeker_2(message: telebot.types.Message):
    skills = list(map(str.strip, message.text.split(',')))
    skills = list(map(str.lower, skills))

    skills = json.dumps(skills)
    temp_seekers[str(message.chat.id)].skills = skills

    new_msg = bot.send_message(message.chat.id,
                               "Полезные навыки! А теперь мне нужно узнать сколько тебе лет. Просто пришли число. Например: 17:")
    bot.register_next_step_handler(new_msg, register_new_seeker_3)


def register_new_seeker_1(message: telebot.types.Message):
    temp_seekers[str(message.chat.id)].full_name = message.text

    new_msg = bot.send_message(
        message.chat.id, "Приятно познакомиться, напиши пожалуйста твои навыки через запятую. Например: Python, Backend, Telegram, Office")
    bot.register_next_step_handler(new_msg, register_new_seeker_2)


def add_new_job_4(message: telebot.types.Message):
    new_job = temp_jobs[str(message.chat.id)]

    if message.text.isdigit():
        new_job.wage = int(message.text)
    else:
        new_msg = bot.send_message(message.chat.id,
                                   "Кажется это не число, пожауйста попробуйте еще раз:")
        bot.register_next_step_handler(new_msg, add_new_job_4)
        return

    new_job.headhunter_id = get_user_by_tg_id(session, message.chat.id).id

    session.add(new_job)
    session.commit()

    new_msg = bot.send_message(
        message.chat.id, "Ваша вакансия была опубликована", reply_markup=menu.main_headhunter_menu())


def add_new_job_3(message: telebot.types.Message):
    skills = list(map(str.strip, message.text.split(',')))
    skills = list(map(str.lower, skills))

    skills = json.dumps(skills)
    temp_jobs[str(message.chat.id)].skills = skills
    new_msg = bot.send_message(
        message.chat.id, "Теперь необходио указать зарплату. Просто напишите число без пробелов. Например: 45000 ")
    bot.register_next_step_handler(new_msg, add_new_job_4)


def add_new_job_2(message: telebot.types.Message):
    description = message.text
    temp_jobs[str(message.chat.id)].description = description
    new_msg = bot.send_message(
        message.chat.id, "Принял, чтобы найти подходящего работника напишите неоходимые для вакансии навыки через запяую. Например: python, английский язык, word, excel")
    bot.register_next_step_handler(new_msg, add_new_job_3)


def add_new_task_4(message: telebot.types.Message):
    new_task = temp_tasks[str(message.chat.id)]

    if message.text.isdigit():
        new_task.payment = int(message.text)
    else:
        new_msg = bot.send_message(message.chat.id,
                                   "Кажется это не число, пожауйста попробуйте еще раз:")
        bot.register_next_step_handler(new_msg, add_new_task_4)
        return

    new_task.headhunter_id = get_user_by_tg_id(session, message.chat.id).id

    session.add(new_task)
    session.commit()

    new_msg = bot.send_message(
        message.chat.id, "Ваше задание было опубликовано", reply_markup=menu.main_headhunter_menu())


def add_new_task_3(message: telebot.types.Message):
    skills = list(map(str.strip, message.text.split(',')))
    skills = list(map(str.lower, skills))

    skills = json.dumps(skills)

    temp_tasks[str(message.chat.id)].skills = skills
    new_msg = bot.send_message(
        message.chat.id, "Теперь необходио указать оплату. Просто напишите число без пробелов. Например: 45000 ")
    bot.register_next_step_handler(new_msg, add_new_task_4)


def add_new_task_2(message: telebot.types.Message):
    description = message.text
    temp_tasks[str(message.chat.id)].description = description
    new_msg = bot.send_message(
        message.chat.id, "Принял, чтобы найти подходящего фрилансера напишите неоходимые для вакансии навыки через запяую. Например: python, английский язык, word, excel")
    bot.register_next_step_handler(new_msg, add_new_task_3)


def add_new_task_1(message: telebot.types.Message):
    title = message.text
    temp_tasks[str(message.chat.id)] = Task()
    temp_tasks[str(message.chat.id)].title = title
    new_msg = bot.send_message(
        message.chat.id, "Хорошо, теперь пришлите описание задания")
    bot.register_next_step_handler(new_msg, add_new_task_2)


def add_new_job_1(message: telebot.types.Message):
    title = message.text
    temp_jobs[str(message.chat.id)] = Job()
    temp_jobs[str(message.chat.id)].title = title
    new_msg = bot.send_message(
        message.chat.id, "Хорошо, теперь пришлите описание вакансии")
    bot.register_next_step_handler(new_msg, add_new_job_2)


def register_new_headhunter_3(message: telebot.types.Message):
    field = message.text
    temp_headhunters[str(message.chat.id)].field = field

    headhunter = temp_headhunters[str(message.chat.id)]

    session.add(headhunter)
    session.commit()

    new_msg = bot.send_message(
        message.chat.id, "Профиль компании успешно создан. Добро пожаловать в главное меню!", reply_markup=menu.main_headhunter_menu())


def register_new_headhunter_2(message: telebot.types.Message):
    description = message.text
    temp_headhunters[str(message.chat.id)].description = description
    new_msg = bot.send_message(
        message.chat.id, "Интересное описание! Пожалуйста кратко напишите сферу деятельности вашей компании")
    bot.register_next_step_handler(new_msg, register_new_headhunter_3)


def register_new_headhunter_1(message: telebot.types.Message):
    name = message.text
    temp_headhunters[str(message.chat.id)].name = name
    new_msg = bot.send_message(
        message.chat.id, "Окей, теперь описание вашей компании")
    bot.register_next_step_handler(new_msg, register_new_headhunter_2)


@bot.message_handler(commands=['start'])
def start(msg: telebot.types.Message):
    is_user_exist = get_user_by_tg_id(session, msg.chat.id)
    if is_user_exist:
        user = is_user_exist
        if type(user) == HeadHunter:
            bot.send_message(msg.chat.id, texts.return_user_headhunter,
                             reply_markup=menu.main_headhunter_menu())

        elif type(user) == Seeker:
            bot.send_message(msg.chat.id, texts.return_user_seeker,
                             reply_markup=menu.main_seeker_menu())
    else:
        bot.send_message(msg.chat.id, texts.start_text(),
                         reply_markup=menu.choose_role())


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call: telebot.types.CallbackQuery):
    if call.data.startswith("chooserole_"):
        user_tg_id = call.from_user.id
        role = call.data.split("_")[1]

        if role == "seeker":
            new_seeker = Seeker()
            print(type(user_tg_id))
            new_seeker.tg_user_id = int(user_tg_id)
            temp_seekers[str(user_tg_id)] = new_seeker

            new_msg = bot.edit_message_text(
                "Отлично, теперь отправь мне своё Имя Отчество в одну строку", call.from_user.id, call.message.id)
            bot.register_next_step_handler(new_msg, register_new_seeker_1)

        elif role == "headhunter":
            new_headhunter = HeadHunter()
            new_headhunter.tg_user_id = user_tg_id
            temp_headhunters[str(user_tg_id)] = new_headhunter

            new_msg = bot.edit_message_text(
                "Пришлите пожалуйста название компании", call.from_user.id, call.message.id)
            bot.register_next_step_handler(new_msg, register_new_headhunter_1)

    elif call.data.startswith("makereply_"):
        job_id = int(call.data.split('_')[1])
        job = session.query(Job).filter(Job.id == job_id).first()
        user = get_user_by_tg_id(session, call.from_user.id)

        add_job_reply(session,  job,  user)

    elif call.data == "add_job":
        new_msg = bot.edit_message_text(
            "Напишите проффесию", call.from_user.id, call.message.id)
        bot.register_next_step_handler(new_msg, add_new_job_1)

    elif call.data == "add_task":
        new_msg = bot.edit_message_text(
            "Напишите название задания", call.from_user.id, call.message.id)
        bot.register_next_step_handler(new_msg, add_new_task_1)

    elif call.data == "my_jobs":
        text = "Ваши вакансии:\n"

        headhunter = get_user_by_tg_id(session, call.from_user.id)
        jobs = list(headhunter.jobs)
        if len(jobs) == 0:
            new_msg = bot.edit_message_text(
                "У вас нет вакансий", call.from_user.id, call.message.id, reply_markup=menu.main_seeker_menu())

        else:
            for job in jobs:
                text += job.title + "\n"

            new_msg = bot.edit_message_text(
                text, call.from_user.id, call.message.id, reply_markup=menu.main_headhunter_menu())

    elif call.data == "main_menu_seeker":
        new_msg = bot.edit_message_text(
            "Выбери пункт меню:", call.from_user.id, call.message.id, reply_markup=menu.main_seeker_menu())

    elif call.data == "my_jobs":
        jobs = list(session.query(Job).filter(
            Job.headhunter_id == call.from_user.id).all())

        new_msg = bot.edit_message_text(
            "Выберите вакансию:", call.from_user.id, call.message.id, reply_markup=menu.my_jobs(jobs))

    elif call.data == "my_tasks":
        tasks = list(session.query(Task).filter(
            Task.headhunter_id == call.from_user.id).all())

        new_msg = bot.edit_message_text(
            "Выберите задание:", call.from_user.id, call.message.id, reply_markup=menu.my_tasks(tasks))

    elif "seacrch_job" in call.data:
        seeker = get_user_by_tg_id(session, call.from_user.id)
        skills = json.loads(seeker.skills)
        job = get_relative_job(session, seeker.tg_user_id, skills)

        if job is None:
            new_msg = bot.edit_message_text(
                "Нет подходящих вакансий( ", call.from_user.id, call.message.id, reply_markup=menu.main_seeker_menu())
        else:
            text = f"Как тебе вакансия? \n"
            text += f"{job.title}\n\Зарплата:\n"
            text += f"{job.wage}р в мес\n\nОписание:\n"
            text += f"{job.description[:250]}\nНавыки:\n"
            text += " ,".join(json.loads(job.skills))
            new_msg = bot.edit_message_text(
                text, call.from_user.id, call.message.id, reply_markup=menu.watch_job(job.id))

    elif "seacrch_task" in call.data:
        seeker = get_user_by_tg_id(session, call.from_user.id)
        skills = json.loads(seeker.skills)
        task = get_relative_task(session, seeker.tg_user_id, skills)

        if task is None:
            new_msg = bot.edit_message_text(
                "Нет подходящих заданий( ", call.from_user.id, call.message.id, reply_markup=menu.main_seeker_menu())
        else:
            text = f"Как тебе задание? \n"
            text += f"{job.title}\n\Стоимость:\n"
            text += f"{job.payment}р\n\nОписание:\n"
            text += f"{job.description[:250]}\nНавыки:\n"
            text += " ,".join(json.loads(job.skills))
            new_msg = bot.edit_message_text(
                text, call.from_user.id, call.message.id, reply_markup=menu.watch_job(job.id))


if __name__ == '__main__':
    bot.infinity_polling()
