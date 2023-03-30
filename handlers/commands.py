from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode

from config.loader import dp, api_storage_module, anti_flood
from keyboard import keyboards
from modules.models.text_enum import Texts


@dp.message_handler(state='*', commands=['start'])
@dp.throttled(anti_flood, rate=1)
async def command_start(message: types.Message, state: FSMContext):
    await message.answer(
        Texts.SHOW_START.format(
            username=message.from_user.first_name
        ),
        reply_markup=keyboards.Btn_main_menu.list_btn,
        parse_mode=ParseMode.HTML
    )
    await state.finish()


@dp.message_handler(text=keyboards.Btn_text_menu.MENU.value, state='*')
async def command_menu(message: types.Message, state: FSMContext):
    await message.answer('Меню', reply_markup=keyboards.Btn_main_menu.list_btn)
    await state.finish()

    