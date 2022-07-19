from aiogram import Bot, Dispatcher, executor, types

TOKEN = "5596751604:AAE-kA_Mvso9liG6hqmxmL3JxhyjazfqPuY"

bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button = types.KeyboardButton(text="Добре")
keyboard.add(button)


# всі команди починаються з символа " / "


@dp.message_handler(content_types="text")
async def eho(message: types.Message):
    await message.reply(message.text)


@dp.message_handler(text="Добре")
async def nice(message: types.Message):
    await message.reply("Круто")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
