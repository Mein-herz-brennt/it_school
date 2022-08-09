from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from States_clicker import *

TOKEN = "5596751604:AAE-kA_Mvso9liG6hqmxmL3JxhyjazfqPuY"

bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())

users = {}

keyboard_click = types.ReplyKeyboardMarkup()
button_click1 = types.KeyboardButton(text="Клік")
button_back = types.KeyboardButton(text="Назад")
keyboard_click.add(button_click1).add(button_back)

keyboard_click_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_click = types.KeyboardButton(text="Клік")
button_head_menu = types.KeyboardButton(text="Меню📝")
keyboard_click_menu.add(button_click).add(button_head_menu)

keyboard_upgrade_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_upgrade = types.KeyboardButton(text="Прокачати")
button_back = types.KeyboardButton(text="Назад")
keyboard_upgrade_menu.add(button_upgrade).add(button_back)


@dp.message_handler(commands="start", state="*")
async def start(message: types.Message):
    global users
    users[str(message.from_user.id)] = {"num": 0, "level": 1}
    await message.answer("Ну що, почнемо грати?", reply_markup=keyboard_click_menu)


@dp.message_handler(text="Назад", state="*")
async def back(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Ти потрапив до головного меню кліків", reply_markup=keyboard_click_menu)


@dp.message_handler(text="Клік")
async def click_check(message: types.Message, state: FSMContext):
    global users
    await state.finish()
    users[str(message.from_user.id)]["num"] += 1
    await message.answer("Клак", reply_markup=keyboard_click)
    await User.click.set()


@dp.message_handler(state=User.click)
async def click(message: types.Message, state: FSMContext):
    global users
    await state.finish()
    users[str(message.from_user.id)]["num"] += 1
    await message.answer("Клак")
    await User.click.set()


@dp.message_handler(text="Меню📝")
async def menu(message: types.Message, state: FSMContext):
    global users
    await state.finish()
    await message.answer(f"Ваш рівень: {users[str(message.from_user.id)]['level']}\n"
                         f"Ваша кількість кліків: {users[str(message.from_user.id)]['num']}\n"
                         f"Щоб прокачати рівень потрібно мати {users[str(message.from_user.id)]['level'] * 10}"
                         f" кліків", reply_markup=keyboard_upgrade_menu)
    await User.menu.set()


@dp.message_handler(state=User.menu)
async def upgrade_menu(message: types.Message, state: FSMContext):
    global users
    await state.finish()
    if str(message.text) == "Прокачати":
        if users[str(message.from_user.id)]["num"] >= users[str(message.from_user.id)]["level"] * 10:
            users[str(message.from_user.id)]["num"] -= users[str(message.from_user.id)]["level"] * 10
            users[str(message.from_user.id)]["level"] += 1
            await message.answer(f"Ваш рівень: {users[str(message.from_user.id)]['level']}\n"
                                 f"Ваша кількість кліків: {users[str(message.from_user.id)]['num']}\n"
                                 f"Щоб прокачати рівень потрібно мати {users[str(message.from_user.id)]['level'] * 10}"
                                 f" кліків", reply_markup=keyboard_upgrade_menu)

            await User.menu.set()
        else:
            await message.answer("Щоб прокачати рівень вам не вистачає кліків", reply_markup=keyboard_click)
            await User.click.set()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
