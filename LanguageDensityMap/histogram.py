import matplotlib.pyplot as plt
import matplotlib.ticker
import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import gaussian_kde
'''
df_c = pd.read_pickle("TweetDF/dataFrame_country.pkl")
df_s = pd.read_pickle("TweetDF/dataFrame_south.pkl")
df_nw = pd.read_pickle("TweetDF/dataFrame_nw.pkl")
df_e =  pd.read_pickle("TweetDF/dataFrame_east.pkl")

frames = [df_c, df_s, df_nw, df_e]

df = pd.concat(frames)

def remove_Istanbul(row):
    if  28.7 <= row['long'] <= 29.3 and 40.8 <= row['lat'] <= 41.25:
        return False
    else:
        return True

m = df.apply(remove_Istanbul, axis = 1)
#print(m)
df_r = df[m]

#df = df.sample(frac = 0.5)
'''

df_border = pd.read_pickle("DFBorders/dataFrame_bulgaria.pkl")

df_border[['latitude','longitude']] = pd.DataFrame(df_border.Coordinates.to_list(), index=df_border.index)

value_ar = ['ar']
value_en = ['en']
value_tr = ['tr']
value_bg = ['bg']
value_und = ['und']

df_ar = df_border[df_border.Lang.isin(value_ar)]
#df_in = df_border[df_border.Lang.isin(value_in)]
df_en = df_border[df_border.Lang.isin(value_en)]
df_tr = df_border[df_border.Lang.isin(value_tr)]
df_bg = df_border[df_border.Lang.isin(value_bg)]
df_und = df_border[df_border.Lang.isin(value_und)]


df_en_mar = df_en[df_en.Date.str.contains('Mar')]
df_en_apr = df_en[df_en.Date.str.contains('Apr')]
df_en_may = df_en[df_en.Date.str.contains('May')]

df_tr_mar = df_tr[df_tr.Date.str.contains('Mar')]
df_tr_apr = df_tr[df_tr.Date.str.contains('Apr')]
df_tr_may = df_tr[df_tr.Date.str.contains('May')]

df_bg_mar = df_bg[df_bg.Date.str.contains('Mar')]
df_bg_apr = df_bg[df_bg.Date.str.contains('Apr')]
df_bg_may = df_bg[df_bg.Date.str.contains('May')]

df_und_mar = df_und[df_und.Date.str.contains('Mar')]
df_und_apr = df_und[df_und.Date.str.contains('Apr')]
df_und_may = df_und[df_und.Date.str.contains('May')]

df_ar_mar = df_ar[df_ar.Date.str.contains('Mar')]
df_ar_apr = df_ar[df_ar.Date.str.contains('Apr')]
df_ar_may = df_ar[df_ar.Date.str.contains('May')]

longs = list(df_ar_may.longitude)
lats = list(df_ar_may.latitude)

longitudes = np.array(longs)
latitudes = np.array(lats)


plt.hist2d(longitudes, latitudes, (20, 20), cmap=plt.cm.gnuplot)
#fmt = matplotlib.ticker.ScalarFormatter(useMathText=True)
plt.colorbar()#format=fmt)
plt.show()

