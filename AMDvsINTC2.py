import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
import numpy as np

start = dt.datetime(2013,1,1)
end = dt.datetime(2020,10,8)

df = web.DataReader('AMD', 'yahoo', start, end)
df2 = web.DataReader('INTC','yahoo', start,end)

stock = pd.DataFrame({"AMD":df['Adj Close'],
                    "INTC":df2['Adj Close']})
stock_return = stock.apply(lambda x: x/ x[0])
print(stock_return.head())

stock_return.plot(figsize=(14,6), grid= True)

plt.show()
