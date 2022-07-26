from aiogram import Bot, Dispatcher, executor, types

TOKEN = "5596751604:AAE-kA_Mvso9liG6hqmxmL3JxhyjazfqPuY"
bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)

keyb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button1 = types.KeyboardButton(text="😎")
button2 = types.KeyboardButton(text="🥺")
button3 = types.KeyboardButton(text="👍")
keyb.add(button1, button2, button3)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Hi", reply_markup=keyb)


@dp.message_handler(text="🙃")
async def smile(message: types.Message):
    await message.answer("Чого сумний?")


@dp.message_handler(text="😎")
async def smile1(message: types.Message):
    await message.answer("Ого який крутий!")


@dp.message_handler(text="👍")
async def smile2(message: types.Message):
    await message.answer("Круто!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
