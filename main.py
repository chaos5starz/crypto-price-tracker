import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

print("provide a coin name")
coin = input()

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",   
    "ids": coin             
}

headers = {"x-cg-demo-api-key": api_key}

response = requests.get(url, headers=headers , params=params)


data = response.json()


for coin_dict in data:
    print(f"the current price of {coin} is {coin_dict['current_price']} last updated in {coin_dict["last_updated"]}")






