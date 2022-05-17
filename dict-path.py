import glob
import sys
import csv
import json

files = glob.glob(sys.argv[1]) #get files.

print(f"checkinglogs:{files}")
dic = dict()

#add path to dict 
def process(words, locat):  
    global dic
    word = words[locat+6:]
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] = dic[word]+1

for i in files:
    with open(i, "r", encoding="utf-8") as f:
        lines = csv.reader(f)
        for k in lines:
            for l in k:
                if l.find("/wp-cron.php") >=0: #if you delete a specific path.
                    break
                loca = l.find("path") #find location at "path".
                if loca > -1:
                    process(l, loca) #it hands over words line and location.
                    break
#dic = sorted(dic.items(), key=lambda x:x[1], reverse=True) #if you sorted value, you delete coment out.


#you need to change [filepath].
#this is to save dict as json type.
with open("filepath","w", encoding="utf-8") as f: 
    json.dump(dic, f, indent=4)
    
