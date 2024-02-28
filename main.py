from currency_api import CURRENCIES, get_exchange_data
from functions import display_exchange_rates

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

        display_exchange_rates(exchange_data, base_currency)

        if base_currency is None:
            break

if __name__ == "__main__":
    main()