from requests import get

class CurrencyAPI():
    API_KEY = "fca_live_CaBMMSxGRhkNQYtquiPM492DLmbraM6p4NMI26oz"
    BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

    def get_currencies(self):
        try:
            data = get(self.BASE_URL).json()["data"] #sends a GET http request to the endpoint
            return data
        except Exception as e:
            return None
    
    def get_currencies_names(self):
        return list(self.get_currencies().keys())

    def exchange_rate(self, currency1, currency2):
        endpoint = f"{self.BASE_URL}&base_currency={currency1}&currencies={currency2}"
    
        try:
            data = get(endpoint).json()["data"]
            rate = list(data.values())[0]
            return rate
        except Exception as e:
            print('Invalid currencies.')
            return None

    def get_conversion(self, currency1, currency2, amount):
        rate = self.exchange_rate(currency1, currency2)

        if rate is None:
            return

        try:
            amount = float(amount)
            conv_amount = rate * amount
        except:
            return 'Invalid amount'

        return conv_amount