import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

print("provide a coin name")

coin = input()


url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd&x_cg_api_key={api_key}"


response = requests.get(url)


data = response.json()

print (data[coin])


