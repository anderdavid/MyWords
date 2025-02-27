from src.Words import *
import tkinter as tk
from tkinter import filedialog
def openFile():
    filetypes = (
        ('Text files', '*.srt'),
    )
    filename = filedialog.askopenfilename(title='Open a file .srt',filetypes=filetypes)
    print('Selected:', filename)
    labelFile.config(text=f"path: {filename}")
    words = Words(filename)
    listWords = words.getWordsNoRepeatSorted()

    for word in listWords:
        listbox.insert(tk.END,f" {word}")

    labelNumWords.config(text=f"Number words {len(listWords)}")
    frame.pack(pady=10,side="top")


window = tk.Tk()
window.title("MY ENGLISH WORDS")
window.geometry("600x700")
button = tk.Button(window, text="Open File",command=openFile)
button.pack(side="top",anchor="w",padx=10, pady=5)
labelFile = tk.Label(window)
labelFile.pack(padx=10, pady=5)
labelNumWords = tk.Label(window)
labelNumWords.pack(side="top",padx=10, pady=10)

frame = tk.Frame(window,width=400,height=500)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set,width=30,height=20,font=("Arial",14))
listbox.pack(side=tk.LEFT,pady=10)

scrollbar.config(command=listbox.yview)


window.mainloop()




