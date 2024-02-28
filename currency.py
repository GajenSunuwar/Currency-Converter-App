# This will be the main Python script.
# Here the code I write will interact with the API.
# Making use of Currency.

import requests

API_KEY = 'fca_live_vNVzhNCSjH1XrW0MunExM6ghMu8n2Sx1QsvTx0fm'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY", "GBP"]

def get_exchange_data(base):
    if base is None:
        return None  # Return None if the base is None (user decided to quit)

    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data.get("data", None)  # Check if 'data' is present, otherwise return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"Error fetching data: {e}")
    return None
# Added response.raise_for_status()
# to raise an HTTPError for bad responses, allowing better handling of HTTP errors.
# Modified the get_exchange_data function to use data.get("data", None)
# to handle the absence of 'data' in the response.

def display_exchange_rates(data, base_currency):
    if data is not None:
        del data[base_currency]
        for ticker, value in data.items():
            print(f"{ticker}: {value}")
    else:
        print("No exchange rate data available.")
# Updated the display_exchange_rates function to handle the case when data is None.

def get_user_input():
    while True:
        base = input("Enter the base currency (q for quit): ").upper()

        if base == "Q":
            return None # Return None if the user decides to quit
        elif base not in CURRENCIES:
            print("Invalid currency")
        else:
            return base

def main():
    while True:
        base_currency = get_user_input()

        exchange_data = get_exchange_data(base_currency)

        display_exchange_rates(exchange_data, base_currency)

        if base_currency is None:
            break  # Exit the loop if the user decides to quit

if __name__ == "__main__":
    main()