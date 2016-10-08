
import json, string, os
from stop_words import get_stop_words

stop_words = get_stop_words('english')
RESULTS = {}

linecounter = 0
wordcounter = 0


fileList = os.listdir("./books/")

for filename in fileList: 

    print("\t> Scanning " + filename + " ...")

    with open("./books/" + filename, 'r') as file:
        for line in file:
            for word in line.split():
                exclude = set(string.punctuation)
                newword = ''.join(ch for ch in word if ch not in exclude)

                flag = True
                for ch in newword:
                    if ch in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        flag = False

                if word == "":
                    flag = False

                if not newword.lower() in stop_words and flag:
                    try:
                        RESULTS[newword].append([filename, linecounter, wordcounter])
                    except:
                        RESULTS[newword] = [[filename, linecounter, wordcounter]]

                wordcounter += 1
            linecounter += 1


with open('Result_Map.json', 'w') as output:
    json.dump(RESULTS, output, ensure_ascii=False, indent=4, sort_keys=True)



