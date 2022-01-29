import time
import csv
import sys
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
destData = time.strftime("data.txt")
placeholder = "LastLine.txt"

# with open(sourceData, 'r', encoding='latin-1') as csvfile:
    # with open(destData, 'w', encoding='latin-1') as dstfile:
        # reader = csv.reader(csvfile)
        # writer = csv.writer(dstfile)
        # next (reader) #skip header
        # for row in reader:
            # writer.writerow(row)
            
def GetLineCount():
    with open(sourceData) as f:
        for i, l in enumerate(f):
            pass
    return i

def MakeLog(startLine, numLines):
    destData = time.strftime("%Y%m%d-%H%M%S.txt")
    with open(sourceData, 'r') as csvfile:
        with open(destData, 'w') as dstfile:
            reader = csv.reader(csvfile)
            writer = csv.writer(dstfile)
            next (reader) #skip header
            inputRow = 0
            linesWritten = 0
            for row in reader:
                inputRow += 1
                if (inputRow > startLine):
                    writer.writerow(row)
                    linesWritten += 1
                    if (linesWritten >= numLines):
                        break
            return linesWritten
        
    
numLines = 1
startLine = 0            
if (len(sys.argv) > 1):
    numLines = int(sys.argv[1])
    
try:
    with open(placeholder, 'r') as f:
        for line in f:
             startLine = int(line)
except IOError:
    startLine = 0

print("Writing " + str(numLines) + " lines starting at line " + str(startLine) + "\n")

totalLinesWritten = 0
linesInFile = GetLineCount()

while (totalLinesWritten < numLines):
    linesWritten = MakeLog(startLine, numLines - totalLinesWritten)
    totalLinesWritten += linesWritten
    startLine += linesWritten
    if (startLine >= linesInFile):
        startLine = 0
        
print("Wrote " + str(totalLinesWritten) + " lines.\n")
    
with open(placeholder, 'w') as f:
    f.write(str(startLine))