from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import json
import datetime
from states import *

TOKEN = "5596751604:AAE-kA_Mvso9liG6hqmxmL3JxhyjazfqPuY"

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())

keyb_nums = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton(text="1")
button2 = types.KeyboardButton(text="2")
button3 = types.KeyboardButton(text="3")
button4 = types.KeyboardButton(text="4")
button5 = types.KeyboardButton(text="5")
button6 = types.KeyboardButton(text="6")
button7 = types.KeyboardButton(text="7")
button8 = types.KeyboardButton(text="8")
button9 = types.KeyboardButton(text="9")
button0 = types.KeyboardButton(text="0")
keyb_nums.add(button7, button8, button9).add(button4, button5, button6).add(button1, button2, button3).add(button0)

# [7, 8, 9,+]
# [4, 5, 6,-]
# [1, 2, 3,*]
# [0, ., =,/]

keyb_dii = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_mnosh = types.KeyboardButton(text="*")
button_dil = types.KeyboardButton(text="/")
button_dod = types.KeyboardButton(text="+")
button_vid = types.KeyboardButton(text="-")
button_stepin = types.KeyboardButton(text="^")
keyb_dii.add(button_mnosh, button_dil, button_stepin).add(button_dod, button_vid)


@dp.message_handler(commands="start", state='*')
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    with open("calc.json", "r", encoding="utf-8") as file:
        info = json.load(file)
    info.append({"id_": message.from_user.id,
                 "num1": 0,
                 "dii": "",
                 "num2": 0})
    with open("calc.json", "w", encoding="utf-8") as file:
        json.dump(info, file, indent=3)
    await message.answer("Привіт користувач!", reply_markup=keyb_nums)
    await Calculate.num1.set()


@dp.message_handler(state=Calculate.num1)
async def firs_num(message: types.Message, state: FSMContext):
    await state.finish()
    with open("calc.json", "r", encoding="utf-8") as file:
        info = json.load(file)
    for i in range(len(info)):
        if info[i]["id_"] == message.from_user.id:
            info[i]["num1"] = float(message.text)
    with open("calc.json", "w", encoding="utf-8") as file:
        json.dump(info, file, indent=3)
    await message.answer("Введіть дію!", reply_markup=keyb_dii)
    await Calculate.dii.set()


@dp.message_handler(state=Calculate.dii)
async def dii(message: types.Message, state: FSMContext):
    await state.finish()
    with open("calc.json", "r", encoding="utf-8") as file:
        info = json.load(file)
    for i in range(len(info)):
        if info[i]["id_"] == message.from_user.id:
            info[i]["dii"] = str(message.text)
    with open("calc.json", "w", encoding="utf-8") as file:
        json.dump(info, file, indent=3)
    await message.answer("Введіть друге число", reply_markup=keyb_nums)
    await Calculate.num2.set()


@dp.message_handler(state=Calculate.num2)
async def second_num(message: types.Message, state: FSMContext):
    await state.finish()
    text = ""
    with open("calc.json", "r", encoding="utf-8") as file:
        info = json.load(file)
    for i in range(len(info)):
        if info[i]["id_"] == message.from_user.id:
            info[i]["num2"] = float(message.text)
    with open("calc.json", "w", encoding="utf-8") as file:
        json.dump(info, file, indent=3)
    with open("calc.json", "r", encoding="utf-8") as file:
        res = json.load(file)
    for i in range(len(res)):
        if info[i]["id_"] == message.from_user.id:
            if info[i]["dii"] == "*":
                text = str(info[i]["num1"] * info[i]["num2"])
            elif info[i]["dii"] == "/":
                if info[i]["num2"] == 0:
                    await message.answer("Ділити на нуль не можна, виберіть якесь інше число", reply_markup=keyb_nums)
                    await Calculate.num2.set()
                else:
                    text = str(info[i]["num1"] / info[i]["num2"])
            elif info[i]["dii"] == "^":
                text = str(info[i]["num1"] ** info[i]["num2"])
            elif info[i]["dii"] == "+":
                text = str(info[i]["num1"] + info[i]["num2"])
            elif info[i]["dii"] == "-":
                text = str(info[i]["num1"] - info[i]["num2"])
            else:
                await message.answer("Ви ввели дію некоректно", reply_markup=keyb_dii)
                await Calculate.dii.set()
    await message.answer(f"Ваш результат {text}", reply_markup=keyb_nums)
    await Calculate.num1.set()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
