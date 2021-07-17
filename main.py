import requests
import json
from reprint import output
import time
import datetime

def get_info():
	response = requests.get(url= 'https://yobit.net/api/3/ticker/btc_usd').json()
	# json.loads(
	return response

# print('Максимальная цена за сегодня: {} Минимальная цена: {} Средняя цена: {} Цена последней сделки: {} Цена покупки: {} Цена продажи: {}'get_info()['btc_usd'])

with output(initial_len=7, interval=1) as output_lines:
	while True:
		resp = get_info()['btc_usd']
		output_lines[0] = 'Максимальная цена за сегодня: ' + str(resp['high'])
		output_lines[1] = 'Минимальная цена: ' + str(resp['low'])
		output_lines[2] = 'Средняя цена: ' + str(resp['avg'])
		output_lines[3] = 'Цена последней сделки: ' + str(resp['last'])
		output_lines[4] = 'Цена покупки: ' + str(resp['buy'])
		output_lines[5] = 'Цена продажи: ' + str(resp['sell'])

		value = datetime.datetime.fromtimestamp(time.time())
		output_lines[6] = value.strftime('%H:%M:%S')

		time.sleep(1)