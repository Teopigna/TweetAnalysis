import gzip
import logging
import json
import os
import pandas as pd
import sys
import binascii

logging.basicConfig(level=logging.DEBUG)

#Current path
path = "/home/pignotti/mydata/data/"
#Utility counters
bad_lines = 0
tweet_num = 0
geoTweet_num = 0
fileCount = 0

df = pd.DataFrame()

subdirs = [x[0] for x in os.walk(path)]

for subdir in subdirs:
    if(subdir == path+"TR_country"):
        files = os.walk(subdir).__next__()[2]
        totalFiles = len(files)
        if(len(files) > 0):
            semipath = os.path.join(path, subdir)
            for file in files:
                fileCount = fileCount + 1
                print("File n " + str(fileCount) + " out of " + str(totalFiles))
                fullpath = os.path.join(semipath, file)
                
                strJson = "["

                try:
                    in_f = gzip.open(fullpath, 'rt')
                    lines = in_f.readlines()
                    
                    for line in lines:
                        try:
                            tweet_num = tweet_num + 1
                            corrected_line = line.replace('"', '-').replace("'", '"').replace('True', 'true').replace('False', 'false').replace('None', 'null')
                            line_dict = json.loads(corrected_line)
                            corrected_line += ","
                            strJson += corrected_line
                        except ValueError:
                            #logging.debug(f'Line could not be parsed')
                            bad_lines = bad_lines +1
                            continue
                        
                except ValueError:
                    logging.debug('Could not open the file')
                    continue

                strJson = strJson[:-1]
                strJson += "]"
                try:
                    d = json.loads(strJson)

                    temp = pd.json_normalize(d)
                    temp = temp[['id_str','user.id','coordinates.coordinates','lang', 'created_at', 'text']]

                    df = df.append(temp, ignore_index = True)
                except ValueError:
                    logging.debug('Impossible to load json file')
                    continue
        else:
            print("This subdirectory contains no elements:" + subdir)


#Estraggo le colonne indicate dal dataframe temp in uno nuovo df
#df = temp[['coordinates.coordinates','lang']]
#Butto via tutti i valori NaN e creo una nuova colonna coordinates
df = df.dropna(axis='index', subset=['coordinates.coordinates', 'lang']).assign(coordinates=lambda row: row['coordinates.coordinates'])
#Elimino la vecchia colonna coordinates.coordinates e ne introduco due nuove
df = df.drop(['coordinates.coordinates'], axis = 1)
df[['long','lat']] = pd.DataFrame(df.coordinates.to_list(), index=df.index)

geoTweet_num = df.shape[0]

out_stats = open("countryStatistics", "w")

out_stats.write("Total number of tweets: " + str(tweet_num) + "\n")
out_stats.write("Total number of geolocated tweets: " + str(geoTweet_num)+ "\n")
out_stats.write("Total number of bad lines: " + str(bad_lines)+ "\n")

out_stats.close()

out_f = open("dataFrame_country.pkl", "wb")

df.to_pickle(out_f)

out_f.close()
