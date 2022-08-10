import requests
from get_all_futures_markets import getMarkets

def getHistoryCandels(interval,limit):
    
    markets = getMarkets() 
    url = 'https://fapi.binance.com/fapi/v1/klines?symbol='
    market_dict = {}
    for market in markets:        
        request_res = requests.get('%s%s&interval=%sm&limit=%s'%(url,market,interval,limit)).json()        
        candels_data = []
        for res in request_res:            
            candels_data.append(
                                [int(res[0]),# open time
                                market,
                                float(res[1]),#open price
                                float(res[2]),#high price
                                float(res[3]),#low price
                                float(res[4]),# close price
                                float(res[5])])#volume
        market_dict[market] = candels_data

    return market_dict
    
    
# [
#   [
#     1499040000000,      // Open time
#     "0.01634790",       // Open
#     "0.80000000",       // High
#     "0.01575800",       // Low
#     "0.01577100",       // Close
#     "148976.11427815",  // Volume
#     1499644799999,      // Close time
#     "2434.19055334",    // Quote asset volume
#     308,                // Number of trades
#     "1756.87402397",    // Taker buy base asset volume
#     "28.46694368",      // Taker buy quote asset volume
#     "17928899.62484339" // Ignore.
#   ]
# ]
    