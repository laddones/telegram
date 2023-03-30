from aiogram import types
from aiogram.types import ParseMode

from MS import state_m
from config.loader import anti_flood, dp, bot, api_storage_module
from keyboard import keyboards
from keyboard.keyboards import Btn_text_menu
from modules.models.text_enum import Texts


@dp.message_handler(state=None)
@dp.throttled(anti_flood, rate=1)
async def main_menu(message: types.Message):
    if message.text == Btn_text_menu.START_SEARCH:
        await message.answer('Напишіть прізвище.', reply_markup=keyboards.Btn_controller.list_btn_req)
        await state_m.StartSearch.search_last_name.set()

    if message.text == Btn_text_menu.ABOUT:
        await message.answer(Texts.SHOW_ABOUT)

    if message.text == Btn_text_menu.SEND_MESSAGE:
        await message.answer(Texts.SHOW_WEB)

    if message.text == Btn_text_menu.INSTRUCTION:
        await message.answer(Texts.INSTRUCTION)




