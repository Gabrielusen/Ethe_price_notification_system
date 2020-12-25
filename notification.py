import requests
import time


eth_api_url = 'https://api.coingecko.com/api/v3/coins/ethereum'

answer = requests.get(eth_api_url)
answer_json = answer.json()
x = float(answer_json['market_data']['current_price']['usd'])
print(x)
