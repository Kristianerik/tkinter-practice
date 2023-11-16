import tkinter as tk
from tkinter import ttk


#setup 
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

#button
def buttonFunction():
    print('a basic button')
    print(radioVar.get())

buttonString = tk.StringVar(value='A button with stringVar')
button = ttk.Button(window, text='A simple button', command=buttonFunction, textvariable=buttonString)
button.pack()

#check button   
checkVar = tk.BooleanVar()
check = ttk.Checkbutton(window, text='checkbox 1', 
                        command = lambda: print(checkVar.get()), variable=checkVar, onvalue=False, offvalue=True)
check.pack()

#radio button
radioVar = tk.StringVar()
radioOne = ttk.Radiobutton(window, text='Radio One', value='radio 1', variable=radioVar,command= lambda: print(radioVar.get()))
radioOne.pack()
radioTwo = ttk.Radiobutton(window, text='Radio Two', value=2, variable=radioVar,command= lambda: print(radioVar.get()))
radioTwo.pack()

#excercise
def radioFunc():
    print(checkBool.get())
    checkBool.set(False)
checkBool = tk.BooleanVar()
radioExcerciseVar = tk.StringVar()

radioThree = ttk.Radiobutton(window, text = 'A', value='A', variable=radioExcerciseVar, command=radioFunc)
radioThree.pack()
radioFour = ttk.Radiobutton(window, text='B', value='B', variable=radioExcerciseVar, command=radioFunc)
radioFour.pack()
checkTwo = ttk.Checkbutton(window, text='checkbox excercise', variable=checkBool, command= lambda: print(radioExcerciseVar.get()))
checkTwo.pack()

#run 
window.mainloop()