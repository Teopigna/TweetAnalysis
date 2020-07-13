import csv
import pandas as pd

df_border = pd.read_pickle("DFBorders/dataFrame_iraq.pkl")
'''
df_border = df_border.append(pd.read_pickle("DFBorders/dataFrame_syria.pkl"))
df_border = df_border.append(pd.read_pickle("DFBorders/dataFrame_armenia.pkl"))
df_border = df_border.append(pd.read_pickle("DFBorders/dataFrame_bulgaria.pkl"))
df_border = df_border.append(pd.read_pickle("DFBorders/dataFrame_greece.pkl"))
df_border = df_border.append(pd.read_pickle("DFBorders/dataFrame_iran.pkl"))
df_border = df_border.append(pd.read_pickle("DFBorders/dataFrame_iraq.pkl"))
'''
print(df_border)


#print(df_border)
daily_total_tweets = { 
    'Mar 01' : 0,
    'Mar 02' : 0,
    'Mar 03' : 0,
    'Mar 04' : 0,
    'Mar 05' : 0,
    'Mar 06' : 0,
    'Mar 07' : 0,
    'Mar 08' : 0,
    'Mar 09' : 0,
    'Mar 10' : 0,
    'Mar 11' : 0,
    'Mar 12' : 0,
    'Mar 13' : 0,
    'Mar 14' : 0,
    'Mar 15' : 0,
    'Mar 16' : 0,
    'Mar 17' : 0,
    'Mar 18' : 0,
    'Mar 19' : 0,
    'Mar 20' : 0,
    'Mar 21' : 0,
    'Mar 22' : 0,
    'Mar 23' : 0,
    'Mar 24' : 0,
    'Mar 25' : 0,
    'Mar 26' : 0,
    'Mar 27' : 0,
    'Mar 28' : 0,
    'Mar 29' : 0,
    'Mar 30' : 0,
    'Mar 31' : 0,
    'Apr 01' : 0,
    'Apr 02' : 0,
    'Apr 03' : 0, 
    'Apr 04' : 0,
    'Apr 05' : 0,
    'Apr 06' : 0,
    'Apr 07' : 0,
    'Apr 08' : 0,
    'Apr 09' : 0,
    'Apr 10' : 0,
    'Apr 11' : 0,
    'Apr 12' : 0,
    'Apr 13' : 0,
    'Apr 14' : 0,
    'Apr 15' : 0,
    'Apr 16' :0,
    'Apr 17' : 0,
    'Apr 18' : 0,
    'Apr 19' : 0,
    'Apr 20' : 0,
    'Apr 21' : 0,
    'Apr 22' : 0, 
    'Apr 23' : 0,
    'Apr 24' : 0,
    'Apr 25' : 0,
    'Apr 26' : 0,
    'Apr 27' : 0,
    'Apr 28' : 0,
    'Apr 29' : 0,
    'Apr 30' : 0,
    'May 01' : 0,
    'May 02' : 0,
    'May 03' : 0,
    'May 04' : 0,
    'May 05' : 0,
    'May 06' : 0,
    'May 07' : 0,
    'May 08' : 0,
    'May 09' : 0,
    'May 10' : 0,
    'May 11' : 0,
    'May 12' : 0,
    'May 13' : 0,
    'May 14' : 0,
    'May 15' : 0,
    'May 16' : 0,
    'May 17' : 0,
    'May 18' : 0,
    'May 19' : 0,
    'May 20' : 0,
    'May 21' : 0,
    'May 22' : 0,
    'May 23' : 0,
    'May 24' : 0,
    'May 25' : 0,
    'May 26' : 0,
    'May 27' : 0,
    'May 28' : 0,
    'May 29' : 0
}

day_index = ['Mar 01','Mar 02','Mar 03','Mar 04','Mar 05',
             'Mar 06','Mar 07','Mar 08','Mar 09','Mar 10',
             'Mar 11','Mar 12','Mar 13','Mar 14','Mar 15',
             'Mar 16','Mar 17','Mar 18','Mar 19','Mar 20',
             'Mar 21','Mar 22','Mar 23','Mar 24','Mar 25',
             'Mar 26','Mar 27','Mar 28','Mar 29','Mar 30',
             'Mar 31','Apr 01','Apr 02','Apr 03','Apr 04',
             'Apr 05','Apr 06','Apr 07','Apr 08','Apr 09',
             'Apr 10','Apr 11','Apr 12','Apr 13','Apr 14',
             'Apr 15','Apr 16','Apr 17','Apr 18','Apr 19',
             'Apr 20','Apr 21','Apr 22','Apr 23','Apr 24',
             'Apr 25','Apr 26','Apr 27','Apr 28','Apr 29',
             'Apr 30','May 01','May 02','May 03','May 04',
             'May 05','May 06','May 07','May 08','May 09',
             'May 10','May 11','May 12','May 13','May 14',
             'May 15','May 16','May 17','May 18','May 19',
             'May 20','May 21','May 22','May 23','May 24',
             'May 25','May 26','May 27','May 28','May 29'
            ]


arab_tweets = [0] * 90
turk_tweets = [0] * 90
eng_tweets = [0] * 90
greek_tweets = [0] * 90
armenian_tweets = [0] * 90 
#serbian_tweets =[0] * 90
georgian_tweets =[0] * 90
persian_tweets =[0] * 90
spanish_tweets =[0] * 90
sloven_tweets =[0] * 90
german_tweets =[0] * 90
romanian_tweets =[0] * 90
hungarian_tweets =[0] * 90
ceco_tweets =[0] * 90
dutch_tweets =[0] * 90
italian_tweets =[0] * 90
russian_tweets =[0] * 90
chinese_tweets =[0] * 90
polish_tweets =[0] * 90
#punjabi_tweets =[0] * 90
hebrew_tweets =[0] * 90
soraniKurdish_tweets =[0] * 90
#pashto_tweets =[0] * 90
vietnamese_tweets =[0] * 90
french_tweets =[0] * 90
#urdu_tweets =[0] * 90
portuguese_tweets =[0] * 90
finnish_tweets =[0] * 90
norvegian_tweets =[0] * 90
danish_tweets =[0] * 90
#sindhi_tweets =[0] * 90
#thai_tweets =[0] * 90
japanese_tweets =[0] * 90
catalan_tweets =[0] * 90
EU_tweets =[0] * 90
hindi_tweets =[0] * 90
svedish_tweets =[0] * 90
ukranian_tweets =[0] * 90
#korean_tweets =[0] * 90
latvian_tweets =[0] * 90
icelandic_tweets =[0] * 90
lituanian_tweets = [0] * 90
indonesian_tweets =[0] * 90
welsh_tweets =[0] * 90
estonian_tweets =[0] * 90
haitian_tweets =[0] * 90
filipine_tweets =[0] * 90
bulgarian_tweets =[0] * 90
#malayalam_tweets =[0] * 90
#uyghur_tweets =[0] * 90
#bengali_tweets =[0] * 90
#marathi_tweets =[0] * 90
undefined_tweets=[0] * 90

lang_stats = {
    'ar' : arab_tweets,
    'tr' : turk_tweets,
    'en' : eng_tweets, 
    'el' : greek_tweets,
    'hy' : armenian_tweets,
    #'sr' : serbian_tweets,
    'ka' : georgian_tweets,
    'fa' : persian_tweets,
    'es' : spanish_tweets,
    'sl' : sloven_tweets,
    'de' : german_tweets,
    'ro' : romanian_tweets,
    'hu' : hungarian_tweets,
    'cs' : ceco_tweets,
    'nl' : dutch_tweets,
    'it' : italian_tweets,
    'ru' : russian_tweets,
    'zh' : chinese_tweets,
    'pl' : polish_tweets,
    #'pa' : punjabi_tweets,
    'iw' : hebrew_tweets, 
    'ckb' : soraniKurdish_tweets,
    #'ps' : pashto_tweets,
    'vi' : vietnamese_tweets,
    'fr' : french_tweets,
    #'ur' : urdu_tweets,
    'pt' : portuguese_tweets,
    'fi' : finnish_tweets,
    'no' : norvegian_tweets,
    'da' : danish_tweets,
    #'sd' : sindhi_tweets,
    'ja' : japanese_tweets,
    'ca' : catalan_tweets,
    'eu' : EU_tweets,
    'hi' : hindi_tweets,
    'sv' : svedish_tweets,
    'uk' : ukranian_tweets,
    #'ko' : korean_tweets,
    'lv' : latvian_tweets,
    'is' : icelandic_tweets,
    'lt' : lituanian_tweets,
    'in' : indonesian_tweets,
    'cy' : welsh_tweets,
    'et' : estonian_tweets,
    'ht' : haitian_tweets,
    'tl' : filipine_tweets,
    'bg' : bulgarian_tweets,
    #'th' : thai_tweets,
    #'ml' : malayalam_tweets,
    #'ug' : uyghur_tweets,
    #'bn' : bengali_tweets,
    #'mr' : marathi_tweets,
    'und' : undefined_tweets
}

dates_list = list(df_border.Date)

lang_list = list(df_border.Lang)


for lan, day in zip(lang_list, dates_list):
    if(lan == 'ko'):
        continue
    lang_stats[lan][day_index.index(day)] += 1
    daily_total_tweets[day] += 1

lang_lists = []
keyslist = []

for key, value in lang_stats.items():
    temp = lang_stats[key]
    lang_lists.append(temp)
    keyslist.append(key)


y=["Arab","Turkish", "English", 
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
z= lang_lists
x=day_index


df_stats = pd.DataFrame()
df_stats['Day'] = day_index
df_stats['Undefined'] = lang_stats['und']
df_stats['Arab'] = lang_stats['ar']
df_stats['Turkish'] = lang_stats['tr']
df_stats['English'] = lang_stats['en']
df_stats['Greek'] = lang_stats['el']
df_stats['Armenian'] = lang_stats['hy']
df_stats['Georgian'] = lang_stats['ka']
df_stats['Bulgarian'] = lang_stats['bg']
df_stats['Persian'] = lang_stats['fa']
df_stats['Indonesian'] = lang_stats['in']
df_stats['Spanish'] = lang_stats['es']
df_stats['Slovenian'] = lang_stats['sl']
df_stats['German'] = lang_stats['de']
df_stats['Romanian'] = lang_stats['ro']
df_stats['Hungarian'] = lang_stats['hu']
df_stats['Czechoslovak'] = lang_stats['cs']
df_stats['Dutch'] = lang_stats['nl']
df_stats['Italian'] = lang_stats['it']
df_stats['Russian'] = lang_stats['ru']
df_stats['Chinese'] = lang_stats['zh']
df_stats['Polish'] = lang_stats['pl']
df_stats['Hebrew'] = lang_stats['iw']
df_stats['Sorani Kurdish'] = lang_stats['ckb']
df_stats['Vietnamese'] = lang_stats['vi']
df_stats['French'] = lang_stats['fr']
df_stats['Portuguese'] = lang_stats['pt']
df_stats['Finnish'] = lang_stats['fi']
df_stats['Norwegian'] = lang_stats['no']
df_stats['Danish'] = lang_stats['da']
df_stats['Japanese'] = lang_stats['ja']
df_stats['Catalan'] = lang_stats['ca']
df_stats['EU'] = lang_stats['eu']
df_stats['Hindi'] = lang_stats['hi']
df_stats['Swedish'] = lang_stats['sv']
df_stats['Ukrainian'] = lang_stats['uk']
df_stats['Latvian'] = lang_stats['lv']
df_stats['Icelandic'] = lang_stats['is']
df_stats['Lithuanian'] = lang_stats['lt']
df_stats['Welsh'] = lang_stats['cy']
df_stats['Estonian'] = lang_stats['et']
df_stats['Haitian'] = lang_stats['ht']
df_stats['Filipine'] = lang_stats['tl']


out_csv = open("iraq_daily_statistics.csv", "w")

df_stats.to_csv(out_csv, encoding='utf-8', index=False)

out_csv.close()