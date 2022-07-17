import requests

def getMarkets():
    res = requests.get('https://fapi.binance.com/fapi/v1/exchangeInfo').json()
    markets = []   
    for s in res['symbols']:
        if s['contractType'] == 'PERPETUAL':
            markets.append(s['symbol'])
    return markets


