# This will be the main Python script.
# Here the code I write will interact with the API.
# Making use of Currency.

import requests

API_KEY = 'fca_live_vNVzhNCSjH1XrW0MunExM6ghMu8n2Sx1QsvTx0fm'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY", "GBP"]
def get_exchange_data(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def display_exchange_rates(data, base_currency):
    del data[base_currency]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")

def get_user_input():
    while True:
        base = input("Enter the base currency (q for quit): ").upper()

        if base == "Q":
            break
        elif base not in CURRENCIES:
            print("Invalid currency")
        else:
            return base


def main():
    while True:
        base_currency = get_user_input()

        if base_currency == "Q":
            break

        exchange_data = get_exchange_data(base_currency)

        if exchange_data:
            display_exchange_rates(exchange_data, base_currency)

if __name__ == "__main__":
    main()