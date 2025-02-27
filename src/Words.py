import os

class Words:
    def __init__(self):
        self.initPath = "./englishFiles"
        self.paths = []
        self.phrases = []
        self.words = []
        self.jsonWords = []
        self.totalWords = []
        self.words = []
        self.wordsNoRepeat = []

    def setPaths(self):
        namesOfFile = os.listdir(self.initPath)
        self.paths.extend(namesOfFile)

    def openFile(self, path):
        self.buildPhrases(path)
        self.buildWords()
        self.buildNoRepeatWords()
        self.addItemsWords()

    def addphrase(self, line):

        if line.isspace():
            return
        if line.strip().isnumeric():
            return
        if line.find("-->") != -1:
            return
        self.phrases.append(line)

    def buildPhrases(self, path):
        file = open(path, "r")
        for line in file:
            self.addphrase(line)

    def addWords(self, phrase):
        mList = phrase.split()
        self.words.extend(mList)

    def buildWords(self):
        for phrase in self.phrases:
            self.addWords(phrase)

    def addWordNoRepeat(self, word):
        count = self.wordsNoRepeat.count(word)
        if count !=0:
            return
        self.wordsNoRepeat.append(word)

    def buildNoRepeatWords(self):
        for mWord in self.words:
            self.addWordNoRepeat(mWord)


    def addTotalWords(self):
        self.setPaths()
        for path in self.paths:
            self.buildPhrases(f"{self.initPath}/{path}")
            self.buildWords()
            self.buildNoRepeatWords()

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

    def getWordsNoRepeatSorted(self):
        listWords=[]
        jsonSorted = self.sortedByRepeat()

        for item in jsonSorted:
            listWords.append(item["word"])

        return listWords



    def buildNewWords(self,listWords,newList):
        newWords =[]
        for word in newList:
            count = listWords.count(word)
            if count == 0:
                newWords.append(word)

        return newWords

