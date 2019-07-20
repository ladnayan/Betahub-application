from tkinter import *
def layout2():
    root.title('BetaHub: Login_Signup/Page')
    root.geometry('{}x{}'.format(1360,710))

    # create all of the main containers
    border_top = Frame(root, bg='black', width=1360, height=10)
    center = Frame(root, bg='gray2', width=1360, height=690)
    border_bottom = Frame(root, bg='black', width=1360, height=10)


    # layout all of the main containers
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    border_top.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")
    border_bottom.grid(row=3, sticky="ew")

    # create the center widgets
    center.grid_columnconfigure(1, weight=1)
    center.grid_rowconfigure(2, weight=1)


    border_left = Frame(center, bg='black', width=10, height=690)
    middle=Frame(center, width=1340, height=690)
    border_right= Frame(center, bg='black', width=10, height=690)

    border_left.grid(row=0, column=0, sticky="ns")
    middle.grid(row=0, column=1, sticky="nsew")
    border_right.grid(row=0, column=2, sticky="ns")
    middle.grid_propagate(0)
    middle.grid_columnconfigure(0,weight=1)
    middle.grid_rowconfigure(1,weight=1)
    top=Frame(middle,bg='black',width=1340,height=200)
    top.grid(row=0,sticky='nsew')
    mid=Frame(middle,bg='black',width=1340,height=20)
    mid.grid(row=1,sticky='ew')
    bottom=Frame(middle,bg='black',width=1340,height=470)
    bottom.grid(row=2,stick='nsew')
    canvas1=Canvas(top,width=1340,height=200)
    canvas1.grid()
    canvas1.create_rectangle(0,0,1340,200,fill='blue')
    canvas1.create_text(670,100,text='BetaHub',font=("Arial Unicode MS",50,'bold'),fill='white')
    global canvas2
    canvas2=Canvas(bottom,width=1340,height=470)
    canvas2.grid()
    canvas2.create_rectangle(0,0,1340,470,fill='cornflower blue')


root = Tk()
layout2()
canvas2.create_text(200,80,text='Username:',font=("Times",20,'bold'),fill='black')
canvas2.create_text(200,110,text='Password:',font=("Times",20,'bold'),fill='black')
username_login=Entry()
password_login=Entry()
login=Button(text='Login')
canvas2.create_window(350,80,window=username_login)
canvas2.create_window(350,110,window=password_login)
canvas2.create_window(350,140,window=login)

canvas2.create_text(805,80,text='Username:',font=("Times",20,'bold'),fill='black')
canvas2.create_text(805,110,text='Password:',font=("Times",20,'bold'),fill='black')
canvas2.create_text(755,140,text='Confirm Password:',font=("Times",20,'bold'),fill='black')
username_signup=Entry()
password_signup=Entry()
password_check=Entry()
signup=Button(text='Sign Up')
canvas2.create_window(955,80,window=username_signup)
canvas2.create_window(955,110,window=password_signup)
canvas2.create_window(955,140,window=password_check)
canvas2.create_window(955,170,window=signup)

root.mainloop()
'''
# create the widgets for the top frame
model_label = Label(top_frame, text='Model Dimensions',bg='cyan')
width_label = Label(top_frame, text='Width:')
length_label = Label(top_frame, text='Length:')
entry_W = Entry(top_frame, background="pink")
entry_L = Entry(top_frame, background="orange")

# layout the widgets in the top frame
model_label.grid(row=0, columnspan=3)
width_label.grid(row=1, column=0)
length_label.grid(row=1, column=2)
entry_W.grid(row=1, column=1)
entry_L.grid(row=1, column=3)



Label(ctr_mid,text='hello',bg='yellow').grid()'''












'''root=Tk()
root.geometry('1360x710')
root.title('BetaHub: Login/Signup/page')
main=Frame(root,bg='black',width='1360',height='710',padx=10, pady=10)

main.grid_rowconfigure(2,weight=1)
main.grid_columnconfigure(0,weight=1)
main.grid(row=0,sticky='nsew')
#layout of frames
top = Frame(main, bg='blue', width=1340, height=200,padx=10, pady=10)
center=Frame(main, bg='black',width=1340,height=10)
bottom=Frame(main, bg='turquoise2',width=1340,height=480)

top.grid(row=0,column=0)
center.grid(row=1)
bottom.grid(row=2)

#adding widgets to top frame
title=Label(top,text='BetaHub',font=('Arial unicode MS',12),fg='white',bg='blue')
title.grid(row=1,column=1)

root.mainloop()'''
