import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np
import json

total_tweets_lang = { 
    'ar' : 0,
    'tr' : 0,
    'en' : 0, 
    'el' : 0,
    'hy' : 0,
    #'sr' : 0,
    'ka' : 0,
    'fa' : 0,
    'es' : 0,
    'sl' : 0,
    'de' : 0,
    'ro' : 0,
    'hu' : 0,
    'cs' : 0,
    'nl' : 0,
    'it' :0,
    'ru' : 0,
    'zh' : 0,
    'pl' : 0,
    #'pa' : 0,
    'iw' : 0, 
    'ckb' : 0,
    #'ps' : 0,
    'vi' : 0,
    'fr' : 0,
    #'ur' : 0,
    'pt' : 0,
    'fi' : 0,
    'no' : 0,
    'da' : 0,
    #'sd' : 0,
    'ja' : 0,
    'ca' : 0,
    'eu' : 0,
    'hi' : 0,
    'sv' : 0,
    'uk' : 0,
    #'ko' : 0,
    'lv' : 0,
    'is' : 0,
    'lt' : 0,
    'in' : 0,
    'cy' : 0,
    'et' : 0,
    'ht' : 0,
    'tl' : 0,
    'bg' : 0,
    #'th' : 0,
    #'ml' : 0,
    #'ug' : 0,
    #'bn' : 0,
    #'mr' : 0,
    'und' : 0
}


#Contatori per i dati al confine con la Grecia
greece_tweets = 0
#Dizionario per contare i linguaggi dei tweet al confine con la Grecia


greece_tweets_lang = { 
    'ar' : 0,
    'tr' : 0,
    'en' : 0, 
    'el' : 0,
    'hy' : 0,
    'sr' : 0,
    'ka' : 0,
    'fa' : 0,
    'es' : 0,
    'sl' : 0,
    'de' : 0,
    'ro' : 0,
    'hu' : 0,
    'cs' : 0,
    'nl' : 0,
    'it' :0,
    'ru' : 0,
    'zh' : 0,
    'pl' : 0,
    'pa' : 0,
    'iw' : 0, 
    'ckb' : 0,
    'ps' : 0,
    'vi' : 0,
    'fr' : 0,
    'ur' : 0,
    'pt' : 0,
    'fi' : 0,
    'no' : 0,
    'da' : 0,
    'sd' : 0,
    'ja' : 0,
    'ca' : 0,
    'eu' : 0,
    'hi' : 0,
    'sv' : 0,
    'uk' : 0,
    'ko' : 0,
    'lv' : 0,
    'is' : 0,
    'lt' : 0,
    'in' : 0,
    'cy' : 0,
    'et' : 0,
    'ht' : 0,
    'tl' : 0,
    'bg' : 0,
    'th' : 0,
    'ml' : 0,
    'ug' : 0,
    'bn' : 0,
    'mr' : 0,
    'und' : 0,
    'other' : 0
}
#Contatori per i dati al confine con la Georgia
georgia_tweets = 0
georgia_tweets_lang = { 
    'ar' : 0,
    'tr' : 0,
    'en' : 0, 
    'el' : 0,
    'hy' : 0,
    'sr' : 0,
    'ka' : 0,
    'fa' : 0,
    'es' : 0,
    'sl' : 0,
    'de' : 0,
    'ro' : 0,
    'hu' : 0,
    'cs' : 0,
    'nl' : 0,
    'it' :0,
    'ru' : 0,
    'zh' : 0,
    'pl' : 0,
    'pa' : 0,
    'iw' : 0, 
    'ckb' : 0,
    'ps' : 0,
    'vi' : 0,
    'fr' : 0,
    'ur' : 0,
    'pt' : 0,
    'fi' : 0,
    'no' : 0,
    'da' : 0,
    'sd' : 0,
    'ja' : 0,
    'ca' : 0,
    'eu' : 0,
    'hi' : 0,
    'sv' : 0,
    'uk' : 0,
    'ko' : 0,
    'lv' : 0,
    'is' : 0,
    'lt' : 0,
    'in' : 0,
    'cy' : 0,
    'et' : 0,
    'ht' : 0,
    'tl' : 0,
    'bg' : 0,
    'th' : 0,
    'ml' : 0,
    'ug' : 0,
    'bn' : 0,
    'mr' : 0,
    'und' : 0,
    'other' : 0
}
#Contatori per i dati al confine con la Syria
syria_tweets = 0
syria_tweets_lang = { 
    'ar' : 0,
    'tr' : 0,
    'en' : 0, 
    'el' : 0,
    'hy' : 0,
    'sr' : 0,
    'ka' : 0,
    'fa' : 0,
    'es' : 0,
    'sl' : 0,
    'de' : 0,
    'ro' : 0,
    'hu' : 0,
    'cs' : 0,
    'nl' : 0,
    'it' :0,
    'ru' : 0,
    'zh' : 0,
    'pl' : 0,
    'pa' : 0,
    'iw' : 0, 
    'ckb' : 0,
    'ps' : 0,
    'vi' : 0,
    'fr' : 0,
    'ur' : 0,
    'pt' : 0,
    'fi' : 0,
    'no' : 0,
    'da' : 0,
    'sd' : 0,
    'ja' : 0,
    'ca' : 0,
    'eu' : 0,
    'hi' : 0,
    'sv' : 0,
    'uk' : 0,
    'ko' : 0,
    'lv' : 0,
    'is' : 0,
    'lt' : 0,
    'in' : 0,
    'cy' : 0,
    'et' : 0,
    'ht' : 0,
    'tl' : 0,
    'bg' : 0,
    'th' : 0,
    'ml' : 0,
    'ug' : 0,
    'bn' : 0,
    'mr' : 0,
    'und' : 0,
    'other' : 0
}

#Contatori per i dati al confine con la Bulgaria
bulgaria_tweets = 0
bulgaria_tweets_lang = { 
    'ar' : 0,
    'tr' : 0,
    'en' : 0, 
    'el' : 0,
    'hy' : 0,
    'sr' : 0,
    'ka' : 0,
    'fa' : 0,
    'es' : 0,
    'sl' : 0,
    'de' : 0,
    'ro' : 0,
    'hu' : 0,
    'cs' : 0,
    'nl' : 0,
    'it' :0,
    'ru' : 0,
    'zh' : 0,
    'pl' : 0,
    'pa' : 0,
    'iw' : 0, 
    'ckb' : 0,
    'ps' : 0,
    'vi' : 0,
    'fr' : 0,
    'ur' : 0,
    'pt' : 0,
    'fi' : 0,
    'no' : 0,
    'da' : 0,
    'sd' : 0,
    'ja' : 0,
    'ca' : 0,
    'eu' : 0,
    'hi' : 0,
    'sv' : 0,
    'uk' : 0,
    'ko' : 0,
    'lv' : 0,
    'is' : 0,
    'lt' : 0,
    'in' : 0,
    'cy' : 0,
    'et' : 0,
    'ht' : 0,
    'tl' : 0,
    'bg' : 0,
    'th' : 0,
    'ml' : 0,
    'ug' : 0,
    'bn' : 0,
    'mr' : 0,
    'und' : 0,
    'other' : 0
}

#Contatori per i dati al confine con la Armenia
armenia_tweets = 0
armenia_tweets_lang = { 
    'ar' : 0,
    'tr' : 0,
    'en' : 0, 
    'el' : 0,
    'hy' : 0,
    'sr' : 0,
    'ka' : 0,
    'fa' : 0,
    'es' : 0,
    'sl' : 0,
    'de' : 0,
    'ro' : 0,
    'hu' : 0,
    'cs' : 0,
    'nl' : 0,
    'it' :0,
    'ru' : 0,
    'zh' : 0,
    'pl' : 0,
    'pa' : 0,
    'iw' : 0, 
    'ckb' : 0,
    'ps' : 0,
    'vi' : 0,
    'fr' : 0,
    'ur' : 0,
    'pt' : 0,
    'fi' : 0,
    'no' : 0,
    'da' : 0,
    'sd' : 0,
    'ja' : 0,
    'ca' : 0,
    'eu' : 0,
    'hi' : 0,
    'sv' : 0,
    'uk' : 0,
    'ko' : 0,
    'lv' : 0,
    'is' : 0,
    'lt' : 0,
    'in' : 0,
    'cy' : 0,
    'et' : 0,
    'ht' : 0,
    'tl' : 0,
    'bg' : 0,
    'th' : 0,
    'ml' : 0,
    'ug' : 0,
    'bn' : 0,
    'mr' : 0,
    'und' : 0,
    'other' : 0
}

#Contatori per i dati al confine con la Iran
iran_tweets = 0
iran_tweets_lang = { 
    'ar' : 0,
    'tr' : 0,
    'en' : 0, 
    'el' : 0,
    'hy' : 0,
    'sr' : 0,
    'ka' : 0,
    'fa' : 0,
    'es' : 0,
    'sl' : 0,
    'de' : 0,
    'ro' : 0,
    'hu' : 0,
    'cs' : 0,
    'nl' : 0,
    'it' :0,
    'ru' : 0,
    'zh' : 0,
    'pl' : 0,
    'pa' : 0,
    'iw' : 0, 
    'ckb' : 0,
    'ps' : 0,
    'vi' : 0,
    'fr' : 0,
    'ur' : 0,
    'pt' : 0,
    'fi' : 0,
    'no' : 0,
    'da' : 0,
    'sd' : 0,
    'ja' : 0,
    'ca' : 0,
    'eu' : 0,
    'hi' : 0,
    'sv' : 0,
    'uk' : 0,
    'ko' : 0,
    'lv' : 0,
    'is' : 0,
    'lt' : 0,
    'in' : 0,
    'cy' : 0,
    'et' : 0,
    'ht' : 0,
    'tl' : 0,
    'bg' : 0,
    'th' : 0,
    'ml' : 0,
    'ug' : 0,
    'bn' : 0,
    'mr' : 0,
    'und' : 0,
    'other' : 0
}

#Contatori per i dati al confine con la Iraq
iraq_tweets = 0
iraq_tweets_lang = { 
    'ar' : 0,
    'tr' : 0,
    'en' : 0, 
    'el' : 0,
    'hy' : 0,
    'sr' : 0,
    'ka' : 0,
    'fa' : 0,
    'es' : 0,
    'sl' : 0,
    'de' : 0,
    'ro' : 0,
    'hu' : 0,
    'cs' : 0,
    'nl' : 0,
    'it' :0,
    'ru' : 0,
    'zh' : 0,
    'pl' : 0,
    'pa' : 0,
    'iw' : 0, 
    'ckb' : 0,
    'ps' : 0,
    'vi' : 0,
    'fr' : 0,
    'ur' : 0,
    'pt' : 0,
    'fi' : 0,
    'no' : 0,
    'da' : 0,
    'sd' : 0,
    'ja' : 0,
    'ca' : 0,
    'eu' : 0,
    'hi' : 0,
    'sv' : 0,
    'uk' : 0,
    'ko' : 0,
    'lv' : 0,
    'is' : 0,
    'lt' : 0,
    'in' : 0,
    'cy' : 0,
    'et' : 0,
    'ht' : 0,
    'tl' : 0,
    'bg' : 0,
    'th' : 0,
    'ml' : 0,
    'ug' : 0,
    'bn' : 0,
    'mr' : 0,
    'und' : 0,
    'other' : 0
}

df_country = pd.read_pickle("TweetDF/dataFrame_country.pkl")
df_nw = pd.read_pickle("TweetDF/dataFrame_nw.pkl")
df_south = pd.read_pickle("TweetDF/dataFrame_south.pkl")
df_east = pd.read_pickle("TweetDF/dataFrame_east.pkl")

languages_list = df_country['lang'].tolist() + df_nw['lang'].tolist() + df_south['lang'].tolist() + df_east['lang'].tolist()
#Print list of all utilized languages
languages_list_no_dup = list(dict.fromkeys(languages_list)) #delete duplicates, needed to only check the number of different languages
print(languages_list_no_dup) 

coordinates_list = list(zip(df_country.lat, df_country.long)) + list(zip(df_nw.lat, df_nw.long)) + list(zip(df_south.lat, df_south.long)) + list(zip(df_east.lat, df_east.long))
dates_list = list(df_country.created_at) + list(df_nw.created_at) + list(df_south.created_at) + list(df_east.created_at)

#Cut date to #Month N° (examples: 'APR 01' , 'MAY 24')
for idx, el in enumerate(dates_list):
    #print(el[4:])
    el = el[4:]
    el = el[:-20]
    dates_list[idx] = el

#print(dates_list)

print("Number of geolocated tweet:  "+str(len(coordinates_list)))
print(df_east)

import plotly.express as px
import plotly


#Greece border polygon points
df_gr = pd.read_json('Polygons/GreeceBorderPolygonV2.json')
df_gr = df_gr[['coordinates']]
df_gr[['long','lat']] = pd.DataFrame(df_gr.coordinates.to_list(), index=df_gr.index)
'''
fig = px.scatter_mapbox(df_gr, lat="lat", lon="long", 
                        color_discrete_sequence=["fuchsia"], zoom=3, height=800)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
'''
greece_longs = df_gr['long']
greece_lats = df_gr['lat']
#Georgian border polygon points
df_ge = pd.read_json('Polygons/GeorgiaBorderPolygonV2.json')
df_ge = df_ge[['coordinates']]
df_ge[['long','lat']] = pd.DataFrame(df_ge.coordinates.to_list(), index=df_ge.index)

georgia_longs = df_ge['long']
georgia_lats = df_ge['lat']
'''
fig = px.scatter_mapbox(df_gr, lat="lat", lon="long", 
                        color_discrete_sequence=["fuchsia"], zoom=3, height=800)

fig2 = px.scatter_mapbox(df_ge, lat="lat", lon="long", 
                        color_discrete_sequence=["red"], zoom=3, height=800)

fig.add_trace(fig2.data[0])                                                    
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
'''
#Syrian border polygon points
df_s = pd.read_json('Polygons/SyriaBorderPolygonV2.json')
df_s = df_s[['coordinates']]
df_s[['long','lat']] = pd.DataFrame(df_s.coordinates.to_list(), index=df_s.index)

syria_longs = df_s['long']
syria_lats = df_s['lat']

#Bulgaria border polygon points
df_b = pd.read_json('Polygons/BulgaryBorderPolygonV2.json')
df_b = df_b[['coordinates']]
df_b[['long','lat']] = pd.DataFrame(df_b.coordinates.to_list(), index=df_b.index)

bulgaria_longs = df_b['long']
bulgaria_lats = df_b['lat']

#Armenia border polygon points
df_ar = pd.read_json('Polygons/ArmeniaBorderPolygonV2.json')
df_ar = df_ar[['coordinates']]
df_ar[['long','lat']] = pd.DataFrame(df_ar.coordinates.to_list(), index=df_ar.index)

armenia_longs = df_ar['long']
armenia_lats = df_ar['lat']
#Iran border polygon points
df_iran = pd.read_json('Polygons/IranBorderPolygonV2.json')
df_iran = df_iran[['coordinates']]
df_iran[['long','lat']] = pd.DataFrame(df_iran.coordinates.to_list(), index=df_iran.index)

iran_longs = df_iran['long']
iran_lats = df_iran['lat']
#Iraq border polygon points
df_iraq = pd.read_json('Polygons/IraqBorderPolygonV2.json')
df_iraq = df_iraq[['coordinates']]
df_iraq[['long','lat']] = pd.DataFrame(df_iraq.coordinates.to_list(), index=df_iraq.index)

iraq_longs = df_iraq['long']
iraq_lats = df_iraq['lat']


greece_area_vect = np.column_stack((greece_longs, greece_lats)) # Reshape coordinates
georgia_area_vect = np.column_stack((georgia_longs, georgia_lats))
syria_area_vect = np.column_stack((syria_longs, syria_lats))
bulgaria_area_vect = np.column_stack((bulgaria_longs, bulgaria_lats))
armenia_area_vect = np.column_stack((armenia_longs, armenia_lats))
iran_area_vect = np.column_stack((iran_longs, iran_lats))
iraq_area_vect = np.column_stack((iraq_longs, iraq_lats))

greece_polygon = Polygon(greece_area_vect) # create polygon
georgia_polygon = Polygon(georgia_area_vect)
syria_polygon = Polygon(syria_area_vect)
bulgaria_polygon = Polygon(bulgaria_area_vect)
armenia_polygon = Polygon(armenia_area_vect)
iran_polygon = Polygon(iran_area_vect)
iraq_polygon = Polygon(iraq_area_vect)
#Dataframe con i dati di ogni confine
df_greece = pd.DataFrame(columns=('Coordinates', 'Date', 'Lang'))
df_georgia = pd.DataFrame(columns=('Coordinates', 'Date', 'Lang'))
df_syria = pd.DataFrame(columns=('Coordinates', 'Date', 'Lang'))
df_bulgaria = pd.DataFrame(columns=('Coordinates', 'Date', 'Lang'))
df_armenia = pd.DataFrame(columns=('Coordinates', 'Date', 'Lang'))
df_iran = pd.DataFrame(columns=('Coordinates', 'Date', 'Lang'))
df_iraq = pd.DataFrame(columns=('Coordinates', 'Date', 'Lang'))

for el,len,date in zip(coordinates_list, languages_list, dates_list):

    point = Point(el[1], el[0]) # create point from coordinates list

    

    if(greece_polygon.contains(point)): # check if polygon contains point
        greece_tweets+=1
        new_row = pd.Series([[el[0], el[1]], date, len], index=['Coordinates', 'Date', 'Lang'])
        df_greece = df_greece.append(new_row, ignore_index=True)
        if(len in greece_tweets_lang) :
            greece_tweets_lang[len] += 1
        else:
            greece_tweets_lang['other'] += 1

        if len in total_tweets_lang:
            total_tweets_lang[len] +=1

        continue

    if(georgia_polygon.contains(point)):
        georgia_tweets+=1
        new_row = pd.Series([[el[0], el[1]], date, len], index=['Coordinates', 'Date', 'Lang'])
        df_georgia = df_georgia.append(new_row, ignore_index=True)
        if(len in georgia_tweets_lang) :
            georgia_tweets_lang[len] += 1
        else:
            georgia_tweets_lang['other'] += 1

        if len in total_tweets_lang:
            total_tweets_lang[len] +=1
            
        continue

    if(syria_polygon.contains(point)):
        syria_tweets+=1
        new_row = pd.Series([[el[0], el[1]], date, len], index=['Coordinates', 'Date', 'Lang'])
        df_syria = df_syria.append(new_row, ignore_index=True)
        if(len in syria_tweets_lang) :
            syria_tweets_lang[len] += 1
        else:
            syria_tweets_lang['other'] += 1
        
        if len in total_tweets_lang:
            total_tweets_lang[len] +=1
            
        continue

    if(bulgaria_polygon.contains(point)):
        bulgaria_tweets+=1
        new_row = pd.Series([[el[0], el[1]], date, len], index=['Coordinates', 'Date', 'Lang'])
        df_bulgaria = df_bulgaria.append(new_row, ignore_index=True)
        if(len in bulgaria_tweets_lang) :
            bulgaria_tweets_lang[len] += 1
        else:
            bulgaria_tweets_lang['other'] += 1
        
        if len in total_tweets_lang:
            total_tweets_lang[len] +=1
            
        continue

    if(armenia_polygon.contains(point)):
        armenia_tweets+=1
        new_row = pd.Series([[el[0], el[1]], date, len], index=['Coordinates', 'Date', 'Lang'])
        df_armenia = df_armenia.append(new_row, ignore_index=True)
        if(len in armenia_tweets_lang) :
            armenia_tweets_lang[len] += 1
        else:
            armenia_tweets_lang['other'] += 1
        
        if len in total_tweets_lang:
            total_tweets_lang[len] +=1
            
        continue

    if(iran_polygon.contains(point)):
        iran_tweets+=1
        new_row = pd.Series([[el[0], el[1]], date, len], index=['Coordinates', 'Date', 'Lang'])
        df_iran = df_iran.append(new_row, ignore_index=True)
        if(len in iran_tweets_lang) :
            iran_tweets_lang[len] += 1
        else:
            iran_tweets_lang['other'] += 1
        
        if len in total_tweets_lang:
            total_tweets_lang[len] +=1
            
        continue

    if(iraq_polygon.contains(point)):
        iraq_tweets+=1
        new_row = pd.Series([[el[0], el[1]], date, len], index=['Coordinates', 'Date', 'Lang'])
        df_iraq = df_iraq.append(new_row, ignore_index=True)
        if(len in iraq_tweets_lang) :
            iraq_tweets_lang[len] += 1
        else:
            iraq_tweets_lang['other'] += 1
        
        if len in total_tweets_lang:
            total_tweets_lang[len] +=1
            
        continue
#Create the dataframe to contains all the stats

#[greece_tweets_lang['ar'] , georgia_tweets_lang['ar'], syria_tweets_lang['ar'], bulgaria_tweets_lang['ar'], armenia_tweets_lang['ar'], iran_tweets_lang['ar'], iraq_tweets_lang['ar']]

#print(df_greece)

df_tot = pd.DataFrame()
df_tot['Language'] = ["Arab","Turkish", "English", 
                   "Greek" , "Armenian" , #"Serbian", 
                   "Georgian" , "Persian", "Spanish",
                   "Slovenian","German","Romanian",
                   "Hungarian","Czechoslovak","Dutch",
                   "Italian","Russian","Chinese",
                   "Polish",
                   #"Punjabi",
                    "Hebrew",
                   "Sorani Kurdish",
                   #"Pashto",
                   "Vietnamese","French",
                     #"Urdu",
                     "Portuguese","Finnish",
                     "Norwegian","Danish",
                     #"Sindhi",
                     "Japanese","Catalan","EU","Hindi",
                     "Swedish","Ukrainian",
                     #"Korean",
                     "Latvian","Icelandic","Lithuanian",
                     "Indonesian","Welsh","Estonian",
                     "Haitian","Filipinine", "Bulgarian",
                      #"Thai", "Malayalam","Uyghur","Bengali", "Marathi",
                      "Undefined"]
df_tot['Tweet Amount'] = list(total_tweets_lang.values())
#df_tot['Total'] = [greece_tweets + georgia_tweets + syria_tweets + bulgaria_tweets + armenia_tweets + iran_tweets + iraq_tweets]



df_stats = pd.DataFrame()
df_stats['Border'] = ['Greece', 'Georgia', 'Syria', 'Bulgaria', 'Armenia', 'Iran', 'Iraq']
df_stats['Total_Tweets'] = [greece_tweets, georgia_tweets, syria_tweets, bulgaria_tweets, armenia_tweets, iran_tweets, iraq_tweets]
df_stats['Arab_Tweets'] =[greece_tweets_lang['ar'] , georgia_tweets_lang['ar'], syria_tweets_lang['ar'], bulgaria_tweets_lang['ar'], armenia_tweets_lang['ar'], iran_tweets_lang['ar'], iraq_tweets_lang['ar']] 
df_stats['English_Tweets'] = [greece_tweets_lang['en'] , georgia_tweets_lang['en'], syria_tweets_lang['en'], bulgaria_tweets_lang['en'], armenia_tweets_lang['en'], iran_tweets_lang['en'], iraq_tweets_lang['en']]
df_stats['Turk_Tweets'] = [greece_tweets_lang['tr'] , georgia_tweets_lang['tr'], syria_tweets_lang['tr'], bulgaria_tweets_lang['tr'], armenia_tweets_lang['tr'], iran_tweets_lang['tr'], iraq_tweets_lang['tr']]
df_stats['Greek_Tweets'] =[greece_tweets_lang['el'] , georgia_tweets_lang['el'], syria_tweets_lang['el'], bulgaria_tweets_lang['el'], armenia_tweets_lang['el'], iran_tweets_lang['el'], iraq_tweets_lang['el']]
df_stats['Armenian_Tweets'] = [greece_tweets_lang['hy'] , georgia_tweets_lang['hy'], syria_tweets_lang['hy'], bulgaria_tweets_lang['hy'], armenia_tweets_lang['hy'], iran_tweets_lang['hy'], iraq_tweets_lang['hy']]
df_stats['Georgian_Tweets'] = [greece_tweets_lang['ka'] , georgia_tweets_lang['ka'], syria_tweets_lang['ka'], bulgaria_tweets_lang['ka'], armenia_tweets_lang['ka'], iran_tweets_lang['ka'], iraq_tweets_lang['ka']]
df_stats['Bulgarian_Tweets'] = [greece_tweets_lang['bg'] , georgia_tweets_lang['bg'], syria_tweets_lang['bg'], bulgaria_tweets_lang['bg'], armenia_tweets_lang['bg'], iran_tweets_lang['bg'], iraq_tweets_lang['bg']]
#df_stats['Serbian_Tweets'] = [greece_tweets_lang['sr'] , georgia_tweets_lang['sr'], syria_tweets_lang['sr'], bulgaria_tweets_lang['sr'], armenia_tweets_lang['sr'], iran_tweets_lang['sr'], iraq_tweets_lang['sr']]
df_stats['Persian_Tweets'] = [greece_tweets_lang['fa'] , georgia_tweets_lang['fa'], syria_tweets_lang['fa'], bulgaria_tweets_lang['fa'], armenia_tweets_lang['fa'], iran_tweets_lang['fa'], iraq_tweets_lang['fa']]
df_stats['Slovenian_Tweets'] = [greece_tweets_lang['sl'] , georgia_tweets_lang['sl'], syria_tweets_lang['sl'], bulgaria_tweets_lang['sl'], armenia_tweets_lang['sl'], iran_tweets_lang['sl'], iraq_tweets_lang['sl']]
df_stats['Spanish_Tweets'] = [greece_tweets_lang['es'] , georgia_tweets_lang['es'], syria_tweets_lang['es'], bulgaria_tweets_lang['es'], armenia_tweets_lang['es'], iran_tweets_lang['es'], iraq_tweets_lang['es']]
df_stats['German_Tweets'] = [greece_tweets_lang['de'] , georgia_tweets_lang['de'], syria_tweets_lang['de'], bulgaria_tweets_lang['de'], armenia_tweets_lang['de'], iran_tweets_lang['de'], iraq_tweets_lang['de']]
df_stats['Romanian_Tweets'] = [greece_tweets_lang['ro'] , georgia_tweets_lang['ro'], syria_tweets_lang['ro'], bulgaria_tweets_lang['ro'], armenia_tweets_lang['ro'], iran_tweets_lang['ro'], iraq_tweets_lang['ro']]
df_stats['Hungarian_Tweets'] = [greece_tweets_lang['hu'] , georgia_tweets_lang['hu'], syria_tweets_lang['hu'], bulgaria_tweets_lang['hu'], armenia_tweets_lang['hu'], iran_tweets_lang['hu'], iraq_tweets_lang['hu']]
df_stats['Czechoslovak_Tweets'] =  [greece_tweets_lang['cs'] , georgia_tweets_lang['cs'], syria_tweets_lang['cs'], bulgaria_tweets_lang['cs'], armenia_tweets_lang['cs'], iran_tweets_lang['cs'], iraq_tweets_lang['cs']]
df_stats['Dutch_Belgian_Tweets'] = [greece_tweets_lang['nl'] , georgia_tweets_lang['nl'], syria_tweets_lang['nl'], bulgaria_tweets_lang['nl'], armenia_tweets_lang['nl'], iran_tweets_lang['nl'], iraq_tweets_lang['nl']]
df_stats['Italian_Tweets'] = [greece_tweets_lang['it'] , georgia_tweets_lang['it'], syria_tweets_lang['it'], bulgaria_tweets_lang['it'], armenia_tweets_lang['it'], iran_tweets_lang['it'], iraq_tweets_lang['it']]
df_stats['Russian_Tweets'] = [greece_tweets_lang['ru'] , georgia_tweets_lang['ru'], syria_tweets_lang['ru'], bulgaria_tweets_lang['ru'], armenia_tweets_lang['ru'], iran_tweets_lang['ru'], iraq_tweets_lang['ru']]
df_stats['Chinese_Tweets'] = [greece_tweets_lang['zh'] , georgia_tweets_lang['zh'], syria_tweets_lang['zh'], bulgaria_tweets_lang['zh'], armenia_tweets_lang['zh'], iran_tweets_lang['zh'], iraq_tweets_lang['zh']]
df_stats['Polish_Tweets'] = [greece_tweets_lang['pl'] , georgia_tweets_lang['pl'], syria_tweets_lang['pl'], bulgaria_tweets_lang['pl'], armenia_tweets_lang['pl'], iran_tweets_lang['pl'], iraq_tweets_lang['pl']]
#df_stats['Punjabi_Indian_Tweets'] = [greece_tweets_lang['pa'] , georgia_tweets_lang['pa'], syria_tweets_lang['pa'], bulgaria_tweets_lang['pa'], armenia_tweets_lang['pa'], iran_tweets_lang['pa'], iraq_tweets_lang['pa']]
df_stats['Hebrew_Tweets'] = [greece_tweets_lang['iw'] , georgia_tweets_lang['iw'], syria_tweets_lang['iw'], bulgaria_tweets_lang['iw'], armenia_tweets_lang['iw'], iran_tweets_lang['iw'], iraq_tweets_lang['iw']]
df_stats['Sorani_Kurdish_Tweets'] =[greece_tweets_lang['ckb'] , georgia_tweets_lang['ckb'], syria_tweets_lang['ckb'], bulgaria_tweets_lang['ckb'], armenia_tweets_lang['ckb'], iran_tweets_lang['ckb'], iraq_tweets_lang['ckb']]
#df_stats['Pashto_Tweets'] = [greece_tweets_lang['ps'] , georgia_tweets_lang['ps'], syria_tweets_lang['ps'], bulgaria_tweets_lang['ps'], armenia_tweets_lang['ps'], iran_tweets_lang['ps'], iraq_tweets_lang['ps']]
df_stats['Vietnamese_Tweets'] = [greece_tweets_lang['vi'] , georgia_tweets_lang['vi'], syria_tweets_lang['vi'], bulgaria_tweets_lang['vi'], armenia_tweets_lang['vi'], iran_tweets_lang['vi'], iraq_tweets_lang['vi']]
df_stats['French_Tweets'] = [greece_tweets_lang['fr'] , georgia_tweets_lang['fr'], syria_tweets_lang['fr'], bulgaria_tweets_lang['fr'], armenia_tweets_lang['fr'], iran_tweets_lang['fr'], iraq_tweets_lang['fr']]
#df_stats['Urdu_Tweets'] = [greece_tweets_lang['ur'] , georgia_tweets_lang['ur'], syria_tweets_lang['ur'], bulgaria_tweets_lang['ur'], armenia_tweets_lang['ur'], iran_tweets_lang['ur'], iraq_tweets_lang['ur']]
df_stats['Portuguese_Tweets'] = [greece_tweets_lang['pt'] , georgia_tweets_lang['pt'], syria_tweets_lang['pt'], bulgaria_tweets_lang['pt'], armenia_tweets_lang['pt'], iran_tweets_lang['pt'], iraq_tweets_lang['pt']]
df_stats['Finnish_Tweets'] = [greece_tweets_lang['fi'] , georgia_tweets_lang['fi'], syria_tweets_lang['fi'], bulgaria_tweets_lang['fi'], armenia_tweets_lang['fi'], iran_tweets_lang['fi'], iraq_tweets_lang['fi']]
df_stats['Norwegian_Tweets'] = [greece_tweets_lang['no'] , georgia_tweets_lang['no'], syria_tweets_lang['no'], bulgaria_tweets_lang['no'], armenia_tweets_lang['no'], iran_tweets_lang['no'], iraq_tweets_lang['no']]
df_stats['Danish_Tweets'] = [greece_tweets_lang['da'] , georgia_tweets_lang['da'], syria_tweets_lang['da'], bulgaria_tweets_lang['da'], armenia_tweets_lang['da'], iran_tweets_lang['da'], iraq_tweets_lang['da']]

df_stats['Japanese_Tweets'] = [greece_tweets_lang['ja'] , georgia_tweets_lang['ja'], syria_tweets_lang['ja'], bulgaria_tweets_lang['ja'], armenia_tweets_lang['ja'], iran_tweets_lang['ja'], iraq_tweets_lang['ja']]
df_stats['Catalan_Tweets'] = [greece_tweets_lang['ca'] , georgia_tweets_lang['ca'], syria_tweets_lang['ca'], bulgaria_tweets_lang['ca'], armenia_tweets_lang['ca'], iran_tweets_lang['ca'], iraq_tweets_lang['ca']]
df_stats['EU_Tweets'] = [greece_tweets_lang['eu'] , georgia_tweets_lang['eu'], syria_tweets_lang['eu'], bulgaria_tweets_lang['eu'], armenia_tweets_lang['eu'], iran_tweets_lang['eu'], iraq_tweets_lang['eu']]
df_stats['Indian_Tweets'] = [greece_tweets_lang['hi'] , georgia_tweets_lang['hi'], syria_tweets_lang['hi'], bulgaria_tweets_lang['hi'], armenia_tweets_lang['hi'], iran_tweets_lang['hi'], iraq_tweets_lang['hi']]
df_stats['Swedish_Tweets'] = [greece_tweets_lang['sv'] , georgia_tweets_lang['sv'], syria_tweets_lang['sv'], bulgaria_tweets_lang['sv'], armenia_tweets_lang['sv'], iran_tweets_lang['sv'], iraq_tweets_lang['sv']]

df_stats['Ukrainian_Tweets'] = [greece_tweets_lang['uk'] , georgia_tweets_lang['uk'], syria_tweets_lang['uk'], bulgaria_tweets_lang['uk'], armenia_tweets_lang['uk'], iran_tweets_lang['uk'], iraq_tweets_lang['uk']]
#df_stats['Korean_Tweets'] = [greece_tweets_lang['ko'] , georgia_tweets_lang['ko'], syria_tweets_lang['ko'], bulgaria_tweets_lang['ko'], armenia_tweets_lang['ko'], iran_tweets_lang['ko'], iraq_tweets_lang['ko']]
df_stats['Latvian_Tweets'] = [greece_tweets_lang['lv'] , georgia_tweets_lang['lv'], syria_tweets_lang['lv'], bulgaria_tweets_lang['lv'], armenia_tweets_lang['lv'], iran_tweets_lang['lv'], iraq_tweets_lang['lv']]
df_stats['Icelandic_Tweets'] = [greece_tweets_lang['is'] , georgia_tweets_lang['is'], syria_tweets_lang['is'], bulgaria_tweets_lang['is'], armenia_tweets_lang['is'], iran_tweets_lang['is'], iraq_tweets_lang['is']]
df_stats['Lithuanian_Tweets'] = [greece_tweets_lang['lt'] , georgia_tweets_lang['lt'], syria_tweets_lang['lt'], bulgaria_tweets_lang['lt'], armenia_tweets_lang['lt'], iran_tweets_lang['lt'], iraq_tweets_lang['lt']]

df_stats['Indonesian_Tweets'] = [greece_tweets_lang['in'] , georgia_tweets_lang['in'], syria_tweets_lang['in'], bulgaria_tweets_lang['in'], armenia_tweets_lang['in'], iran_tweets_lang['in'], iraq_tweets_lang['in']]
df_stats['Welsh_Tweets'] = [greece_tweets_lang['cy'] , georgia_tweets_lang['cy'], syria_tweets_lang['cy'], bulgaria_tweets_lang['cy'], armenia_tweets_lang['cy'], iran_tweets_lang['cy'], iraq_tweets_lang['cy']]
df_stats['Estonian_Tweets'] = [greece_tweets_lang['et'] , georgia_tweets_lang['et'], syria_tweets_lang['et'], bulgaria_tweets_lang['et'], armenia_tweets_lang['et'], iran_tweets_lang['et'], iraq_tweets_lang['et']]
df_stats['Haitian_Tweets'] = [greece_tweets_lang['ht'] , georgia_tweets_lang['ht'], syria_tweets_lang['ht'], bulgaria_tweets_lang['ht'], armenia_tweets_lang['ht'], iran_tweets_lang['ht'], iraq_tweets_lang['ht']]
df_stats['Tagalog(Filipine)_Tweets'] = [greece_tweets_lang['tl'] , georgia_tweets_lang['tl'], syria_tweets_lang['tl'], bulgaria_tweets_lang['tl'], armenia_tweets_lang['tl'], iran_tweets_lang['tl'], iraq_tweets_lang['tl']]

#df_stats['Thai_Tweets'] = [greece_tweets_lang['th'] , georgia_tweets_lang['th'], syria_tweets_lang['th'], bulgaria_tweets_lang['th'], armenia_tweets_lang['th'], iran_tweets_lang['th'], iraq_tweets_lang['th']]
#df_stats['Malayalam_Tweets'] = [greece_tweets_lang['ml'] , georgia_tweets_lang['ml'], syria_tweets_lang['ml'], bulgaria_tweets_lang['ml'], armenia_tweets_lang['ml'], iran_tweets_lang['ml'], iraq_tweets_lang['ml']]
#df_stats['Uyghur_Tweets'] = [greece_tweets_lang['ug'] , georgia_tweets_lang['ug'], syria_tweets_lang['ug'], bulgaria_tweets_lang['ug'], armenia_tweets_lang['ug'], iran_tweets_lang['ug'], iraq_tweets_lang['ug']]
#df_stats['Begali_Tweets'] = [greece_tweets_lang['bn'] , georgia_tweets_lang['bn'], syria_tweets_lang['bn'], bulgaria_tweets_lang['bn'], armenia_tweets_lang['bn'], iran_tweets_lang['bn'], iraq_tweets_lang['bn']]
#df_stats['Marathi_Tweets'] = [greece_tweets_lang['mr'] , georgia_tweets_lang['mr'], syria_tweets_lang['mr'], bulgaria_tweets_lang['mr'], armenia_tweets_lang['mr'], iran_tweets_lang['mr'], iraq_tweets_lang['mr']]

#df_stats['Sindhi_Tweets'] = [greece_tweets_lang['sd'] , georgia_tweets_lang['sd'], syria_tweets_lang['sd'], bulgaria_tweets_lang['sd'], armenia_tweets_lang['sd'], iran_tweets_lang['sd'], iraq_tweets_lang['sd']]
df_stats['Undefined_Tweets'] = [greece_tweets_lang['und'] , georgia_tweets_lang['und'], syria_tweets_lang['und'], bulgaria_tweets_lang['und'], armenia_tweets_lang['und'], iran_tweets_lang['und'], iraq_tweets_lang['und']]
#df_stats['Others_Tweets'] = [greece_tweets_lang['other'] , georgia_tweets_lang['other'], syria_tweets_lang['other'], bulgaria_tweets_lang['other'], armenia_tweets_lang['other'], iran_tweets_lang['other'], iraq_tweets_lang['other']]

#Dataframe con statistiche totali per ogni lingua
out_tot = open("DFStats/stats_border_total.pkl", "wb")
df_tot.to_pickle(out_tot)
out_tot.close()

#Dataframe di ogni confine contenente coordinate, data del tweet e lingua, per plot sulle lingue nel tempo
out_gr = open("DFBorders/dataFrame_greece.pkl", "wb")
df_greece.to_pickle(out_gr)
out_gr.close()

out_ge = open("DFBorders/dataFrame_georgia.pkl", "wb")
df_georgia.to_pickle(out_ge)
out_ge.close() 

out_s = open("DFBorders/dataFrame_syria.pkl", "wb")
df_syria.to_pickle(out_s)
out_s.close()

out_b = open("DFBorders/dataFrame_bulgaria.pkl", "wb")
df_bulgaria.to_pickle(out_b)
out_b.close()

out_ar = open("DFBorders/dataFrame_armenia.pkl", "wb")
df_armenia.to_pickle(out_ar)
out_ar.close()

out_irn = open("DFBorders/dataFrame_iran.pkl", "wb")
df_iran.to_pickle(out_irn)
out_irn.close()

out_irq = open("DFBorders/dataFrame_iraq.pkl", "wb")
df_iraq.to_pickle(out_irq)
out_irq.close()

#Dataframe con le statistiche per eventuali grafici (vedi : lang_stat_plot.py)
out_f = open("dataFrame_lang_stats_dict.pkl", "wb")

out_csv = open("borders_language_statistics.csv", "w")

df_stats.to_csv(out_csv, encoding='utf-8', index=False)

df_stats.to_pickle(out_f)

out_csv.close()

out_f.close()
