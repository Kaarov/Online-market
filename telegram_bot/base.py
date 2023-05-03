import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav

TOKEN = '5648483777:AAE0Dg4REveimWtRYl7GMya_FBgmCmNWE48'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, f"Hello {message.from_user.first_name}, Roma Koh", reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
