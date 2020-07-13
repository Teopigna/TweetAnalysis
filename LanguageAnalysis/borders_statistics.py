import pandas as pd

df_georgia = pd.read_pickle("DFBorders/dataFrame_georgia.pkl")
df_greece = pd.read_pickle("DFBorders/dataFrame_greece.pkl")
df_syria = pd.read_pickle("DFBorders/dataFrame_syria.pkl")
df_iran = pd.read_pickle("DFBorders/dataFrame_iran.pkl")
df_iraq = pd.read_pickle("DFBorders/dataFrame_iraq.pkl")
df_armenia = pd.read_pickle("DFBorders/dataFrame_armenia.pkl")
df_bulgaria = pd.read_pickle("DFBorders/dataFrame_bulgaria.pkl")

#Auxiliary set for dictionaries (len : tweet_amount)



lang_dict = { 
    'ar' : 'Arab',
    'tr' : 'Turkish',
    'en' : 'English', 
    'el' : 'Greek',
    'hy' : 'Armenian',
    'sr' : 'Serbian',
    'ka' : 'Georgian',
    'fa' : 'Persian',
    'es' : 'Spanish',
    'sl' : 'Slovenian',
    'de' : 'German',
    'ro' : 'Romanian',
    'hu' : 'Hungarian',
    'cs' : 'Czechoslovak',
    'nl' : 'Dutch',
    'it' :'Italian',
    'ru' : 'Russian',
    'zh' : 'Chinese',
    'pl' : 'Polish',
    'pa' : 'Punjabi',
    'iw' : 'Hebrew', 
    'ckb' : 'Sorani Kurdish',
    'ps' : 'Pashto',
    'vi' : 'Vietnamese',
    'fr' : 'French',
    'ur' : 'Urdu',
    'pt' : 'Portuguese',
    'fi' : 'Finnish',
    'no' : 'Norwegian',
    'da' : 'Danish',
    'sd' : 'Sindhi',
    'ja' : 'Japanese',
    'ca' : 'Catalan',
    'eu' : 'EU',
    'hi' : 'Hindi',
    'sv' : 'Swedish',
    'uk' : 'Ukranian',
    'ko' : 'Korean',
    'lv' : 'Latvian',
    'is' : 'Icelandic',
    'lt' : 'Lithuanian',
    'in' : 'Indonesian',
    'cy' : 'Welsh',
    'et' : 'Estonian',
    'ht' : 'Haitian',
    'tl' : 'Filipine',
    'bg' : 'Bulgarian',
    'th' : 'Thai',
    'ml' : 'Malayalam',
    'ug' : 'Uyghur',
    'bn' : 'bn',
    'mr' : 'mr',
    'und' : 'Undefined'
}

total_mar_tweets = 0
total_mar_tweets_lang = { 
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
    'und' : 0
}

total_apr_tweets = 0
total_apr_tweets_lang = { 
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
    'und' : 0
}

total_may_tweets = 0
total_may_tweets_lang = { 
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
    'und' : 0
}

''' reset total_tweets_lang
for k in total_tweets_lang:
...     total_tweets_lang[k] = 0
'''
#Syria Analysis
#######################################################################################################
dates_list = list(df_syria.Date)

lang_list = list(df_syria.Lang)

for lan, day in zip(lang_list, dates_list):
    if 'Mar' in day:
        #total_mar_tweets += 1
        total_mar_tweets_lang[lan] += 1
    if 'Apr' in day:
        #total_apr_tweets += 1
        total_apr_tweets_lang[lan] += 1    
    if 'May' in day:
        #total_may_tweets += 1
        total_may_tweets_lang[lan] += 1    

df_stats_syria = pd.DataFrame(columns=('Language', 'TotalTweets', 'Month'))

#March count
for key, val in total_mar_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'Mar'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_syria = df_stats_syria.append(new_row ,ignore_index=True)
    
#April count
for key, val in total_apr_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'Apr'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_syria = df_stats_syria.append(new_row, ignore_index=True)
#May count
for key, val in total_may_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'May'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_syria = df_stats_syria.append(new_row,ignore_index=True)

out_s = open("DFStats/stats_syria.pkl", "wb")
df_stats_syria.to_pickle(out_s)
out_s.close()
#print(df_stats_syria)
#######################################################################################################

#Reset total_tweets monthly dictionaries for reusing it

for k in total_mar_tweets_lang:
    total_mar_tweets_lang[k] = 0

for k in total_apr_tweets_lang:
    total_apr_tweets_lang[k] = 0

for k in total_may_tweets_lang:
    total_may_tweets_lang[k] = 0

################################
#Georgia Analysis
#######################################################################################################
dates_list = list(df_georgia.Date)

lang_list = list(df_georgia.Lang)

for lan, day in zip(lang_list, dates_list):
    if 'Mar' in day:
        total_mar_tweets += 1
        total_mar_tweets_lang[lan] += 1
    if 'Apr' in day:
        total_apr_tweets += 1
        total_apr_tweets_lang[lan] += 1    
    if 'May' in day:
        total_may_tweets += 1
        total_may_tweets_lang[lan] += 1    

df_stats_georgia = pd.DataFrame(columns=('Language', 'TotalTweets', 'Month'))

#March count
for key, val in total_mar_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'Mar'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_georgia = df_stats_georgia.append(new_row ,ignore_index=True)
    
#April count
for key, val in total_apr_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'Apr'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_georgia = df_stats_georgia.append(new_row, ignore_index=True)
#May count
for key, val in total_may_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'May'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_georgia = df_stats_georgia.append(new_row,ignore_index=True)

out_s = open("DFStats/stats_georgia.pkl", "wb")
df_stats_georgia.to_pickle(out_s)
out_s.close()
#print(df_stats_georgia)
#######################################################################################################

#Reset total_tweets monthly dictionaries for reusing it

for k in total_mar_tweets_lang:
    total_mar_tweets_lang[k] = 0

for k in total_apr_tweets_lang:
    total_apr_tweets_lang[k] = 0

for k in total_may_tweets_lang:
    total_may_tweets_lang[k] = 0

################################
#Armenia Analysis
#######################################################################################################
dates_list = list(df_armenia.Date)

lang_list = list(df_armenia.Lang)

for lan, day in zip(lang_list, dates_list):
    if 'Mar' in day:
        total_mar_tweets += 1
        total_mar_tweets_lang[lan] += 1
    if 'Apr' in day:
        total_apr_tweets += 1
        total_apr_tweets_lang[lan] += 1    
    if 'May' in day:
        total_may_tweets += 1
        total_may_tweets_lang[lan] += 1    

df_stats_armenia = pd.DataFrame(columns=('Language', 'TotalTweets', 'Month'))

#March count
for key, val in total_mar_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'Mar'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_armenia = df_stats_armenia.append(new_row ,ignore_index=True)
    
#April count
for key, val in total_apr_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'Apr'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_armenia = df_stats_armenia.append(new_row, ignore_index=True)
#May count
for key, val in total_may_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'May'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_armenia = df_stats_armenia.append(new_row,ignore_index=True)

out_s = open("DFStats/stats_armenia.pkl", "wb")
df_stats_armenia.to_pickle(out_s)
out_s.close()
#print(df_stats_armenia)
#######################################################################################################

#Reset total_tweets monthly dictionaries for reusing it

for k in total_mar_tweets_lang:
    total_mar_tweets_lang[k] = 0

for k in total_apr_tweets_lang:
    total_apr_tweets_lang[k] = 0

for k in total_may_tweets_lang:
    total_may_tweets_lang[k] = 0

###############################
#Greece Analysis
#######################################################################################################
dates_list = list(df_greece.Date)

lang_list = list(df_greece.Lang)

for lan, day in zip(lang_list, dates_list):
    if 'Mar' in day:
        total_mar_tweets += 1
        total_mar_tweets_lang[lan] += 1
    if 'Apr' in day:
        total_apr_tweets += 1
        total_apr_tweets_lang[lan] += 1    
    if 'May' in day:
        total_may_tweets += 1
        total_may_tweets_lang[lan] += 1    

df_stats_greece = pd.DataFrame(columns=('Language', 'TotalTweets', 'Month'))

#March count
for key, val in total_mar_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'Mar'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_greece = df_stats_greece.append(new_row ,ignore_index=True)
    
#April count
for key, val in total_apr_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'Apr'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_greece = df_stats_greece.append(new_row, ignore_index=True)
#May count
for key, val in total_may_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'May'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_greece = df_stats_greece.append(new_row,ignore_index=True)

out_s = open("DFStats/stats_greece.pkl", "wb")
df_stats_greece.to_pickle(out_s)
out_s.close()
#print(df_stats_armenia)
#######################################################################################################

#Reset total_tweets monthly dictionaries for reusing it

for k in total_mar_tweets_lang:
    total_mar_tweets_lang[k] = 0

for k in total_apr_tweets_lang:
    total_apr_tweets_lang[k] = 0

for k in total_may_tweets_lang:
    total_may_tweets_lang[k] = 0

###############################
#Bulgaria Analysis
#######################################################################################################
dates_list = list(df_bulgaria.Date)

lang_list = list(df_bulgaria.Lang)

for lan, day in zip(lang_list, dates_list):
    if 'Mar' in day:
        total_mar_tweets += 1
        total_mar_tweets_lang[lan] += 1
    if 'Apr' in day:
        total_apr_tweets += 1
        total_apr_tweets_lang[lan] += 1    
    if 'May' in day:
        total_may_tweets += 1
        total_may_tweets_lang[lan] += 1    

df_stats_bulgaria = pd.DataFrame(columns=('Language', 'TotalTweets', 'Month'))

#March count
for key, val in total_mar_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'Mar'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_bulgaria = df_stats_bulgaria.append(new_row ,ignore_index=True)
    
#April count
for key, val in total_apr_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'Apr'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_bulgaria = df_stats_bulgaria.append(new_row, ignore_index=True)
#May count
for key, val in total_may_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'May'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_bulgaria = df_stats_bulgaria.append(new_row,ignore_index=True)

out_s = open("DFStats/stats_bulgaria.pkl", "wb")
df_stats_bulgaria.to_pickle(out_s)
out_s.close()
#print(df_stats_armenia)
#######################################################################################################

#Reset total_tweets monthly dictionaries for reusing it

for k in total_mar_tweets_lang:
    total_mar_tweets_lang[k] = 0

for k in total_apr_tweets_lang:
    total_apr_tweets_lang[k] = 0

for k in total_may_tweets_lang:
    total_may_tweets_lang[k] = 0

###############################
#Iran Analysis
#######################################################################################################
dates_list = list(df_iran.Date)

lang_list = list(df_iran.Lang)

for lan, day in zip(lang_list, dates_list):
    if 'Mar' in day:
        total_mar_tweets += 1
        total_mar_tweets_lang[lan] += 1
    if 'Apr' in day:
        total_apr_tweets += 1
        total_apr_tweets_lang[lan] += 1    
    if 'May' in day:
        total_may_tweets += 1
        total_may_tweets_lang[lan] += 1    

df_stats_iran = pd.DataFrame(columns=('Language', 'TotalTweets', 'Month'))

#March count
for key, val in total_mar_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'Mar'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_iran = df_stats_iran.append(new_row ,ignore_index=True)
    
#April count
for key, val in total_apr_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'Apr'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_iran = df_stats_iran.append(new_row, ignore_index=True)
#May count
for key, val in total_may_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'May'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_iran = df_stats_iran.append(new_row,ignore_index=True)

out_s = open("DFStats/stats_iran.pkl", "wb")
df_stats_iran.to_pickle(out_s)
out_s.close()
#print(df_stats_armenia)
#######################################################################################################

#Reset total_tweets monthly dictionaries for reusing it

for k in total_mar_tweets_lang:
    total_mar_tweets_lang[k] = 0

for k in total_apr_tweets_lang:
    total_apr_tweets_lang[k] = 0

for k in total_may_tweets_lang:
    total_may_tweets_lang[k] = 0

###############################

#Iraq Analysis
#######################################################################################################
dates_list = list(df_iraq.Date)

lang_list = list(df_iraq.Lang)

for lan, day in zip(lang_list, dates_list):
    if 'Mar' in day:
        total_mar_tweets += 1
        total_mar_tweets_lang[lan] += 1
    if 'Apr' in day:
        total_apr_tweets += 1
        total_apr_tweets_lang[lan] += 1    
    if 'May' in day:
        total_may_tweets += 1
        total_may_tweets_lang[lan] += 1    

df_stats_iraq = pd.DataFrame(columns=('Language', 'TotalTweets', 'Month'))

#March count
for key, val in total_mar_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'Mar'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_iraq = df_stats_iraq.append(new_row ,ignore_index=True)
    
#April count
for key, val in total_apr_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'Apr'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_iraq = df_stats_iraq.append(new_row, ignore_index=True)
#May count
for key, val in total_may_tweets_lang.items():
    new_row = pd.Series([lang_dict[key], val, 'May'], index=['Language', 'TotalTweets', 'Month'])
    df_stats_iraq = df_stats_iraq.append(new_row,ignore_index=True)

out_s = open("DFStats/stats_iraq.pkl", "wb")
df_stats_iraq.to_pickle(out_s)
out_s.close()
#print(df_stats_armenia)
#######################################################################################################
