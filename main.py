from src.Words import *
ruta = "./englishFiles/englishFile.srt"

words =Words(ruta)
words.buildPhrases()
words.buildWords()
words.buildNoRepeatWords()
words.addItemsWords()
sorted_by_repeat =words.sortedByRepeat()

print(sorted_by_repeat)




