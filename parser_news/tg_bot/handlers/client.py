from aiogram import types, Dispatcher
from aiogram.utils.markdown import hbold, hlink
from keyboards import kb_client

import json 


async def start(message: types.Message):
		await message.answer('hello)', reply_markup=kb_client)


async def all_news(message: types.Message):
	with open('D:\\PycharmProjects\\pythonProject\\pythonPJ\\bs4\\parser_news\\parser\\data\\json_data\\news_data.json', encoding='utf-8') as f:
		news_dict = json.load(f)

	for k, v in sorted(news_dict.items())[-15:]:
		news =  f"{hbold(v['time'])}\n" \
				f"{hlink(v['name'], v['url'])}"

		await message.answer(news)


async def last_five_news(message: types.Message):
	with open('D:\\PycharmProjects\\pythonProject\\pythonPJ\\bs4\\parser_news\\parser\\data\\json_data\\news_data.json', encoding='utf-8') as f:
		news_dict = json.load(f)

	for k, v in sorted(news_dict.items())[-5:]:
		news =  f"{hbold(v['time'])}\n" \
				f"{hlink(v['name'], v['url'])}"

		await message.answer(news)


def register_handler_client(dp: Dispatcher):
	dp.register_message_handler(start, commands=['start', 'help'])
	dp.register_message_handler(all_news, commands=['all_news'])
	dp.register_message_handler(last_five_news, commands=['last_five_news'])

