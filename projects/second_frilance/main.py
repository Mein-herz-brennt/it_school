from aiogram import Dispatcher, executor, Bot, types
from config import *
from states import *
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import json
from keyboards import *

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(commands="start", state="*")
async def start(message: types.Message):
    await message.answer(f"Вітаю у frilance-bot!\n"
                         f"Чим бажаєте зайнятись?", reply_markup=keyboard_start)


@dp.message_handler(text="Хочу подати замовлення")
async def get_work(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Введіть опис замовлення!")
    await Frilance.info_abou_deal.set()


@dp.message_handler(state=Frilance.info_abou_deal)
async def deal_info(message: types.Message, state: FSMContext):
    await state.finish()
    with open("frilance.json", "r", encoding="utf-8") as file:
        info = json.load(file)
    info.append({"id_": message.from_user.id,
                 "username": message.from_user.username,
                 "name": message.from_user.full_name,
                 "info": message.text,
                 "time": f"{message.date}---{message.date.time()}"})
    with open("frilance.json", "w", encoding="utf-8") as file:
        json.dump(info, file, indent=3)
    await message.answer("Ваше замовлення успішно записане!", reply_markup=keyboard_start)


@dp.message_handler(text="Я хочу взяти замовлення")
async def get_deals(message: types.Message, state: FSMContext):
    await state.finish()
    with open("frilance.json", "r", encoding="utf-8") as file:
        info = json.load(file)
    for i in info:
        await message.answer(f"Замовник: @{i['username']}\n"
                             f"Інформація про замовлення:\n {i['info']}\n"
                             f"Час замовлення: {i['time']}")
    await message.answer("Зв'яжіться з замовником якщо можете виконати якесь із замовлень", reply_markup=keyboard_start)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
