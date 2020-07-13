

import pandas as pd
import plotly.express as px
import plotly
import time



#plotly.io.orca.config.executable = "/home/matteo/miniconda3/envs/Test/bin/orca"

#import orca



df = pd.read_pickle("dataFrame_country.pkl")
minidf = df[:100000]

fig = px.scatter_mapbox(minidf, lat="lat", lon="long", hover_name="lang",
                        color_discrete_sequence=["fuchsia"], zoom=3, height=800)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
#Stampo il plot

#plotly.io.orca.ensure_server()
#time.sleep(10)


#fig.write_image("scatteredPlot.png")