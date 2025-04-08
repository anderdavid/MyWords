import tkinter as tk
import pyttsx3

class ListWords:
    def __init__(self,container):
        self.container = container
        self.container.grid(row=5, column=1, sticky='w', padx=5, pady=5)

        self.scrollbar = tk.Scrollbar(self.container)
        self.listbox = tk.Listbox(self.container, yscrollcommand=self.scrollbar.set, width=30, height=20, font=("Arial", 14))
        self.buttonCopyClipBoard = tk.Button(self.container, text ="Copy to clipboard",command=self.copyClipBoard)

        self.scrollbar.grid(row=1, column=1, sticky='w', padx=5, pady=5)
        self.listbox.grid(row=1, column=1, sticky='w', pady=10)
        self.scrollbar.config(command=self.listbox.yview)


    def insertListInFrame(self,list):
        self.listbox.delete(0, tk.END)
        for word in list:
            self.listbox.insert(tk.END, f" {word}")
        self.container.grid(row=4, column=1, sticky='w', padx=5, pady=5)
        self.buttonCopyClipBoard.grid(row=6, column=1, sticky='w', padx=5, pady=5)
    def copyClipBoard(self):
            items = self.listbox.get(0,tk.END)
            textToCopy = '\n'.join(items)
            self.container.clipboard_clear()
            self.container.clipboard_append(textToCopy)
            self.container.update()

    def speak_word(word):
        engine = pyttsx3.init()
        engine.say(word)
        engine.runAndWait()