from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from enum import Enum


class Btn_text_menu(str, Enum):
    START_SEARCH = '📨  Розпочати пошук'
    # ADD_INF = '📨 Додати на блокування'
    # CALLBACK = '🤙Зворотній зв\'язок📱'
    ABOUT = '📜Про бот'
    INSTRUCTION = '🤙 Інструкція'
    SEND_MESSAGE = '👋 Сайт'
    # HELP = '🆘 Допомога ЗСУ'
    MENU = '🌍 Меню'


class Btn_text_controller_inf(str, Enum):
    SKIP = '⏭️Пропустити'


class Btn_main_menu:
    btn_start_blocking = KeyboardButton(Btn_text_menu.START_SEARCH)
    btn_about = KeyboardButton(Btn_text_menu.ABOUT)
    btn_send_message = KeyboardButton(Btn_text_menu.SEND_MESSAGE)
    btn_instruction = KeyboardButton(Btn_text_menu.INSTRUCTION)
    btn_main_menu = KeyboardButton(Btn_text_menu.MENU)
    list_btn = ReplyKeyboardMarkup(resize_keyboard=True)\
        .row(btn_start_blocking)\
        .row(btn_about, btn_send_message)\
        .row(btn_instruction)


class Btn_controller:
    btn_skip = KeyboardButton(Btn_text_controller_inf.SKIP)

    list_btn_req = ReplyKeyboardMarkup(resize_keyboard=True).row(Btn_main_menu.btn_main_menu)
    list_btn = ReplyKeyboardMarkup(resize_keyboard=True).row(Btn_main_menu.btn_main_menu, btn_skip)








