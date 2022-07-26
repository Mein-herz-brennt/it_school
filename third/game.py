from aiogram import Bot, Dispatcher, executor, types
import random

TOKEN = "5596751604:AAE-kA_Mvso9liG6hqmxmL3JxhyjazfqPuY"
bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)

tpl = ("👊", "🤚", "✌")

keyb = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton(text="👊")
button2 = types.KeyboardButton(text="🤚")
button3 = types.KeyboardButton(text="✌")
keyb.add(button1, button2, button3)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    print(message.from_user.id)
    await message.answer("Hi", reply_markup=keyb)


@dp.message_handler(text="👊")
async def stone(message: types.Message):
    global tpl
    random_emo = tpl[random.randint(0, 2)]
    await message.reply(random_emo)
    if random_emo == "👊":
        await message.answer("Нічия")
    elif random_emo == "✌":
        await message.answer("you WIN🎉")
    else:
        await message.answer("you LOSE😞")


@dp.message_handler(text="✌")
async def nosh(message: types.Message):
    global tpl
    random_emo = tpl[random.randint(0, 2)]
    await message.reply(random_emo)
    if random_emo == "✌":
        await message.answer("Нічия")
    elif random_emo == "👊":
        await message.answer("you LOSE😞")
    else:
        await message.answer("you WIN🎉")


@dp.message_handler(text="🤚")
async def papir(message: types.Message):
    global tpl
    random_emo = tpl[random.randint(0, 2)]
    await message.reply(random_emo)
    if random_emo == "🤚":
        await message.answer("Нічия")
    elif random_emo == "👊":
        await message.answer("you WIN🎉")
    else:
        await message.answer("you LOSE😞")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
