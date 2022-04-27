from bs4 import BeautifulSoup

import time 
import lxml 
import json


class Parser:
	def __init__(self, browzer):
		self.browzer = browzer


	def main(self):
		self.get_data('https://www.ukr.net/ua/news/technologies.html')
		self.parser()
		self.browzer.quit()


	def get_data(self, url: str):
		self.browzer.get(url)
		time.sleep(3)

		with open('data\\index.html', 'w', encoding='utf-8') as f:
			f.write(self.browzer.page_source)

	def parser(self):
		with open('data\\index.html', encoding='utf-8') as f:
			src = f.read()

		soup = BeautifulSoup(src, 'lxml')
		items = soup.find_all('section', class_='im')
		news_data = {}

		for item in items:
			news_time = item.find('time').text.strip()
			news_name = item.find('a', class_='im-tl_a').text.strip()
			news_url = item.find('a', class_='im-tl_a').get('href')
			news_id = item.find('a', class_='im-tl_a').get('data-count')
			
			if isinstance(news_id, str):
				news_id = news_id.replace(',', ':')
			else:
				continue

			news_data[news_id] = {
				'time': news_time,
				'name': news_name,
				'url': news_url,
			}

		with open('data\\json_data\\news_data.json', 'w', encoding='utf-8') as f:
			json.dump(news_data, f, indent=4, ensure_ascii=False)




			


