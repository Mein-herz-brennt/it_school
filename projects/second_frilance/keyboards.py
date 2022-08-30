from aiogram import types

keyboard_start = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_dev = types.KeyboardButton(text="Я хочу взяти замовлення")
button_add = types.KeyboardButton(text="Хочу подати замовлення")
keyboard_start.add(button_add).add(button_dev)