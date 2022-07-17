import unicorn_binance_websocket_api
import pandas as pd
import pandas_ta as ta
import timeit, time
from telegram_sender import send
from getHistory import getHistoryCandels
from get_all_futures_markets import getMarkets
from IPython.display import display 
from db import log_db

def checkMarkets():

        markets = getMarkets()                
        interval = '15m'
        limit = '50'
        market_dict = {}
        market_dfs = {}

        cols = ['time', 'symbol', 'open', 'high', 'low', 'close', 'volume']



        market_dict = getHistoryCandels(markets,interval,limit)
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
        start = timeit.default_timer()   

        for key in market_dict:

                market_dfs[key] = pd.DataFrame(market_dict[key] , columns= cols)
                market_dfs[key]['date'] = pd.to_datetime(market_dfs[key]['time'], unit='ms')
                market_dfs[key]['rsi'] = ta.rsi(close=market_dfs[key].close,length=14)

                if market_dfs[key]['rsi'].iloc[-1] > 75:
                        #log_db(market_dfs[key].iloc[-1])
                        send('look at short '+key+' rsi '+str(market_dfs[key]['rsi'].iloc[-1])+' Price '+str(market_dfs[key]['close'].iloc[-1]))
                        

                elif market_dfs[key]['rsi'].iloc[-1] < 25:
                        #log_db(market_dfs[key].iloc[-1])
                        send('look at long '+key+' rsi '+str(market_dfs[key]['rsi'].iloc[-1])+' Price '+str(market_dfs[key]['close'].iloc[-1]))
                        
                                        
        stop = timeit.default_timer()
        print('Time ', stop-start )
        


# for key in market_dfs:
#     print(key)
#     print(market_dfs[key]['rsi'].iloc[-1])

# for key in market_dfs:
#     display(market_dfs.get(key))

##### socet version
# ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
# ubwa.create_stream(['kline_1m'], markets, output="UnicornFy")
# for key in market_dfs:
#                         display(market_dfs.get(key))


# while True:
#         if ubwa.is_manager_stopping():
#             exit(0)
#         oldest_data = ubwa.pop_stream_data_from_stream_buffer()
#         if oldest_data is False:
#             time.sleep(0.01)
#         else:
#             try:
#                 if oldest_data['kline']['is_closed']:
#                     print('oldest closed candel')
#                     print(oldest_data)
#                     print(market_dfs[oldest_data['symbol']])
#                     new_df = pd.DataFrame([int(oldest_data['event_time']/1000),
#                                   oldest_data['symbol'],
#                                   oldest_data['kline']['open_price'],
#                                   oldest_data['kline']['high_price'],
#                                   oldest_data['kline']['low_price'],
#                                   oldest_data['kline']['close_price'],
#                                   oldest_data['kline']['base_volume']],columns=cols)
#                     display(new_df)
#                     market_dfs[oldest_data['symbol']] = pd.concat(market_dfs[oldest_data['symbol']],new_df)
#                 #df = pd.DataFrame(data_list, columns=['time', 'symbol', 'open', 'high', 'low', 'close', 'volume'])
#                 #print('print df')
#                     for key in market_dfs:
#                         display(market_dfs.get(key))
#                 # remove # to activate the print function:                
#             except KeyError:
#                 # Any kind of error...
#                 # not able to process the data? write it back to the stream_buffer
#                 ubwa.add_to_stream_buffer(oldest_data)