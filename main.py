import logging

from aiogram import Dispatcher, Bot, executor
from configuration import Config


CONFIG_BOT = Config()
bot = Bot(CONFIG_BOT.bot_token)
dp = Dispatcher(bot)


if __name__ == '__main__':
    logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,
                        datefmt="%H:%M:%S")

    from handlers.admin_panel import dp, initial_performance

    executor.start_polling(dp, on_startup=initial_performance)