from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


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
        "Искать вакансии", callback_data="seacrch_job"))
    keyboard.add(InlineKeyboardButton(
        "Искать задания", callback_data="seacrch_task"))
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
