class Words:
    def __init__(self,ruta):
        self.path = ruta
        self.phrases =[]
        self.words =[]
        self.wordsNoRepeat=[]
        self.jsonWords=[]

        print(f"path: {self.path}")
        self.buildPhrases()
        self.buildWords()
        self.buildNoRepeatWords()
        self.addItemsWords()

    def addphrase(self,line):
        if line.isspace():
            return
        if line.strip().isnumeric():
            return
        if line.find("-->") != -1:
            return
        self.phrases.append(line)

    def buildPhrases(self):
        file = open(self.path,"r")
        for line in file:
            self.addphrase(line)

    def addWords(self,phrase):
        mList = phrase.split()
        self.words.extend(mList)

    def buildWords(self):
        for phrase in self.phrases:
            self.addWords(phrase)

    def addWordNoRepeat(self,word):
        count = self.wordsNoRepeat.count(word)
        if count !=0:
            return
        self.wordsNoRepeat.append(word)

    def buildNoRepeatWords(self):
        for mWord in self.words:
            self.addWordNoRepeat(mWord)

    def addItemsWords(self):
        for noRepeatWord in self.wordsNoRepeat:
            itemWord={}
            count = self.words.count(noRepeatWord)
            itemWord["word"] = noRepeatWord
            itemWord["repeat"] = count
            self.jsonWords.append(itemWord)

    def sortedByRepeat(self):
        sorted_by_repeat = sorted(self.jsonWords, key=lambda x: x["repeat"], reverse=True)
        return sorted_by_repeat


