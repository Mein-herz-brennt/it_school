from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import json
import datetime

TOKEN = "5596751604:AAE-kA_Mvso9liG6hqmxmL3JxhyjazfqPuY"

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Привіт користувач!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
