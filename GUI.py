from tkinter import *

root=Tk()                              #create a window
from tkinter import *
root=Tk()

title=Label(root,text='Bet@Hub',fg='black')
title.config(font=('courier',32))
title.grid(columnspan=2)

name=Button(root,text='Name:')
password=Button(root,text='Password')
name.grid(row=2,column=0,sticky="E")
password.grid(row=3,column=0,sticky="E")

name_input=Entry(root)
password_input=Entry(root)
name_input.grid(row=2,column=1)
password_input.grid(row=3,column=1)
check=Checkbutton(root,text='Remember password')
check.grid(columnspan=2)
root.mainloop()
