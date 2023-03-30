import re
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
from MS import state_m
from config.loader import anti_flood, dp, bot, api_storage_module
from keyboard import keyboards
from modules.models.schema import SearchSchema
from modules.models.text_schema import TextModul


@dp.message_handler(state=state_m.StartSearch.search_last_name)
@dp.throttled(anti_flood, rate=1)
async def search_last_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text

    await message.answer('Введіть ім\'я для пошуку', reply_markup=keyboards.Btn_controller.list_btn_req)
    await state_m.StartSearch.search_first_name.set()


@dp.message_handler(state=state_m.StartSearch.search_first_name)
@dp.throttled(anti_flood, rate=1)
async def search_first_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text

    await message.answer('Введіть по-батькові', reply_markup=keyboards.Btn_controller.list_btn)
    await state_m.StartSearch.search_middle_name.set()


@dp.message_handler(state=state_m.StartSearch.search_middle_name)
@dp.throttled(anti_flood, rate=1)
async def search_middle_name(message: types.Message, state: FSMContext):
    if message.text == keyboards.Btn_text_controller_inf.SKIP:
        await message.answer('Ведіть дату народження людини в форматі (дд.мм.гггг)',
                             reply_markup=keyboards.Btn_controller.list_btn)
        await state_m.StartSearch.search_birthday.set()
        return

    async with state.proxy() as data:
        data['middle_name'] = message.text

    await message.answer('Ведіть дату народження людини в форматі (дд.мм.гггг)',
                         reply_markup=keyboards.Btn_controller.list_btn)
    await state_m.StartSearch.search_birthday.set()


@dp.message_handler(state=state_m.StartSearch.search_birthday)
@dp.throttled(anti_flood, rate=1)
async def search_birthday(message: types.Message, state: FSMContext):
    if message.text == keyboards.Btn_text_controller_inf.SKIP:
        async with state.proxy() as data:
            search = SearchSchema(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                middle_name='' if data.get('middle_name') is None else data.get('middle_name'),
            )
        response = await api_storage_module.get_person(search)
        await bot.send_message(message.from_user.id, "Йде пошук ...",
                               reply_markup=keyboards.Btn_main_menu.list_btn)
        if response:
            for person in response:
                await bot.send_message(message.from_user.id, TextModul.show_search_person(person),
                                       reply_markup=keyboards.Btn_main_menu.list_btn,
                                       parse_mode=ParseMode.HTML)
        else:
            await bot.send_message(message.from_user.id, "За вашим запитом нічого не знайдено",
                                   reply_markup=keyboards.Btn_main_menu.list_btn)
        await state.finish()
        return

    if len(re.findall(r'[\d*]{1,2}\.[\d*]{1,2}\.[\d*]{1,4}', message.text)) > 0:
        async with state.proxy() as data:
            data['birthday'] = message.text
            search = SearchSchema(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                middle_name='' if data.get('middle_name') is None else data.get('middle_name'),
                birthday=data.get('birthday'),
            )
        response = await api_storage_module.get_person(search)
        if response:
            for person in response:
                await bot.send_message(message.from_user.id, TextModul.show_search_person(person),
                                       reply_markup=keyboards.Btn_main_menu.list_btn,
                                       parse_mode=ParseMode.HTML)
        else:
            await bot.send_message(message.from_user.id, "За вашим запитом нічого не знайдено",
                                   reply_markup=keyboards.Btn_main_menu.list_btn)
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, f"Неверно был введен формат даты, повторите ещё раз.",
                               reply_markup=keyboards.Btn_controller.list_btn)
        await state_m.StartSearch.search_birthday.set()
        return


