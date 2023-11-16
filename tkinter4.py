import tkinter as tk
from tkinter import ttk

def buttonFunc():
    print(stringVar.get())
    stringVar.set('button pressed')

# window
window = tk.Tk()
window.title("tkinter variables")

#tkinter var
stringVar = tk.StringVar()

# widget
label = ttk.Label(master=window, text='Label', textvariable=stringVar)
label.pack()

entry = ttk.Entry(master=window, textvariable=stringVar)
entry.pack()

button = ttk.Button(master=window, text='button', command=buttonFunc)
button.pack()

#excercise
stringVarTwo = tk.StringVar(value='test')

labelTwo = ttk.Label(master=window, text='Label 2', textvariable=stringVarTwo)
labelTwo.pack()
entryTwo = ttk.Entry(master=window, textvariable=stringVarTwo)
entryTwo.pack()
entryThree = ttk.Entry(master=window, textvariable=stringVarTwo)
entryThree.pack()

#run
window.mainloop()