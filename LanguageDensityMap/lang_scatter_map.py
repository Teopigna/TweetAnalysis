import pandas as pd

df_border = pd.read_pickle("DFBorders/dataFrame_syria.pkl")


df_border[['Lat','Long']] = pd.DataFrame(df_border.Coordinates.to_list(), index=df_border.index)

value_ar = ['ar']
value_en = ['en']
value_tr = ['tr']

df_ar = df_border[df_border.Lang.isin(value_ar)]
df_en = df_border[df_border.Lang.isin(value_en)]
df_tr = df_border[df_border.Lang.isin(value_tr)]
#print(len(df_ar.index))


df_ar['Lang'] = 'Arab'
print(df_ar)

df_ar_mar = df_ar[df_ar.Date.str.contains('Mar')]
df_ar_apr = df_ar[df_ar.Date.str.contains('Apr')]
df_ar_may = df_ar[df_ar.Date.str.contains('May')]

print(df_ar_apr)

df_en['Lang'] = 'English'
df_tr['Lang'] = 'Turkish'

import plotly.express as px

fig = px.scatter_mapbox(df_ar_mar, lat="Lat", lon="Long", color_discrete_sequence=['Red'],#opacity=0.1,
                        #color_discrete_sequence=["fuchsia"], 
                        zoom=3, height=800
                        )
fig2 = px.scatter_mapbox(df_ar_apr, lat="Lat", lon="Long", color_discrete_sequence=['Blue'],#opacity=0.1,
                        #color_discrete_sequence=["fuchsia"], 
                        zoom=3, height=800
                        )
fig3 = px.scatter_mapbox(df_ar_may, lat="Lat", lon="Long", color_discrete_sequence=['Green'],#opacity=0.1,
                        #color_discrete_sequence=["fuchsia"], 
                        zoom=3, height=800
                        )

fig.add_trace(fig2.data[0])  
fig.add_trace(fig3.data[0])  
fig.update_layout(showlegend=True)
fig.update_layout(mapbox_style="open-street-map")
'''
fig = px.scatter_mapbox(df_tr, lat="Lat", lon="Long", color = 'Lang',color_discrete_sequence=['Yellow'], #opacity=0.1,
                        #color_discrete_sequence=["fuchsia"], 
                        zoom=3, height=800
                        )
fig2 = px.scatter_mapbox(df_en, lat="Lat", lon="Long", color = 'Lang',color_discrete_sequence=['Blue'],#opacity=0.1,
                        #color_discrete_sequence=["fuchsia"], 
                        zoom=3, height=800
                        )
fig3 = px.scatter_mapbox(df_ar, lat="Lat", lon="Long", color = 'Lang',color_discrete_sequence=['Red'],#opacity=0.1,
                        #color_discrete_sequence=["fuchsia"], 
                        zoom=3, height=800
                        )

fig.add_trace(fig2.data[0])  
fig.add_trace(fig3.data[0])  
fig.update_layout(showlegend=True)
fig.update_layout(mapbox_style="open-street-map")
'''
'''
fig = px.density_mapbox(df_ar, lat='Lat', lon='Long', radius=5,
                    center=dict(lat=39, lon=34), color_continuous_scale='Electric', zoom=3.5, opacity= 0.6
                    #mapbox_style="open-street-map"
                    )
              
fig.update_layout(mapbox_style="open-street-map")


fig = px.density_mapbox(minidf, lat='lat', lon='long', radius=5,
                    center=dict(lat=39, lon=34), color_continuous_scale='portland', zoom=3.5, opacity= 0.6,
                    mapbox_style="open-street-map")
'''

fig.show()
