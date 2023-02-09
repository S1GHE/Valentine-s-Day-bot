from aiogram import types
from aiogram.dispatcher.filters import Command

from main import dp, bot, CONFIG_BOT
from KeyBoard import admin_menu


async def initial_performance(dp) -> None:
    await bot.send_message(chat_id=CONFIG_BOT.admin_id, text="BOT IS START")
    await bot.set_my_commands(
        [
            types.BotCommand('start', 'Обновления бота'),
            types.BotCommand('compliment', 'Получить комплимент :)'),
            types.BotCommand('settings', 'Настройка бота'),
            types.BotCommand('admin', 'Админ панель')
        ]
    )


@dp.message_handler(Command('admin'))
async def start_command_admin(message: types.Message):
    if CONFIG_BOT.admin_id == message.from_user.id:
        await message.answer('<b>Админ Панель</b>',
                             parse_mode=types.ParseMode.HTML, reply_markup=admin_menu)
    else:
        await message.answer('<b>ЗАЧЕМ?</b>\n'
                             'Ты не Ефим, так что сюда тебя не пущу :3',
                             parse_mode=types.ParseMode.HTML, )
