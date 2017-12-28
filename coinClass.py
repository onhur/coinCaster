"""

File: apiCall.py
Author: Alan Korek
Date: 20171221
class to hold coin information

"""
# imports
import requests


class Coin:

    # function initialize class
    def __init__(self, coin_type):
        self.market_cap_usd = ""
        self.percent_change_1hr = ""
        self.id = ""
        self.percent_change_24hr = ""
        self.available_supply = ""
        self.symbol = ""
        self.last_updated = ""
        self.price_btc = ""
        self.name = ""
        self.percent_change_7days = ""
        self.twenty_four_hour_volume_used = ""
        self.price_usd = ""
        self.total_supply = ""
        self.rank = ""
        self.max_supply = ""
        self.api_call(coin_type=coin_type)

    # get usd cost of coins
    def get_coin_usd(self, amount):
        return amount * self.price_usd

    def api_call(self, coin_type):
        # variables
        url = "https://api.coinmarketcap.com/v1/ticker/"
        response = requests.get(url + coin_type + "/")
        status = response.status_code
        successful_status = 200

        # if status is 200 fill out coin class if not return status
        if status == successful_status:
            api_response = response.json()
            coin_data = api_response[0]

            self.market_cap_usd = coin_data['market_cap_usd']
            self.percent_change_1hr = coin_data['percent_change_1h']
            self.id = coin_data['id']
            self.percent_change_24hr = coin_data['percent_change_24h']
            self.available_supply = coin_data['available_supply']
            self.price_usd = coin_data['price_usd']
            self.twenty_four_hour_volume_used = coin_data['24h_volume_usd']
            self.name = coin_data['name']
            self.symbol = coin_data['symbol']
            self.price_btc = coin_data['price_btc']
            self.rank = coin_data['rank']
            self.last_updated = coin_data['last_updated']
            self.percent_change_7days = coin_data['percent_change_7d']
            self.max_supply = coin_data['max_supply']
            self.total_supply = coin_data['total_supply']
            return self
        else:
            return status
