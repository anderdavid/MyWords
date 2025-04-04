from src.Words import *
import tkinter as tk
import pyttsx3
from tkinter import filedialog

filename = ""
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
    buttonLearnedWords.grid(row=1, column=1, padx=5, pady=5)
    buttonWordsOfFile.grid(row=1, column=2, padx=5, pady=5)
    buttonNewWords.grid(row=1, column=3, padx=5, pady=5)

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

def learnedWords():
    print("Learned words")

def copyClipBoard():
    items = listbox.get(0,tk.END)
    textToCopy = '\n'.join(items)
    window.clipboard_clear()
    window.clipboard_append(textToCopy)
    window.update()

window = tk.Tk()
window.title("MY ENGLISH WORDS")
window.geometry("600x700+0+0")

buttonOpen = tk.Button(window, text="Open File",command=openFile)
buttonOpen = buttonOpen.grid(row=1, column=1,sticky='w', padx=5, pady=5)

labelFile = tk.Label(window)
labelNumWords = tk.Label(window)
labelNumWords.grid(row=3, column=1,sticky='w', padx=10, pady=10)


frameButtons = tk.Frame(window,width=300,height=50)
buttonLearnedWords = tk.Button(frameButtons, text ="Learned Words",command=learnedWords)
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




