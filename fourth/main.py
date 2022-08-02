from aiogram import Bot, Dispatcher, executor, types

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
async def text(message: types.Message):
    global lst
    text_ = message.text
    id_ = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    is_bot = message.from_user.is_bot
    message_for_you = f"Повідомлення від: {first_name} {last_name},\n" \
                      f"id: {id_} \n" \
                      f"Повідомлення: {text_}\n" \
                      f"Це бот: {is_bot}\n"
    print(message_for_you)
    for i in lst:
        if i != message.from_user.id:
            await bot.send_message(i, message_for_you)


# @dp.message_handler(command="")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
