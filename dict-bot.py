import glob
import sys

files = glob.glob(sys.argv[1]) #get files
print(f"checkingfiles:{files}")

dic = dict()
#add bot to dict 
def process(lines, k, x): 
    global dic
    word = lines[k][x-10:x+3] #Extract the characters before and after the bot
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] = dic[word]+1

for i in files:
    with open(i, "r" , encoding="utf-8") as f:
        lines = f.readlines()
        for k in range(len(lines)):
            x = lines[k].find("bot")
            if x == -1:
                x = lines[k].find("Bot")
                if x == -1:
                    x = lines[k].find("BOT")
                    if x == -1:
                        continue
                    else:
                        process(lines,k, x)
                else:
                    process(lines,k, x)
            else:
                process(lines, k, x)


print(dic)
