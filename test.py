from tkinter import *

def keep_flat(event):       # on click,
    if event.widget is btn: # if the click came from the button
        event.widget.config(relief='flat') # enforce an option

def change_back(event):       # on click,
    if event.widget is btn: # if the click came from the button
        event.widget.config(relief='groove') # enforce an option

def callback():
    print('button clicked')

root = Tk()

btn = Button(root, text='click', relief='groove', command=callback)
btn.pack()

root.bind('<Button-1>', keep_flat) # bind the application to left mouse click
root.bind("<ButtonRelease-1>", change_back)

mainloop()