from tkinter import *
def name_check(d,name):
        """ function to check the validity of the user name"""
        if name in d.keys():
                Label(bot,text="Username taken",fg='red').grid(row=6,column=5)
                #name_check(d,name)
