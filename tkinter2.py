import tkinter as tk
from tkinter import ttk

def button_func():
    print('A button was pressed')

def newButtonFunc():
    print('hello')

#creating window
window = tk.Tk()
window.title('Widgets')
window.geometry('800x500')

#ttk label
label = ttk.Label(master=window, text='This is a Test')
label.pack()

#tk text
text = tk.Text(master=window)
text.pack()

#ttk entry
entry = ttk.Entry(master=window)
entry.pack()

#excercise 
newLabel = ttk.Label(master=window, text='My label')
newLabel.pack()
newButton = ttk.Button(master=window, text='Hello', command=newButtonFunc)
newButton.pack()

#ttk button
button = ttk.Button(master=window, text='A button', command=button_func)
button.pack()

#run
window.mainloop()
