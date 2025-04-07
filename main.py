import tkinter as tk
from src.ui.LearnedFiles import *
from src.ui.ListWords import *
from src.Words import *
class Ui:
    def __init__(self):
        self.window = tk.Tk()
        self.filename =""
        self.frameTopButtons = tk.Frame(self.window,width=300,height=50)
        self.frameTabContent = tk.Frame(self.window)
        self.frameListContent = tk.Frame(self.window)
        self.labelNumWords = None


    def openFile(self):
        self.frameTabContent.destroy()
        self.frameTabContent = tk.Frame(self.window)
        self.frameTabContent.grid(row =2, column =1,sticky ='w',padx=5, pady=5)

        filetypes = (
            ('Text files', '*.srt'),
        )
        self.filename = filedialog.askopenfilename(title='Open a file .srt', filetypes=filetypes)
        print('Selected:', self.filename)

        labelFile = tk.Label(self.frameTabContent,text =self.filename)
        labelFile.grid(row=1, column=1, padx=10, pady=10)

        self.labelNumWords = tk.Label(self.frameTabContent)
        self.labelNumWords.grid(row=2, column=1, sticky='w', padx=10, pady=10)

        frameButtons = tk.Frame(self.frameTabContent, width=300, height=50)
        frameButtons.grid(row=3, column=1, sticky='w', padx=5, pady=5)

        buttonWordsOfFile = tk.Button(frameButtons, text="Words of File", command=self.wordsOfFile)
        buttonNewWords = tk.Button(frameButtons, text="new words", command=self.newWords)
        buttonWordsOfFile.grid(row=1, column=1, padx=5, pady=5)
        buttonNewWords.grid(row=1, column=2, padx=5, pady=5)

    def newWords(self):
        self.frameListContent = tk.Frame(self.frameTabContent)
        totalWords = Words()
        totalWords.addTotalWords()
        mWords = Words()
        mWords.openFile(self.filename)
        newListWords = mWords.buildNewWords(totalWords.wordsNoRepeat, mWords.wordsNoRepeat)

        self.labelNumWords.config(text=f"Number words {len(newListWords)}")
        listWords = ListWords(container=self.frameListContent)
        listWords.insertListInFrame(newListWords)

    def wordsOfFile(self):
        self.frameListContent = tk.Frame(self.frameTabContent)
        words = Words()
        words.openFile(self.filename)
        list = words.getWordsNoRepeatSorted()
        self.labelNumWords.config(text=f"Number words {len(list)}")
        listWords = ListWords(container=self.frameListContent)
        listWords.insertListInFrame(list)

    def learnedWords(self):
        self.frameTabContent.destroy()
        self.frameTabContent = tk.Frame(self.window)
        self.frameTabContent.grid(row=2, column=1, sticky='w', padx=5, pady=5)

        learnedFiles = LearnedFiles(container=self.frameTabContent)
        learnedFiles.learnedWords()
    def initUi(self):
        self.window.title("MY ENGLISH WORDS")
        self.window.geometry("600x700+200+0")
        self.frameTopButtons.grid(row=1, column=1, sticky='w', padx=5, pady=5)
        self.frameTabContent.grid(row =2, column =1,sticky ='w',padx=5, pady=5)

        buttonOpen = tk.Button(self.frameTopButtons, text="Open File", command=self.openFile)
        buttonOpen.grid(row=1, column=1, sticky='w', padx=5, pady=5)
        buttonLearnedWords = tk.Button(self.frameTopButtons, text="Learned Words", command=self.learnedWords)
        buttonLearnedWords.grid(row=1, column=2, sticky='w', padx=5, pady=5)

        self.window.mainloop()

ui = Ui()
ui.initUi()
