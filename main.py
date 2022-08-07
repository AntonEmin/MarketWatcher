import schedule
import time
from binance_stream import checkMarkets
from db import init_db

# init_db()
# checkMarkets()
def startShedule(interval):
    schedule.every(interval).minutes.at(':00').do(checkMarkets, interval = interval)

    while True: 
        schedule.run_pending()    
        time.sleep(.1)

if __name__ == '__main__':    
    startShedule(5)