def display_exchange_rates(data, base_currency):
    if data is not None:
        del data[base_currency]
        for ticker, value in data.items():
            print(f"{ticker}: {value}")
    else:
        print("No exchange rate data available.")