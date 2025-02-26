from src.Words import *
import tkinter as tk
from tkinter import filedialog
def openFile():
    filetypes = (
        ('Text files', '*.srt'),
    )
    filename = filedialog.askopenfilename(title='Open a file',filetypes=filetypes)
    print('Selected:', filename)
    labelFile.config(text=f"path: {filename}")
    words = Words(filename)
    sorted_by_repeat = words.sortedByRepeat()
    labelNumWords.config(text=f"Number words {len(sorted_by_repeat)}")

    print(sorted_by_repeat)

window = tk.Tk()
window.title("MY ENGLISH WORDS")
window.geometry("600x700")
button = tk.Button(window, text="Open File",command=openFile)
button.pack(side="top",anchor="w",padx=10, pady=5)
labelFile = tk.Label(window)
labelFile.pack(padx=10, pady=5)
labelNumWords = tk.Label(window)
labelNumWords.pack(side="top",padx=10, pady=10)
window.mainloop()




