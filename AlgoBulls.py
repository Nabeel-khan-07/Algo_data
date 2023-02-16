#!/usr/bin/env python
# coding: utf-8

# In[83]:


from alpha_vantage.timeseries import TimeSeries
import pandas as pd

class ScriptData:
    def __init__(self):
        self.key = "B58DBY0CMD90L77F"
        self.rdata = {}
        self.pdata = {}
        
    def fetch_intraday_data(self, script):
        ts = TimeSeries(key=self.key)
        data, meta_data = ts.get_intraday(script)
        self.rdata[script] = data

        
    def convert_intraday_data(self, script):
        data = self.rdata[script]       
        df = pd.DataFrame(data).T
        df.reset_index(inplace=True)
        df = df.astype({"1. open": float, "2. high": float, "3. low": float, "4. close": float, "5. volume": int})
        df.rename(columns={"1. open": "open", "2. high": "high", "3. low": "low", "4. close": "close", "5. volume": "volume"}, inplace=True)
        self.pdata[script] = df
        
sd = ScriptData()
sd.fetch_intraday_data('GOOGL')
sd.convert_intraday_data('GOOGL')
print(sd.pdata) 
def indicator1(df, timeperiod):
    ind1_df = pd.DataFrame(columns=['ts', 'indicator'])
    D = {
        'ts':[ ],
        'Ind1':[ ]
    }
    for i in range(len(df)):
        D['ts'].append(df.index[i])
        D['ind1'].append(avg)
        
        
    
    
    print("*"*50+"Indicator")
    for i in range(timeperiod-1, len(df)):
        sum = 0
        for j in range(timeperiod):
            sum += df.loc[i-j]['close']
        avg = sum/timeperiod
        ind1_df=Dataframe(D)
        return ind1_df


indicator1(sd.pdata['GOOGL'], 5)


# 

# In[ ]:




