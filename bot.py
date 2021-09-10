from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from config import TOKEN
import keyboards as kb


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(state='*',commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!!! Для начла выбери что ты хочешь ..... ", reply_markup=kb.menu_kb)


@dp.message_handler(lambda message: message.text == 'Категории🧢👚👖🥾')
async def process_start_command(message: types.Message):
    await message.reply("Выбери категорию действие ..... ", reply_markup=kb.сategories_kb)


@dp.message_handler(lambda message: message.text == 'В главное меню')
async def process_start_command(message: types.Message):
    await message.reply("Выбери категорию товара ..... ", reply_markup=kb.menu_kb)

@dp.message_handler(lambda message: message.text == 'Обувь🥾')
async def process_start_command(message: types.Message):
    await message.reply(".", reply_markup=kb.product_menu_kb)
    await message.answer("Товар 1")
    await message.answer("Товар 2")
    await message.answer("Товар 3")
    await message.answer("Товар 4")




@dp.message_handler(commands=['hi2'])
async def process_hi2_command(message: types.Message):
    await message.reply("Второе - прячем клавиатуру после одного нажатия", reply_markup=kb.greet_kb2)



@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.text== 'Привет':
        await bot.send_message(msg.from_user.id, 'Салам')
    else:
        await bot.send_message(msg.from_user.id, msg.text)

# bot.py



if __name__ == '__main__':
    executor.start_polling(dp)
