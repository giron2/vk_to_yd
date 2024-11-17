import requests
import json
import yadisk
from datetime import datetime
from tqdm import tqdm





class vk():
	def __init__(self, i, yd_api):
		self.i = i
		self.yd_api = yd_api

	def create_folder(self):
		api_yandex = self.yd_api
		headers = {"Authorization": api_yandex}
		vk_id = self.i
		fold = requests.put(url=f'https://cloud-api.yandex.net/v1/disk/resources?path=/{vk_id}', headers=headers)

	def upload_ile(self):
		access_token = ()
		with open("api_vk.txt") as file:
			api = file.read()
			access_token = api
		api_yandex = self.yd_api
		vk_id = self.i
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
		#yd.mkdir(vk_id)
		info_file = []
		for item in tqdm(items):
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
					elif path.status_code == 200 :
						date = datetime.fromtimestamp(item['date'])
						p = yd.upload_url(f'{size['url']}', f'/{vk_id}/{date}-'
						                                    f'{item['likes']['count']}.jpg')



		with open("info_file.json", "w") as f:
		    f.write(str(info_file))




d = vk('651***', 'y0_A****')
d.create_folder()
d.upload_ile()
