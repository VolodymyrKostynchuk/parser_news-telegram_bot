from aiogram import Bot, Dispatcher, types

import os 


bot = Bot(token=os.getenv('TOKEN'), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

