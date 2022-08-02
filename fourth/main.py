from aiogram import Bot, Dispatcher, executor, types

TOKEN = "5596751604:AAE-kA_Mvso9liG6hqmxmL3JxhyjazfqPuY"
bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)

lst = []
lst_msg = []
admin = 789402487


@dp.message_handler(commands="start")
async def start(message: types.Message):
    global lst
    if message.from_user.id not in lst:
        lst.append(message.from_user.id)
        print(lst)
    await message.answer("Hi")


inline_keyb = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
button1 = types.KeyboardButton(text="Так")
button2 = types.KeyboardButton(text="Ні")
inline_keyb.add(button1, button2)


@dp.message_handler(commands="admin")
async def admin(message: types.Message):
    id = message.from_user.id
    if "789402487" == str(id):
        await message.answer("Привіт адмін!")


@dp.message_handler(text="Так")
async def yeas(message: types.Message):
    global lst, lst_msg
    id = message.from_user.id
    if "789402487" == str(id):
        for i in lst:
            await bot.send_message(i, lst_msg[-1])
            lst_msg.pop(-1)


@dp.message_handler(text="Ні")
async def no(message: types.Message):
    global lst, lst_msg
    id = message.from_user.id
    if "789402487" == str(id):
        lst_msg.pop(-1)


@dp.message_handler(content_types="text")
async def text(message: types.Message):
    global lst, lst_msg
    text_ = message.text
    id_ = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    is_bot = message.from_user.is_bot
    message_for_you = f"Повідомлення від: {first_name} {last_name},\n" \
                      f"id: {id_} \n" \
                      f"Повідомлення: {text_}\n" \
                      f"Це бот: {is_bot}\n"
    lst_msg.append(message_for_you)
    print(message_for_you)
    await bot.send_message("789402487", message_for_you, reply_markup=inline_keyb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
