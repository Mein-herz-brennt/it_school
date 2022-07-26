from aiogram import Bot, Dispatcher, executor, types
from random import randint

TOKEN = "5596751604:AAE-kA_Mvso9liG6hqmxmL3JxhyjazfqPuY"
bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)

lst = []


@dp.message_handler(commands="start")
async def start(message: types.Message):
    global lst
    if message.from_user.id not in lst:
        lst.append(message.from_user.id)
        print(lst)
    await message.answer("Hi")


@dp.message_handler(content_types="text")
async def msg(msg: types.Message):
    global lst
    print("*" * 30)
    print(msg.from_user.first_name + " _-*-_ " + msg.text)
    print("*" * 30)
    for i in lst:
        if i != msg.from_user.id:
            await bot.send_message(i, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
