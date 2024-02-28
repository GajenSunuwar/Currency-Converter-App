# currency_api.py
#for handling API requests:

import requests

API_KEY = 'fca_live_vNVzhNCSjH1XrW0MunExM6ghMu8n2Sx1QsvTx0fm'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY", "GBP"]

def get_exchange_data(base):
    if base is None:
        return None

    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("data", None)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"Error fetching data: {e}")
    return None