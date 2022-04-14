from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import random


def my_jobs(jobs: list):
    keyboard = InlineKeyboardMarkup()

    for job in jobs:
        keyboard.add(InlineKeyboardButton(job.title, callback_data=f"choosejob_{job.id}"))

    return keyboard


def my_tasks(tasks: list):
    keyboard = InlineKeyboardMarkup()

    for task in tasks:
        keyboard.add(InlineKeyboardButton(
            task.title, callback_data=f"choosetask_{task.id}"))

    return keyboard

def main_headhunter_menu():
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton(
        "Мои вакансии", callback_data="my_jobs"))
    keyboard.add(InlineKeyboardButton(
        "Мои задания", callback_data="my_tasks"))
    keyboard.add(InlineKeyboardButton(
        "Добавить вакансию", callback_data="add_job"))
    keyboard.add(InlineKeyboardButton(
        "Добавить задание", callback_data="add_task"))
    # keyboard.add(InlineKeyboardButton("Профиль", callback_data="profile"))

    return keyboard


def main_seeker_menu():
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton(
        "Искать вакансии", callback_data=f"seacrch_job_{random.randint(1, 100)}"))
    keyboard.add(InlineKeyboardButton(
        "Искать задания", callback_data=f"seacrch_task_{random.randint(1, 100)}"))
    keyboard.add(InlineKeyboardButton(
        "Мои отклики", callback_data="my_callbacks"))
    # keyboard.add(InlineKeyboardButton(
    #     "Профиль", callback_data="profile"))

    return keyboard


def choose_role():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(
        "Работадатель", callback_data="chooserole_headhunter"))
    keyboard.add(InlineKeyboardButton(
        "Соискатель", callback_data="chooserole_seeker"))

    return keyboard


def watch_job(job_id):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("⏩", callback_data=f"seacrch_job"))
    keyboard.add(InlineKeyboardButton(
        "✅ Откликнуться", callback_data=f"makereply_{job_id}"))
    keyboard.add(InlineKeyboardButton(
        "🟥 В главное меню", callback_data="main_menu_seeker"))

    return keyboard
