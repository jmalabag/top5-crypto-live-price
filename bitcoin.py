import apikey
import requests

headers = {
    'X-CMC_PRO_API_KEY': apikey.key,
    'Accepts': 'application/json'
}

params = {
    'start': '1',
    'limit': '5',
    'convert': 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
json = requests.get(url, params=params, headers=headers).json()
try:
    coins = json['data']

    for x in coins:
        if x['symbol'] == 'BTC':
            x['quote']['USD']['price']
        print(x['symbol'], x['quote']['USD']['price'] )
except:
    if apikey.key == '@todo':
        print('Check the API key')
    else:
        print('Error')