from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import json
from States_clicker import *
# import aioschedule as schedule
import datetime

TOKEN = "5596751604:AAE-kA_Mvso9liG6hqmxmL3JxhyjazfqPuY"

bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())

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


# def msg(chat_id):


def reader(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def adder(filename: str, data: dict) -> None:
    info = reader(filename)
    info.append(data)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(info, file, indent=3, ensure_ascii=False)


def adding(filename: str, data: list) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=3, ensure_ascii=False)


def checker(id_: int) -> bool:
    lst_id = [i["user_id"] for i in reader("info.json")]
    if id_ in lst_id:
        return True
    else:
        return False


@dp.message_handler(commands="start")
async def start(message: types.Message):
    msg_id = message.message_id
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    is_bot = message.from_user.is_bot
    if checker(user_id):
        await message.answer("Ну що, почнемо грати?", reply_markup=keyboard_click_menu)
    else:
        adder("info.json", {"user_id": user_id,
                            "name": first_name,
                            "last_name": last_name,
                            "is_bot": is_bot,
                            "msg_id": msg_id,
                            "num": 0,
                            "level": 1})
        await message.answer("Ну що, почнемо грати?", reply_markup=keyboard_click_menu)


@dp.message_handler(text="Назад", state="*")
async def back(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Ти потрапив до головного меню кліків", reply_markup=keyboard_click_menu)


# @dp.message_handler(text="Почати")
# async def strt(message: types.Message):
#     time = datetime.datetime.now().min
#     data = reader("info.json")
#     for i in data:
#         if i["user_id"] == message.from_user.id:
#             i["time"] = time
#     adding("info.json", data)
#     await message.answer("Стартуй!", reply_markup=keyboard_click)


@dp.message_handler(text="Клік")
async def click_check(message: types.Message, state: FSMContext):
    global users
    await state.finish()
    time_now = datetime.datetime.now().min
    data = reader("info.json")
    for i in data:
        if i["user_id"] == message.from_user.id:
            i["num"] += 1
    adding("info.json", data)

    await message.answer("Клак", reply_markup=keyboard_click)
    await User.click.set()


@dp.message_handler(state=User.click)
async def click(message: types.Message, state: FSMContext):
    global users
    await state.finish()
    data = reader("info.json")
    for i in data:
        if i["user_id"] == message.from_user.id:
            i["num"] += 1
    adding("info.json", data)
    await message.answer("Клак")
    await User.click.set()


@dp.message_handler(text="Меню📝")
async def menu(message: types.Message, state: FSMContext):
    global users
    await state.finish()
    data = reader("info.json")
    for i in data:
        if i["user_id"] == message.from_user.id:
            await message.answer(f"Ваш рівень: {i['level']}\n"
                                 f"Ваша кількість кліків: {i['num']}\n"
                                 f"Щоб прокачати рівень потрібно мати {i['level'] * 10}"
                                 f" кліків", reply_markup=keyboard_upgrade_menu)
    await User.menu.set()


@dp.message_handler(state=User.menu)
async def upgrade_menu(message: types.Message, state: FSMContext):
    global users
    await state.finish()
    if str(message.text) == "Прокачати":
        data = reader("info.json")
        for i in data:
            if i["user_id"] == message.from_user.id:
                if i["num"] >= i["level"] * 10:
                    i["num"] -= i["level"] * 10
                    i["level"] += 1
                    adding("info.json", data)
                    await message.answer(f"Ваш рівень: {i['level']}\n"
                                         f"Ваша кількість кліків: {i['num']}\n"
                                         f"Щоб прокачати рівень потрібно мати {i['level'] * 10}"
                                         f" кліків", reply_markup=keyboard_upgrade_menu)

                    await User.menu.set()
                else:
                    await message.answer("Щоб прокачати рівень вам не вистачає кліків", reply_markup=keyboard_click)
                    await User.click.set()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
