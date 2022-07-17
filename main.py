import schedule
import time
from binance_stream import checkMarkets
from db import init_db

# init_db()
# checkMarkets()
schedule.every(15).minutes.at(':00').do(checkMarkets)
while True:
    
    schedule.run_pending()    
    time.sleep(.1)