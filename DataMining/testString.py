import gzip
import logging
import json
import os
import pandas as pd
import sys
import binascii

logging.basicConfig(level=logging.DEBUG)

#Current path
path = "/home/matteo/Desktop/Tesi/FolderIteration/Data/"
#Utility counters
bad_lines = 0
tweet_num = 0
geoTweet_num = 0
fileCount = 0

temp = pd.DataFrame()

subdirs = [x[0] for x in os.walk(path)]

for subdir in subdirs:
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
                last_line = lines[-1]
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

            d = json.loads(strJson)

            temp1 = pd.json_normalize(d)
            temp1 = temp1[['coordinates.coordinates','lang', 'created_at']]

            temp = temp.append(temp1, ignore_index = True)
    else:
        print("This subdirectory contains no elements:" + subdir)


#Butto via tutti i valori NaN e creo una nuova colonna coordinates
df = temp.dropna(axis='index', subset=['coordinates.coordinates', 'lang']).assign(coordinates=lambda row: row['coordinates.coordinates'])
#Elimino la vecchia colonna coordinates.coordinates e ne introduco due nuove
df = df.drop(['coordinates.coordinates'], axis = 1)
df[['long','lat']] = pd.DataFrame(df.coordinates.to_list(), index=df.index)
#Prendo il numero di tweet geolocalizzati
geoTweet_num = df.shape[0]

out_stats = open("countryStatistics", "w")

out_stats.write("Total number of tweets: " + str(tweet_num) + "\n")
out_stats.write("Total number of geolocated tweets: " + str(geoTweet_num)+ "\n")
out_stats.write("Total number of bad lines: " + str(bad_lines)+ "\n")

out_stats.close()

out_f = open("dataFrameTest.pkl", "wb")

df.to_pickle(out_f)

out_f.close()
