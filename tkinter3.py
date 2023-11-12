import tkinter as tk
from tkinter import ttk

def buttonFunc():
    entry_text = entry.get()
    #update label
    #label.config(text='some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'

def newButtonFunc():
    label['text'] = 'some text'
    entry['state'] = 'enabled'

#window
window = tk.Tk()
window.title('Getting and Setting Widgets')

#widgets
label = tk.Label(master=window, text='Some Text')
label.pack()
entry = ttk.Entry(master=window)
entry.pack()
button = ttk.Button(master=window, text='The Button', command=buttonFunc)
button.pack()

#excercise
newButton = ttk.Button(master=window, text='Change Label', command=newButtonFunc)
newButton.pack()

#run
window.mainloop()