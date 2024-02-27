# This will be the main Python script.
# Here the code I write will interact with the API.
# Making use of Currency.

import requests

API_KEY = 'fca_live_vNVzhNCSjH1XrW0MunExM6ghMu8n2Sx1QsvTx0fm'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY", "GBP"]
def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(e)
        return None

while True:
    base = input("Enter the base currency (q for quit): ").upper()

    if base == "Q":
        break
    elif base not in CURRENCIES:
        print("Invalid currency")

    data = convert_currency(base)
    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}:{value}")