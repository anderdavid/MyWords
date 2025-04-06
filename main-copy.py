from src.Words import *
import tkinter as tk
import pyttsx3
from tkinter import filedialog
import shutil
from pathlib import Path

filename = ""
learnedFiles =[]
def openFile():
    global  filename
    filetypes = (
        ('Text files', '*.srt'),
    )
    filename = filedialog.askopenfilename(title='Open a file .srt',filetypes=filetypes)
    print('Selected:', filename)
    labelFile.config(text=f"path: {filename}")
    labelFile.grid(row=2, column=1, padx=10, pady=10)


    frameButtons.grid(row=4, column=1,sticky='w',padx=5, pady=5)
    buttonWordsOfFile.grid(row=1, column=1, padx=5, pady=5)
    buttonNewWords.grid(row=1, column=2, padx=5, pady=5)

def addFile():
    filetypes = (
        ('Text files', '*.srt'),
    )
    filename = filedialog.askopenfilename(title='Open a file .srt', filetypes=filetypes)
    print('Selected:', filename)
    fileTitle =Path(filename).name
    shutil.copy(filename, f"./englishFiles/{fileTitle}")
    learnedWords()

def removeFile(name):
    filePath = Path(name)
    filePath.unlink()

def removeFiles():
    print("remove Files")
    print(learnedFiles)

    selectedFiles = list(filter(lambda x: x["selected"] == True, learnedFiles))
    print("selectedFiles",selectedFiles)

    for file in selectedFiles:
        removeFile(f"./englishFiles/{file['name']}")

    learnedWords()



def speak_word(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()
def insertListInFrame(list):
    labelNumWords.config(text=f"Number words {len(list)}")
    listbox.delete(0, tk.END)
    for word in list:
        listbox.insert(tk.END, f" {word}")

    frameContainer.grid(row=5,column=1,sticky='w',padx=5,pady=5)
    buttonCopyClipBoard.grid(row=6,column=1,sticky='w',padx=5,pady=5)

def wordsOfFile():
    words = Words()
    words.openFile(filename)
    listWords = words.getWordsNoRepeatSorted()
    insertListInFrame(listWords)


def newWords():
    print("newWords")
    totalWords = Words()
    totalWords.addTotalWords()

    mWords = Words()
    mWords.openFile(filename)

    newListWords = mWords.buildNewWords(totalWords.wordsNoRepeat,mWords.wordsNoRepeat)
    insertListInFrame(newListWords)

def openWindowAllWords():
    new_window = tk.Toplevel(window)
    new_window.title("ALL WORDS")
    new_window.geometry("300x200")


def setSelected(index):
    def callback():
        global learnedFiles
        learnedFiles[index]["selected"] =not learnedFiles[index]["selected"]

    return callback

def learnedWords():
    global learnedFiles
    global framePathsContainer
    learnedFiles =[]
    mWords = Words()
    paths =mWords.getPaths()
    print(f"paths ",paths)


    for i,path in enumerate(paths):
        learnedFiles.append({"name":path,"selected":False})

    framePathsContainer.destroy()
    framePathsContainer = tk.Frame(window)
    framePathsContainer.grid( row=5, column=1,padx=5,pady=5,sticky='w')



    for i,file, in enumerate(learnedFiles):
        var = tk.IntVar()
        checkboxItem = tk.Checkbutton(framePathsContainer, text=f"{file['name']}",variable=var,command=setSelected(i))
        checkboxItem.grid( row=i,column=1,padx=5,pady=5,sticky='w')

    frameActions = tk.Frame(window,width=300,height=50)
    frameActions.grid(row=6,column=1,pady=5,padx=5,sticky='w')
    buttonViewTotalWords = tk.Button(frameActions,text="view all words",command=openWindowAllWords)
    buttonViewTotalWords.grid(row=1,column=1,pady=5,padx=5,sticky='w')
    buttonAddFile = tk.Button(frameActions, text="Add File", command=addFile)
    buttonAddFile.grid(row=1, column=2, pady=5, padx=5, sticky='w')
    buttonRemoveFiles = tk.Button(frameActions,text="Remove File",command=removeFiles)
    buttonRemoveFiles.grid(row=1,column=3,padx=5,pady=5, sticky='w')



def copyClipBoard():
    items = listbox.get(0,tk.END)
    textToCopy = '\n'.join(items)
    window.clipboard_clear()
    window.clipboard_append(textToCopy)
    window.update()

window = tk.Tk()
window.title("MY ENGLISH WORDS")
window.geometry("600x700+0+0")

frameTopButtons = tk.Frame(window,width=300,height=50)
frameTopButtons.grid(row=1, column=1, sticky='w', padx=5, pady=5)

framePathsContainer = tk.Frame(window)

buttonOpen = tk.Button(frameTopButtons, text="Open File",command=openFile)
buttonOpen.grid(row=1, column=1,sticky='w', padx=5, pady=5)
buttonLearnedWords = tk.Button(frameTopButtons, text ="Learned Words",command=learnedWords)
buttonLearnedWords.grid(row =1, column=2, sticky='w', padx=5, pady =5)

labelFile = tk.Label(window)
labelNumWords = tk.Label(window)
labelNumWords.grid(row=3, column=1,sticky='w', padx=10, pady=10)


frameButtons = tk.Frame(window,width=300,height=50)

buttonWordsOfFile = tk.Button(frameButtons,text="Words of File",command=wordsOfFile)
buttonNewWords = tk.Button(frameButtons, text ="new words",command=newWords)

frameContainer = tk.Frame(window,width=400,height=800)


scrollbar = tk.Scrollbar(frameContainer)
scrollbar.grid(row=1,column=1,sticky='w',padx=5, pady=5)

listbox = tk.Listbox(frameContainer, yscrollcommand=scrollbar.set,width=30,height=20,font=("Arial",14))
listbox.grid(row=1,column=1,sticky='w',pady=10)
buttonCopyClipBoard = tk.Button(window, text ="Copy to clipboard",command=copyClipBoard)

scrollbar.config(command=listbox.yview)


window.mainloop()




