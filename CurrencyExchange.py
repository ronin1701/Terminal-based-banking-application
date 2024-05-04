from FileManager import FileManager
from HistoryMessages import HistoryMessages
import requests as rq

class CurrencyExchange:

    def __init__(self, balance = 0):
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        

    def write_to_history(self, hist_dict):

        self.file_manager.add_to_json(hist_dict, self.hist_file_path)

    def get_exchange_rates(self):

        try:
            rates = rq.get('https://fake-api.apps.berlintech.ai/api/currency_exchange').json()
            return rates
        
        except Exception as e:
            print(f"Request Error: {e}") 
            return None
    
    def exchange_currency(self, currency_from, currency_to, amount):
        pass

        # implement a process that transfers the specified amount from currency `currency_from` 
        # to currency `currency_to` and, if positive, returns the amount in the new currency
        

        try:
            amount = float(amount)
        except ValueError:
            print('Currency exchange failed!')
            history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
            self.write_to_history(history_message)
            return None

        exchange_rates = self.get_exchange_rates()

        if exchange_rates and currency_from in exchange_rates and currency_to in exchange_rates:
            conversion_rate = exchange_rates[currency_to] / exchange_rates[currency_from]
            converted_amount = amount * conversion_rate
            history_message = HistoryMessages.exchange("success", amount, converted_amount, currency_from, currency_to)
            self.write_to_history(history_message)
            return converted_amount
        else:
            print("Currency exchange failed!")
            history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
            self.write_to_history(history_message)
            return None
        # in case of a negative outcome, the history entry looks like this
        # - if currency_from or currency_to is specified incorrectly
        # - if amount is not a number

