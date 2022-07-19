from aiogram import Bot, Dispatcher, executor, types

TOKEN = "5596751604:AAE-kA_Mvso9liG6hqmxmL3JxhyjazfqPuY"

bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot)

id = []


@dp.message_handler(commands="start")
async def start(message: types.Message):
    # await bot.send_message("789402487", f"Користувач:  @{message.from_user.username} натиснув старт")
    await message.reply("Вітаємо у нашому боті!")
    await message.answer("Напишіть мені щось")


@dp.message_handler(commands="send")
async def send(message: types.Message):
    global id
    for i in id:
        await bot.send_message(i, "Вітаємо на уроці!")



@dp.message_handler(content_types="text")
async def code(message: types.Message):
    global id
    id.append(message.from_user.id)
    string = message.text
    k = ""
    for i in string:
        k += i + " - "
    await message.answer(k)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
