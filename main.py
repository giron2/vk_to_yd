import requests
import json
import yadisk
from datetime import datetime






class vk():
	def upload_ile(i):
		access_token = '6529184065291840652918402d660851486652965291840023d294536869b369cdf463e'
		api_yandex = ()
		with open("api_yandex.txt") as file:
			api = file.read()
			api_yandex = api
		vk_id = i
		param_vk = {'access_token': access_token,
			         'owner_id': vk_id,
			         'album_id': 'profile',
			         'count': 5,
			         'extended': '1',
			         'v': 5.199}
		method_vk = 'photos.get'
		headers = {
			"Authorization": api_yandex
			}
		respons_vk = requests.get(url=f'https://api.vk.ru/method/{method_vk}', params=param_vk)
		yd = yadisk.YaDisk(token=api_yandex)
		all_respons = respons_vk.json()['response']
		items = all_respons['items']
		yd.mkdir(vk_id)
		info_file = []
		for item in items:
			for size in item["sizes"]:
				info = dict()
				if size['type'] == 'z':
					info["file_name"] = f'{item['likes']['count']}.jpg'
					info["size"] = size['type']
					info_file.append(info)
					path = requests.get(url=f'https://cloud-api.yandex.net/v1/disk/resources?path=/{vk_id}/{item['likes']['count']}.jpg',
					                    headers=headers)

					if path.status_code != 200:


						p = yd.upload_url(f'{size['url']}', f'/{vk_id}/{item['likes']['count']}.jpg')
						if p.get_status() == 'success':
							print(f'Файл {item['likes']['count']}.jpg  успешно загружен на ЯндексДиск')
					elif path.status_code == 200 :
						date = datetime.fromtimestamp(item['date'])
						p = yd.upload_url(f'{size['url']}', f'/{vk_id}/{date}-'
						                                    f'{item['likes']['count']}.jpg')
						if p.get_status() == 'success':
							print(f'Файл {date}-{item['likes']['count']}.jpg  успешно загружен на ЯндексДиск')


		with open("info_file.json", "w") as f:
		    f.write(str(info_file))

d = vk
d.upload_ile('618713577')
