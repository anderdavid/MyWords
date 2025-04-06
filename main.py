import tkinter as tk
from src.ui.LearnedFiles import *
class Ui:
    def __init__(self):
        self.window = tk.Tk()
        self.frameTopButtons = tk.Frame(self.window,width=300,height=50)
        self.frameTabContent = tk.Frame(self.window)

    def openFile(self):
        self.frameTabContent.destroy()
        self.frameTabContent = tk.Frame(self.window)
        self.frameTabContent.grid(row =2, column =1,sticky ='w',padx=5, pady=5)
        label = tk.Label(self.frameTabContent,text= 'open File')
        label.grid(row=1, column=1, sticky='w',padx=5, pady=5)
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
