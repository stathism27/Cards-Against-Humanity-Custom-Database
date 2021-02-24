#A script to integrate Packs in Cards Against Humanity
import json

db = "Cards Against Humanity Database.json"
names_of_packs = ["Greek Reality"]
output = "Cards Against Humanity Database Expanded.json"
def addPack(pack):
    cards[pack] = {'name':pack, 'white':[], 'black':[], 'official': False}#.append({'name':pack, 'white':[], 'black':[], 'official': False})

    addCards(pack)

def addCards(pack):

    whites = "whites/"+pack + "_whites.txt"
    blacks = "blacks/"+pack + "_blacks.txt"
    with open(whites) as w:
        for line in w.readlines():
            line = customizeString(line)
            if(line not in cards[pack]['white']):
                cards[pack]['white'].append(line)
    with open(blacks) as b:
        for line in b.readlines():
            line = customizeString(line)
            if(line not in cards[pack]['black']):
                underscores = line.count("_")
                if(underscores == 0):
                    underscores =1
                blackDict ={'text':line,'pick':underscores}
                cards[pack]['black'].append(blackDict)

def customizeString(string):
    if("\n" in string):
        string = string.replace('\r', '').replace('\n', '')
    return string


with open(db) as json_file:
    cards = json.load(json_file)

for pack in names_of_packs:
    if(pack not in cards):
        addPack(pack)
    else:
        addCards(pack)

#output
with open(output,"w") as out:
    json.dump(cards,out, ensure_ascii=False)
counter = 0
s = 0
for key in cards:
    print(cards[key]['name'])
    print(len(cards[key]['black']))
    print()