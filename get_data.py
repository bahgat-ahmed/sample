import json
import time

# with open('sample.json') as input_file:
    # data = json.load(input_file)

# tweet_ids, airlines, names, texts, tweet_coords, tweet_createds, tweet_locations, user_timezones = [], [], [], [], [], [], [], []

# for record in data:
    # tweet_ids.append(record['tweet_id'])
    # airlines.append(record['airline'])
    # names.append(record['name'])
    # texts.append(record['text'])
    # tweet_coords.append(record['tweet_coord'])
    # tweet_createds.append(record['tweet_created'])
    # tweet_locations.append(record['tweet_location'])
    # user_timezones.append(record['user_timezone'])  

sourceData = "sample.csv" 
destData = time.strftime("/data.txt")
with open(sourceData, 'r', encoding='latin-1') as csvfile:
    with open(destData, 'w') as dstfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(dstfile)
        next (reader) #skip header
        for row in reader:
            writer.writerow(row)