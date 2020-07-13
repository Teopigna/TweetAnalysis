import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#import mplleaflet as mpll
import numpy as np




df_border = pd.read_pickle("DFBorders/dataFrame_greece.pkl")

df_border[['latitude','longitude']] = pd.DataFrame(df_border.Coordinates.to_list(), index=df_border.index)

value_ar = ['ar']
#value_in = ['in']
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

f, ax = plt.subplots(1, figsize=(12, 9))

#kwargs = {'levels': np.arange(0, 1, 0.1)}

sns.kdeplot(df_und_may['longitude'], df_und_may['latitude'], #cbar=True,
            shade=False, cmap='gnuplot', #hot, Reds, autumn
            bw=(0.4,0.4), #gridsize = 500,
            n_levels=15, #**kwargs, 
            ax=ax)

ax.set_axis_off()

#f.savefig("output_density.png")

plt.axis('equal')
#plt.colorbar()
#plt.show()

import mplleaflet

mplleaflet.show(fig=f)

'''
out_csv = open("ar_apr.csv", "w")

df_ar_apr.to_csv(out_csv, encoding='utf-8', index=False)

out_csv.close()


import plotly.express as px

fig = px.scatter_mapbox(df_ar_apr, lat="latitude", lon="longitude", 
                        color_discrete_sequence=["fuchsia"], zoom=3, height=800)
fig.update_layout(mapbox_style="open-street-map")

fig.show()



#locations = df_ar[['latitude', 'longitude']]

f, ax = plt.subplots(1, figsize=(12, 9))

ax = sns.kdeplot(df_ar_apr['longitude'], df_ar_apr['latitude'], 
            shade=False, cmap='gnuplot', #hot, Reds, autumn, gnuplot
            bw=(0.337,0.337), clip=((1,50), (1,50)),
            #cbar=True,
            ax=ax)

ax = sns.scatterplot(x=df_ar_apr['longitude'], y=df_ar_apr['latitude'], alpha=0.2)


label_patch = mpatches.Patch(
        color=sns.color_palette('gnuplot')[2],
        label='Arab')

labels = [label_patch]

plt.legend(handles=labels, loc='upper left')

sns.kdeplot(df_en['longitude'], df_en['latitude'], 
            shade=False, cmap='Greens',  
            ax=ax)

sns.kdeplot(df_tr['longitude'], df_tr['latitude'], 
            shade=False, cmap='vlag', 
            ax=ax)


ax.set_axis_off()

#plt.axis('equal')
plt.show()

import mplleaflet

mplleaflet.show(fig=f)
'''
#print(df_ar)




