import pandas as pd

if os.path.exists(pth) is True and "w" in mode:
        with open (pth) as abcd:
            if len(abcd.read()) > 0:
                raise Exception (f"file {pth} already exists and is not empty")

series_abc = pd.Series(data={'a':1, 'b':2, 'c':3})


df = pd.DataFrame({'Dates': date_series, 'AUD/USD':aud_usd_series, 'EUR/AUD':eur_aud_series})
df.index = df ['Dates']
df.sort_index(inplace=True)



