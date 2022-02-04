from tkinter import *

root = Tk()			
root.geometry('100x100')

btn = Button(root, text = 'HEY! CLICK HERE !!', bd = '5',command = root.destroy)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
root.configure(background='darkblue')

root.mainloop()
