import json
import sqlite3
import uuid

def init_db():
    con = sqlite3.connect('mydb.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Streaming
                (Id text, Symbol text, Date datetime, OpenPrice real, PriceAfter5m real, Diff5m real, PriceAfter15m real, Diff15m real, PriceAfter30m real, Diff30m real, PriceAfter1h real, Diff1h real,  IsClosed boolean )''')
    con.commit()
    con.close()

def log_db(df):
    
    id = str(uuid.uuid4().hex) #Creates something like: 2345234jhkj345234jhkjhk2345234jhkjhk
    symbol = df["symbol"]
    date = df["time"]
    price = df["close"]
    
    print("log:")
    print("symbol: " + symbol)
    print("interval: " + str(date))
    print("close: " + str(price))   

    row = (id, symbol, date, price)
    con = sqlite3.connect('mydb.db')
    cur = con.cursor()
    cmd = "insert into Streaming (Id, Symbol, Date, OpenPrice) values (?, ?, ?, ?)" 
    
    cur.execute(cmd, row)
    
    con.commit()
    con.close()    
    print('inserted')