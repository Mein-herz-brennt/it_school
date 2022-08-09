from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from States import *

TOKEN = "5596751604:AAE-kA_Mvso9liG6hqmxmL3JxhyjazfqPuY"

bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())

id_ = []

keyb = types.InlineKeyboardMarkup()
button_yeas = types.InlineKeyboardButton(text="Так", callback_data="y")
button_no = types.InlineKeyboardButton(text="Ні", callback_data="n")
keyb.add(button_yeas, button_no)


@dp.message_handler(commands="start", state="*")
async def start(message: types.Message):
    global id_
    id_.append(message.from_user.id)
    await message.answer("Привіт, не хочеш пройти тестування?", reply_markup=keyb)


@dp.callback_query_handler(text="y")
async def yeas(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer("Добрий день як в вас справи?")
    await World.first.set()


@dp.callback_query_handler(text="n")
async def no(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer("Ну якщо захочеш то тицяй по кнопках", reply_markup=keyb)


@dp.message_handler(state=World.first)
async def first(message: types.Message, state: FSMContext):
    await state.finish()
    print(str(message.from_user.id) + " -- -- " + str(message.text))
    await message.answer("а кто ти такой?")
    await World.second.set()


@dp.message_handler(state=World.second)
async def second(message: types.Message, state: FSMContext):
    await state.finish()
    print(str(message.from_user.id) + " -- -- " + str(message.text))
    await message.answer("Як в тебе настрій ?")
    await World.third.set()


@dp.message_handler(state=World.third)
async def second(message: types.Message, state: FSMContext):
    await state.finish()
    print(str(message.from_user.id) + " -- -- " + str(message.text))
    await message.answer("Дякую за пройдене опитування , не бажаєте пройти ще раз?", reply_markup=keyb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
