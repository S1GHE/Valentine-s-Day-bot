from main import dp, bot, CONFIG_BOT
from aiogram import types
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command('compliment'))
async def get_compliment(message: types.Message):
    if CONFIG_BOT.user_love == message.from_user.id:
        await message.answer("<b>Привет Арин</b>")