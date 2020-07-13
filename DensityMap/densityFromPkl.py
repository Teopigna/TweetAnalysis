import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mplleaflet as mpll
#import statsmodels

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


df = df.sample(frac = 0.01)

m = df.apply(remove_Istanbul, axis = 1)
#print(m)
df_r = df[m]

print(len(df_r.index))

print(len(df.index))
#print(df)


f, ax = plt.subplots(1, figsize=(12, 9))

sns.kdeplot(df_r['long'], df_r['lat'], 
            shade=False, cmap='gnuplot', #hot, Reds, autumn
            bw=(0.65, 0.65), 
            n_levels=15,
            ax=ax)


ax.set_axis_off()

f.savefig("output_density_TOT.png")

plt.axis('equal')
#plt.show()

import mplleaflet

mplleaflet.show(fig=f)
