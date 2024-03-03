class ExchangeRateDisplayer:
    def __init__(self, data, base_currency):
        self.data = data
        self.base_currency = base_currency

    def display_exchange_rates(self):
        if self.data is not None:
            del self.data[self.base_currency]
            for ticker, value in self.data.items():
                print(f"{ticker}: {value}")
        else:
            print("No exchange rate data available.")