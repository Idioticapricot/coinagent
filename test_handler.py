#!/usr/bin/env python3
import requests
from dotenv import load_dotenv

load_dotenv()

COINGECKO_URL = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?vs_currencies=usd&ids={coin}"
)

def handle_task(job_input: str) -> str:
    """
    Fetch crypto price from CoinGecko based on user input.
    job_input: e.g., "bitcoin" or "ethereum"
    """
    coin = job_input.strip().lower()
    if not coin:
        return "Invalid input. Provide a coin name like 'bitcoin'."

    url = COINGECKO_URL.format(coin=coin)

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return f"API request failed: {str(e)}"

    if coin not in data:
        return f"Coin '{coin}' not found."

    usd_price = data[coin]["usd"]
    return f"{coin.capitalize()} price: ${usd_price}"

if __name__ == "__main__":
    # Test the handler directly
    test_inputs = ["bitcoin", "ethereum", "cardano", "invalid_coin"]
    
    for test_input in test_inputs:
        print(f"Testing: {test_input}")
        result = handle_task(test_input)
        print(f"Result: {result}")
        print("-" * 50)