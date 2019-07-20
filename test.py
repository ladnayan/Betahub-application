from tkinter import *

'''game_screen=Tk()
game_screen.geometry('500x600')
game_screen.title("BetaHub: Rock Paper Scissor")
top=Frame(game_screen,width=500,height=184)
top.pack()
bot=Frame(game_screen)
bot.pack(side='bottom')
p=PhotoImage(file='top.png')
print(p)
Label(top,image=p).pack(fill=X)
Button(bot,text='ROCK').pack()
game_screen.mainloop()

button1 = Button(self, text = "Quit", command = self.quit, anchor = W)
button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
button1_window = canvas1.create_window(10, 10, anchor=NW, window=button1)'''

'''root = Tk()              #to pass width and heigt as variable
root.title('Model Definition')
i=800
root.geometry('{}x{}'.format(800, i))
root.mainloop()'''

root=Tk()
root.geometry('800x400')
main=Frame(root,bg='black',width='800',height='400',padx=10, pady=10)
main.grid_rowconfigure(0,weight=1)
main.grid_rowconfigure(0,weight=1)
main.grid()

top = Frame(main, bg='blue', width=780, height=185, padx=10, pady=10)
center=Frame(main, bg='black',width=780,height=10)
bottom=Frame(main, bg='red',width=780,height=185)

center.grid(row=1)
top.grid(row=0)
bottom.grid(row=2)
Button(top,text='hello').grid()
root.mainloop()
