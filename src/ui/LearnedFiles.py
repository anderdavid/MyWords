import tkinter as tk
from src.Words import *
import shutil
from pathlib import Path
from tkinter import filedialog

class LearnedFiles:
    def __init__(self,container):
        self.learnedFiles =[]
        self.paths = Words().getPaths()
        self.container = container
        self.framePathsContainer = tk.Frame(container)

        print(f"paths",self.paths)

    def setSelected(self,index):
        def callback():
            self.learnedFiles[index]["selected"] =not self.learnedFiles[index]["selected"]

        return callback

    def openWindowAllWords(self):
        print("openWindowAllWords")

    def openWindowAllWords(self):
        new_window = tk.Toplevel(self.container)
        new_window.title("ALL WORDS")
        new_window.geometry("300x200")

    def addFile(self):
        filetypes = (
            ('Text files', '*.srt'),
        )
        filename = filedialog.askopenfilename(title='Open a file .srt', filetypes=filetypes)
        print('Selected:', filename)
        fileTitle = Path(filename).name
        shutil.copy(filename, f"./englishFiles/{fileTitle}")
        self.learnedWords()

    def dropFile(self,name):
        print(f"rname {name}")
        filePath = Path(name)
        filePath.unlink()

    def removeFiles(self):
        selectedFiles = list(filter(lambda x: x["selected"] == True, self.learnedFiles))
        print(f"selectedFiles {selectedFiles}")

        for file in selectedFiles:
            name = f"./englishFiles/{file['name']}"
            print(f"name {name}")
            self.dropFile(name)

        self.learnedWords()

    def learnedWords(self):
        print("learnedWords")
        self.learnedFiles=[]
        self.paths = Words().getPaths()
        print(f"paths {self.paths}")
        for i, path in enumerate(self.paths):
            self.learnedFiles.append({"name": path, "selected": False})

        self.framePathsContainer.destroy()
        self.framePathsContainer = tk.Frame(self.container)
        self.framePathsContainer.grid(row=5, column=1, padx=5, pady=5, sticky='w')

        print(f"learned Files {self.learnedFiles}")

        for i, file, in enumerate(self.learnedFiles):
            var = tk.IntVar()
            checkboxItem = tk.Checkbutton(self.framePathsContainer, text=f"{file['name']}", variable=var,command=self.setSelected(i))
            checkboxItem.grid(row=i, column=1, padx=5, pady=5, sticky='w')

        frameActions = tk.Frame(self.container, width=300, height=50)
        frameActions.grid(row=6, column=1, pady=5, padx=5, sticky='w')
        buttonViewTotalWords = tk.Button(frameActions, text="view all words", command=self.openWindowAllWords)
        buttonViewTotalWords.grid(row=1, column=1, pady=5, padx=5, sticky='w')
        buttonAddFile = tk.Button(frameActions, text="Add File", command=self.addFile)
        buttonAddFile.grid(row=1, column=2, pady=5, padx=5, sticky='w')
        buttonRemoveFiles = tk.Button(frameActions, text="Remove File", command=self.removeFiles)
        buttonRemoveFiles.grid(row=1, column=3, padx=5, pady=5, sticky='w')