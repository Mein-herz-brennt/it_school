from aiogram.dispatcher.filters.state import StatesGroup, State


class World(StatesGroup):
    first = State()
    second = State()
    third = State()
