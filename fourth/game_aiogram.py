from aiogram import Bot, Dispatcher, executor, types
import random

TOKEN = "5596751604:AAE-kA_Mvso9liG6hqmxmL3JxhyjazfqPuY"
bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)

lst = []
gamers = []
conected = []

tpl = ("👊", "🤚", "✌")

keyb = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton(text="👊")
button2 = types.KeyboardButton(text="🤚")
button3 = types.KeyboardButton(text="✌")
button5 = types.KeyboardButton(text="Вийти")
keyb.add(button1, button2, button3).add(button5)

keyb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button4 = types.KeyboardButton(text="Знайти гравця")
keyb1.add(button4)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    global lst
    lst.append(message.from_user.id)
    await message.answer("Hi", reply_markup=keyb1)


@dp.message_handler(text="Знайти гравця")
async def find(message: types.Message):
    global gamers, conected
    gamers.append(message.from_user.id)
    rand_gamer = random.randint(0, len(gamers)-1)
    if message.from_user.id != gamers[rand_gamer]:
        conected.append((message.from_user.id, gamers[rand_gamer]))
        await message.answer("Вас з'єднано", reply_markup=keyb)
    else:
        await message.answer("Натисніть ще раз", reply_markup=keyb1)


@dp.message_handler(text="Вийти")
async def out(message: types.Message):
    global conected
    for i in conected:
        if i[0] == message.from_user.id:
            game = i[1]
            conected.remove(i)
            await message.answer("Ви вийшли з Гри", reply_markup=keyb1)
            await bot.send_message(game, "Ваш друг покинув Гру", reply_markup=keyb1)
        elif i[1] == message.from_user.id:
            game = i[0]
            conected.remove(i)
            await message.answer("Ви вийшли з Гри", reply_markup=keyb1)
            await bot.send_message(game, "Ваш друг покинув Гру", reply_markup=keyb1)


@dp.message_handler(text="👊")
async def stone(message: types.Message):
    global tpl, conected

    for i in conected:
        if i[0] == message.from_user.id:
            game = i[1]
            await bot.send_message(game, message.text)
        elif i[1] == message.from_user.id:
            game = i[0]
            await bot.send_message(game, message.text)

    # await message.reply(random_emo)
    # if random_emo == "👊":
    #     await message.answer("Нічия")
    # elif random_emo == "✌":
    #     await message.answer("you WIN🎉")
    # else:
    #     await message.answer("you LOSE😞")


@dp.message_handler(text="✌")
async def nosh(message: types.Message):
    global tpl, conected

    for i in conected:
        if i[0] == message.from_user.id:
            game = i[1]
            await bot.send_message(game, message.text)
        elif i[1] == message.from_user.id:
            game = i[0]
            await bot.send_message(game, message.text)

    # if random_emo == "✌":
    #     await message.answer("Нічия")
    # elif random_emo == "👊":
    #     await message.answer("you LOSE😞")
    # else:
    #     await message.answer("you WIN🎉")


@dp.message_handler(text="🤚")
async def papir(message: types.Message):
    global tpl, conected

    for i in conected:
        if i[0] == message.from_user.id:
            game = i[1]
            await bot.send_message(game, message.text)
        elif i[1] == message.from_user.id:
            game = i[0]
            await bot.send_message(game, message.text)
    # await message.reply(random_emo)
    # if random_emo == "🤚":
    #     await message.answer("Нічия")
    # elif random_emo == "👊":
    #     await message.answer("you WIN🎉")
    # else:
    #     await message.answer("you LOSE😞")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
