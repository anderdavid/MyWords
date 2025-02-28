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
    buttonWordsOfFile.pack(pady=10, side="top")
    buttonNewWords.pack(pady=10, side="top")

def speak_word(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()
def insertListInFrame(list):
    labelNumWords.config(text=f"Number words {len(list)}")
    listbox.delete(0, tk.END)
    for word in list:
        listbox.insert(tk.END, f" {word}")

    frame.pack(pady=10,side="top")
    buttonCopyClipBoard.pack(pady =10, side="bottom")

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

def copyClipBoard():
    items = listbox.get(0,tk.END)
    textToCopy = '\n'.join(items)
    window.clipboard_clear()
    window.clipboard_append(textToCopy)
    window.update()

window = tk.Tk()
window.title("MY ENGLISH WORDS")
window.geometry("600x700")
button = tk.Button(window, text="Open File",command=openFile)
button.pack(side="top",anchor="w",padx=10, pady=5)
labelFile = tk.Label(window)
labelFile.pack(padx=10, pady=5)
labelNumWords = tk.Label(window)
labelNumWords.pack(side="top",padx=10, pady=10)

buttonWordsOfFile = tk.Button(window,text="Words of File",command=wordsOfFile)
buttonNewWords = tk.Button(window, text ="new words",command=newWords)

frame = tk.Frame(window,width=400,height=800)


scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set,width=30,height=20,font=("Arial",14))
listbox.pack(side=tk.LEFT,pady=10)
buttonCopyClipBoard = tk.Button(window, text ="Copy to clipboard",command=copyClipBoard)

scrollbar.config(command=listbox.yview)


window.mainloop()




