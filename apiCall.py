"""

Depreciated 20171223:  Moved to coinClass
File: apiCall.py
Author: Alan Korek
Date: 20171221
Script calls the coinmarketcap.com api for data on a specific coin
returns coin object with data on success returns status number of failure

"""
# imports
import requests
import coinClass


def api_call(coin_type):
    # variables
    url = "https://api.coinmarketcap.com/v1/ticker/"
    response = requests.get(url + coin_type + "/")
    status = response.status_code
    successful_status = 200
    c_data = coinClass.Coin()
    # if status is 200 fill out coin class if not return status
    if status == successful_status:
        api_response = response.json()
        coin_data = api_response[0]

        c_data.market_cap_usd = coin_data['market_cap_usd']
        c_data.percent_change_1hr = coin_data['percent_change_1h']
        c_data.id = coin_data['id']
        c_data.percent_change_24hr = coin_data['percent_change_24h']
        c_data.available_supply = coin_data['available_supply']
        c_data.price_usd = coin_data['price_usd']
        c_data.twenty_four_hour_volume_used = coin_data['24h_volume_usd']
        c_data.name = coin_data['name']
        c_data.symbol = coin_data['symbol']
        c_data.price_btc = coin_data['price_btc']
        c_data.rank = coin_data['rank']
        c_data.last_updated = coin_data['last_updated']
        c_data.percent_change_7days = coin_data['percent_change_7d']
        c_data.max_supply = coin_data['max_supply']
        c_data.total_supply = coin_data['total_supply']
        return c_data
    else:
        return status
