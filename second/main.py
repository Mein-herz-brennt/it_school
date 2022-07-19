from aiogram import Bot, Dispatcher, executor, types

TOKEN = "5596751604:AAE-kA_Mvso9liG6hqmxmL3JxhyjazfqPuY"

bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot)

# inline keyboard
keyb = types.InlineKeyboardMarkup()
b1 = types.InlineKeyboardButton(text="Привіт",
                                url="https://telegra.ph/Gajd-z-rozrobki-telegam-bot%D1%96v-na-python-07-15")
keyb.add(b1)

# reply keyboard
keyb2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
b3 = types.KeyboardButton(text="Привіт")
b4 = types.KeyboardButton(text="Бувай")
keyb2.add(b3, b4)

keyb1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
b = types.KeyboardButton(text="give contact", request_contact=True)
keyb1.add(b)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    # await bot.send_message("789402487", f"Користувач:  @{message.from_user.username} натиснув старт")
    await message.reply("Вітаємо у нашому боті!", reply_markup=keyb)
    await message.answer("Ви крутий", reply_markup=keyb1)


@dp.callback_query_handler(text="1")
async def hi(call: types.CallbackQuery):
    await call.answer("Бувай")


@dp.callback_query_handler(text="2")
async def by(call: types.CallbackQuery):
    await call.message.answer("Привіт")


@dp.message_handler(text="Привіт")
async def hi1(message: types.Message):
    await message.answer("Бувай!")



@dp.message_handler(text="Бувай")
async def by1(message: types.Message):
    await message.answer("Привіт")


@dp.message_handler(content_types="contact")
async def loc(message: types.Message):
    print(message.contact.values)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
