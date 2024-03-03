from currency_api import CURRENCIES, get_exchange_data
from functions import ExchangeRateDisplayer

def get_user_input():
    while True:
        base = input("Enter the base currency (q for quit): ").upper()

        if base == "Q":
            return None
        elif base not in CURRENCIES:
            print("Invalid currency")
        else:
            return base

def main():
    while True:
        base_currency = get_user_input()

        exchange_data = get_exchange_data(base_currency)

        displayer = ExchangeRateDisplayer(exchange_data, base_currency)
        displayer.display_exchange_rates()

        if base_currency is None:
            break

if __name__ == "__main__":
    main()