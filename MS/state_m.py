from aiogram.dispatcher.filters.state import StatesGroup, State


class StartSearch(StatesGroup):
    search_last_name = State()
    search_first_name = State()
    search_middle_name = State()
    search_birthday = State()




