import requests
from bs4 import BeautifulSoup
from reprint import output
import time
import datetime

header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

with output(initial_len=2, interval=1) as output_lines:
	while True:
		content = requests.get(url= 'https://ru.investing.com/crypto/bitcoin', headers= header).content

		soup = BeautifulSoup(content, 'html.parser')
		change = soup.findAll(id= 'last_last')[0].text

		output_lines[0] = change

		value = datetime.datetime.fromtimestamp(time.time())
		output_lines[1] = value.strftime('%H:%M:%S')
