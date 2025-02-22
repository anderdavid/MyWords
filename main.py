ruta = "./englishFiles/englishFile.srt"

phrases = []
words = []
wordsNoRepeat =[]
jsonWords =[]

print(ruta)
f = open(ruta, "r")


def addphrase(mLine):
    if mLine.isspace():
        return
    if mLine.strip().isnumeric():
        return
    if mLine.find("-->") != -1 :
        return
    phrases.append(mLine)

def addWords(phrase):
    mList = phrase.split()
    words.extend(mList)

def addWordNoRepeat(word):
    count = wordsNoRepeat.count(word)
    if count !=0:
        return
    wordsNoRepeat.append(word)

def buildNoRepeatWords():
    for mWord in words:
        addWordNoRepeat(mWord)


def addItemsWords():

    for noRepeatWord in wordsNoRepeat:
        itemWord = {}
        count = words.count(noRepeatWord)
        itemWord["word"] = noRepeatWord
        itemWord["repeat"] = count
        jsonWords.append(itemWord)


for line in f:
    addphrase(line)

for phrase in phrases:
    addWords(phrase)

buildNoRepeatWords()
addItemsWords()


sorted_by_repeat = sorted(jsonWords,key=lambda x: x["repeat"],reverse=True)

print("count of words: ",len(sorted_by_repeat))
print(sorted_by_repeat)
