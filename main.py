import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

print("provide a coin name, type exit to exit")

while True :

    coin = input().lower()

    if coin == "exit" :
        print("bye")
        break

    url = "https://api.coingecko.com/api/v3/coins/markets" 
    params = { "vs_currency": "usd", "ids": coin } 
    headers = {"x-cg-demo-api-key": api_key} 


    try:
        response = requests.get(url, headers = headers , params=params , timeout=5)
        response.raise_for_status()  # catch HTTP errors
        data = response.json()
    except requests.exceptions.Timeout:
        print("Bro your internet is sleeping. Try again.")
        continue
    except Exception:
        print("API messed up. Try later.")
        continue


    if data != [] :
        print(f"the current price of {coin} is ${round(data[0]['current_price'], 2)} and it was last updated on {data[0]['last_updated']}")
    else :
        print("invalid coin")
        continue

    







