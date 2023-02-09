from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Добавить комплимент', callback_data="add_compliment")
        ]
    ]
)
