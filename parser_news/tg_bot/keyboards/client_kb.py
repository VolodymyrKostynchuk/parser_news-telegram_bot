from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


b1 = KeyboardButton('/all_news')
b2 = KeyboardButton('/last_five_news')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1, b2)