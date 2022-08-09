from aiogram.dispatcher.filters.state import StatesGroup, State


class User(StatesGroup):
    click = State()
    menu = State()
    upgrade = State()
    clicked = State()