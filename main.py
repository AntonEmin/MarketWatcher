import schedule
import time
from binance_stream import checkMarkets
from db import init_db

# init_db()
# checkMarkets()
def startShedule(*argv):
    scheduler1 = schedule.Scheduler()
    scheduler2 = schedule.Scheduler()

    for arg in argv:        
        if arg[-1] == 'm':
            scheduler1 = schedule.Scheduler()
            if len(arg) == 3:
                scheduler1.every( int(arg[0:1])).minutes.at(':00').do(checkMarkets, interval = arg)
            else:
                scheduler1.every( int(arg[0])).minutes.at(':00').do(checkMarkets, interval = arg)
        else:
            if len(arg) == 3:
                scheduler2.every(int(arg[0:1])).hours.do(checkMarkets, interval = arg)
            else:
                scheduler2.every(int(arg[0])).hours.do(checkMarkets, interval = arg)
        
    

    while True: 
        scheduler1.run_pending()    
        scheduler2.run_pending()   
        time.sleep(.1)

if __name__ == '__main__':    
    startShedule('5m','1h')