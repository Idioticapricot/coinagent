import os
import requests
from dotenv import load_dotenv
from orca_agent_sdk import AgentConfig, AgentServer

# Load environment variables
load_dotenv()

COINGECKO_URL = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?vs_currencies=usd&ids={coin}&x_cg_demo_api_key=CG-AfBLAzXCPgXMdkBytWZxRVy1"
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
    config = AgentConfig(
        agent_id="5bbf48cf-62a2-4ab3-bd96",
        receiver_address="PYPRYGBB4QLQHJIMUCPKMEXIY5ILOTTJVORI2OJJUDUIYMBDFUGP343L3M",
        price_microalgos=1_000_000,
    )

    AgentServer(config=config, handler=handle_task).run()