from tkinter import *
from data_base_load import data_base_load
import pymysql
import os
import time
import random

uw=0
cw=0
gd=0
def global_zero():
    global uw
    global cw
    global gd
    uw=0
    cw=0
    gd=0 #set game variables to zero
def Calculator():
    global_zero()
    homepage()
    global operator
    operator=""
    global input
    input=StringVar()
    def click(num):
        global operator
        operator=operator+str(num)
        input.set(operator)
    def clear():
        global operator
        operator=""
        input.set("")
    def equal():
        global operator
        sumup=str(eval(operator))
        input.set(sumup)
        operator=""


    display=Entry(textvariable=input,width=25,bd=10,bg='powder blue',font=('arial',25,'bold'),justify='right')
    canvas2.create_text(830,80,text='Calculator',font=('Times',40,'bold'),fill='black')
    calc9=Button(text='9',width=5,height=1,font=('Times',25,'bold'),command=lambda: click(9))
    calc8=Button(text='8',width=5,height=1,font=('Times',25,'bold'),command=lambda: click(8))
    calc7=Button(text='7',width=5,height=1,font=('Times',25,'bold'),command=lambda: click(7))
    calc6=Button(text='6',width=5,height=1,font=('Times',25,'bold'),command=lambda: click(6))
    calc5=Button(text='5',width=5,height=1,font=('Times',25,'bold'),command=lambda: click(5))
    calc4=Button(text='4',width=5,height=1,font=('Times',25,'bold'),command=lambda: click(4))
    calc3=Button(text='3',width=5,height=1,font=('Times',25,'bold'),command=lambda: click(3))
    calc2=Button(text='2',width=5,height=1,font=('Times',25,'bold'),command=lambda: click(2))
    calc1=Button(text='1',width=5,height=1,font=('Times',25,'bold'),command=lambda: click(1))
    calcC=Button(text='C',width=5,height=1,font=('Times',25,'bold'),command=clear)
    calc0=Button(text='0',width=5,height=1,font=('Times',25,'bold'),command=lambda: click(0))
    calc_equal=Button(text='=',width=5,height=1,font=('Times',25,'bold'),command=equal)
    calc_add=Button(text='+',width=5,height=1,font=('Times',25,'bold'),command=lambda: click('+'))
    calc_sub=Button(text='-',width=5,height=1,font=('Times',25,'bold'),command=lambda: click('-'))
    calc_div=Button(text='/',width=5,height=1,font=('Times',25,'bold'),command=lambda: click('/'))
    calc_mul=Button(text='*',width=5,height=1,font=('Times',25,'bold'),command=lambda: click('*'))

    canvas2.create_window(600,160,window=display,anchor=W)
    canvas2.create_window(600,220,window=calc7,anchor=W)
    canvas2.create_window(720,220,window=calc8,anchor=W)
    canvas2.create_window(840,220,window=calc9,anchor=W)
    canvas2.create_window(960,220,window=calc_div,anchor=W)
    canvas2.create_window(600,270,window=calc4,anchor=W)
    canvas2.create_window(720,270,window=calc5,anchor=W)
    canvas2.create_window(840,270,window=calc6,anchor=W)
    canvas2.create_window(960,270,window=calc_mul,anchor=W)
    canvas2.create_window(600,320,window=calc1,anchor=W)
    canvas2.create_window(720,320,window=calc2,anchor=W)
    canvas2.create_window(840,320,window=calc3,anchor=W)
    canvas2.create_window(960,320,window=calc_sub,anchor=W)
    canvas2.create_window(600,370,window=calcC,anchor=W)
    canvas2.create_window(720,370,window=calc0,anchor=W)
    canvas2.create_window(840,370,window=calc_equal,anchor=W)
    canvas2.create_window(960,370,window=calc_add,anchor=W)
def Bank():
    global_zero()
    homepage()
    canvas2.create_text(830,80,text='BetaHub Bank',font=('calibri',40,'bold'),fill='black')
    canvas2.create_text(830,180,text='Service not available, sorry for the inconvenience!',font=('calibri',20),fill='black')
def Change_password():
    def Change_password_confirmation():
        print(name)
        data_base=data_base_load()
        old=old_password.get()
        new=new_password.get()
        check=confirm_new_password.get()
        old_password_entry.delete(0,END)
        new_password_entry.delete(0,END)
        confirm_new_password_entry.delete(0,END)

        if data_base[name][1]==hash(old):
            if new==check:
                db=pymysql.connect('localhost','nayan','1234','user_database')
                cursor=db.cursor()
                cursor.execute("UPDATE data SET password=%s WHERE username=%s",(hash(new),name))
                db.commit()
                db.close()
                Change_password()
                canvas2.create_text(1110,320,text="Password changed",font=('Times',15,'bold'),fill='black')
            else:
                Change_password()
                canvas2.create_text(1110,320,text="Password doesn't match",font=('Times',15,'bold'),fill='black')
        else:
            Change_password()
            canvas2.create_text(1110,330,text='Incorrect Password',font=('Times',15,'bold'),fill='black')
    Settings()
    global old_password
    global new_password
    global confirm_new_password
    global old_password_entry
    global new_password_entry
    global confirm_new_password_entry
    old_password=StringVar()
    new_password=StringVar()
    confirm_new_password=StringVar()
    old_password_entry=Entry(textvariable=old_password)
    new_password_entry=Entry(textvariable=new_password)
    confirm_new_password_entry=Entry(textvariable=confirm_new_password)
    ok=Button(text='confirm',command=Change_password_confirmation,font=('Times',12,'bold'))

    canvas2.create_text(920,180,text='Current Password:',font=('Times',20,'bold'),fill='black')
    canvas2.create_text(920,230,text='      New Password:',font=('Times',20,'bold'),fill='black')
    canvas2.create_text(920,280,text='Confirm Password:',font=('Times',20,'bold'),fill='black')
    canvas2.create_window(1040,180,window=old_password_entry,anchor=W)
    canvas2.create_window(1040,230,window=new_password_entry,anchor=W)
    canvas2.create_window(1040,280,window=confirm_new_password_entry,anchor=W)
    canvas2.create_window(1070,310,window=ok,anchor=W)
def rock_paper_scissor_game(choice):
    user=choice
    def game(user):
        global uw
        global cw
        global gd
        global comp
        choice=user

        list=['rock','paper','scissor']
        comp=random.choice(list)
        if choice==1:            #rock
            if (comp=='scissor'):
                uw=uw+1
                return('won')
            elif (comp=='paper'):
                cw=cw+1
                return('lost')
            else:
                gd=gd+1
                return('game drawn')

        if choice==3:          #scissor
            if (comp=='rock'):
                cw=cw+1
                return('lost')
            elif (comp=='paper'):
                uw=uw+1
                return('won')
            else:
                gd=gd+1
                return('game drawn')

        if choice==2:
            if (comp=='scissor'):
                cw=cw+1
                return('lost')
            elif (comp=='rock'):
                uw=uw+1
                return('won')
            else:
                gd=gd+1
                return('game drawn')

    result=game(user)
    rock_paper_scissor()
    if result=='won':
        result='Computer played '+comp+'''
          You won!'''
    elif result=='lost':
        result='Computer played '+comp+'''
              You lose'''
    else:
        result='         Game Drawn'
    canvas2.create_text(320,335,text=result,font=('Times',22,'bold'),fill='red2',anchor=W)


    tg=cw+uw+gd
    total='Total games played: '+str(tg)
    won=  'Won   : '+str(uw)
    lost= 'Lost   : '+str(cw)
    drawn='Drawn: '+str(gd)
    canvas2.create_rectangle(810,130,1200,330,fill='indian red')
    canvas2.create_text(830,150,text='     Scoreboard',font=('calibri',24,'bold'),fill='red4',anchor=W)
    canvas2.create_text(830,190,text=total,font=('calibri',22,'bold'),fill='navy',anchor=W)
    canvas2.create_text(830,230,text=won,font=('calibri',22,'bold'),fill='navy',anchor=W)
    canvas2.create_text(830,270,text=lost,font=('calibri',22,'bold'),fill='navy',anchor=W)
    canvas2.create_text(830,310,text=drawn,font=('calibri',22,'bold'),fill='navy',anchor=W)
def Logout():
    global_zero()
    global name
    global password
    name=0
    password=0
    mainpage()
def change_username_confirmation():
    global name
    data_base=data_base_load()
    new_name=new_username.get()
    check=password_confirmation1.get()
    password_entry1.delete(0,END)
    new_username_entry.delete(0,END)

    if new_name not in data_base.keys():
        if data_base[name][1]==hash(check):
            db=pymysql.connect('localhost','nayan','1234','user_database')
            cursor=db.cursor()

            cursor.execute("UPDATE data SET username=%s WHERE data_id=%s",(new_name,data_base[name][0]))
            db.commit()
            db.close()
            Settings()

            name=new_name
            print(name)
        else:
            Change_username()
            canvas2.create_text(1080,300,text='Incorrect Password',font=('Times',15,'bold'),fill='black')
    else:
        Change_username()
        canvas2.create_text(1080,300,text='Username Taken',font=('Times',15,'bold'),fill='black')
def Change_username():
    Settings()
    global new_username
    global new_username_entry
    global password_entry1
    global password_confirmation1
    new_username=StringVar()
    password_confirmation1=StringVar()
    new_username_entry=Entry(textvariable=new_username)
    password_entry1=Entry(textvariable=password_confirmation1)
    ok=Button(text='confirm',command=change_username_confirmation,font=('Times',12,'bold'))


    canvas2.create_text(920,180,text='     New Username:',font=('Times',20,'bold'),fill='black')
    canvas2.create_text(920,230,text='Confirm Password:',font=('Times',20,'bold'),fill='black')
    canvas2.create_window(1040,180,window=new_username_entry,anchor=W)
    canvas2.create_window(1040,230,window=password_entry1,anchor=W)
    canvas2.create_window(1050,270,window=ok,anchor=W)
def delete_account():
    Settings()
    def delete_account_confirm():
        global name
        print(name)
        data_base=data_base_load()
        ch=password_confirmation.get()
        password_entry.delete(0,END)
        print(ch)
        if data_base[name][1]==hash(ch):
            db=pymysql.connect('localhost','nayan','1234','user_database')
            cursor=db.cursor()
            cursor.execute('DELETE from data where username=%s',(name))
            db.commit()
            cursor.execute('DELETE from game_record where id=%s',(data_base[name][0]))
            db.commit()
            db.close()
            mainpage()
        else:
            canvas2.create_text(910,320,text='Incorrect Password',font=('calibri',12,'bold'),fill='black',anchor=W)
    def Yes():
        global password_confirmation
        global password_entry
        password_confirmation=StringVar()
        password_entry=Entry(textvariable=password_confirmation)
        ok=Button(text='confirm',command=delete_account_confirm,font=('Times',12,'bold'))

        canvas2.create_text(820,260,text='          Password Verification',font=('calibri',18,'bold'),fill='black',anchor=W)
        canvas2.create_window(900,300,window=password_entry,anchor=W)
        canvas2.create_window(1050,300,window=ok,anchor=W)


    yes=Button(text='Yes',command=Yes,font=('Times',15,'bold'),width=5,height=1)
    no=Button(text='No',command=Settings,font=('Times',15,'bold'),width=5,height=1)

    canvas2.create_window(900,220,window=yes,anchor=W)
    canvas2.create_window(1040,220,window=no,anchor=W)
    canvas2.create_rectangle(810,130,1200,330,fill='blue')
    canvas2.create_text(820,160,text=' Delete BetaHub Account!',font=('calibri',24,'bold'),fill='white',anchor=W)
def Settings():
    global_zero()
    homepage()
    user=Button(text='1. Change username',command=Change_username,font=('Times',22,'bold'),fg='white',bg='blue',width=18,height=1)
    password=Button(text='2. Change password',command=Change_password,font=('Times',22,'bold'),fg='white',bg='blue',width=18,height=1)
    delete=Button(text='3. Delete account   ',command=delete_account,font=('Times',22,'bold'),fg='white',bg='blue',width=18,height=1)

    canvas2.create_text(830,80,text='Settings',font=('calibri',40,'bold'),fill='black')
    canvas2.create_window(380,180,window=user,anchor=W)
    canvas2.create_window(380,230,window=password,anchor=W)
    canvas2.create_window(380,280,window=delete,anchor=W)
def rock_paper_scissor():
    homepage()
    canvas2.create_text(830,80,text='Rock Paper Scissor!',font=('calibri',40),fill='black')
    canvas2.create_text(390,140,text='try your luck!',font=('calibri',22,'bold'),fill='navy',anchor=W)

    rock=Button(text=' Rock ',command=lambda: rock_paper_scissor_game(1),font=('Times',22,'bold'),fg='white',bg='brown',width=10,height=1)
    paper=Button(text='Paper  ',command=lambda: rock_paper_scissor_game(2),font=('Times',22,'bold'),fg='white',bg='SteelBlue3',width=10,height=1)
    scissor=Button(text='scissor',command=lambda: rock_paper_scissor_game(3),font=('Times',22,'bold'),fg='white',bg='gray',width=10,height=1)

    canvas2.create_window(380,180,window=rock,anchor=W)
    canvas2.create_window(380,230,window=paper,anchor=W)
    canvas2.create_window(380,280,window=scissor,anchor=W)

    canvas2.create_rectangle(810,130,1200,330,fill='indian red')
    canvas2.create_text(830,150,text='     Scoreboard',font=('calibri',24,'bold'),fill='red4',anchor=W)
    canvas2.create_text(830,190,text='Total games played: 0',font=('calibri',22,'bold'),fill='navy',anchor=W)
    canvas2.create_text(830,230,text='Won   : 0',font=('calibri',22,'bold'),fill='navy',anchor=W)
    canvas2.create_text(830,270,text='Lost   : 0',font=('calibri',22,'bold'),fill='navy',anchor=W)
    canvas2.create_text(830,310,text='Drawn: 0',font=('calibri',22,'bold'),fill='navy',anchor=W)
def Ping_pong():
    homepage()
    canvas2.create_text(830,80,text='Ping Pong!',font=('calibri',40,'bold'),fill='black')
    canvas2.create_text(830,180,text='Game is under construction, sorry for the inconvenience!',font=('calibri',20),fill='black')
def Game():
    global_zero()
    homepage()
    canvas2.create_rectangle(330,30,1310,440,fill='navy')
    canvas2.create_text(830,80,text='Games',font=('calibri',40),fill='white')
    rps=Button(text='1. Rock Paper Scissors',font=('Times',22,'bold'),fg='white',bg='blue',command=rock_paper_scissor,width=20,height=1)
    ping_pong=Button(text='2. Ping Pong                ',font=('Times',22,'bold'),fg='white',bg='blue',command=Ping_pong,width=20,height=1)

    canvas2.create_window(380,180,window=rps,anchor=W)
    canvas2.create_window(380,230,window=ping_pong,anchor=W)
def Profile():
    global_zero()
    homepage()
    canvas2.create_text(830,80,text='Profile',font=('calibri',40,'bold'),fill='black')
    canvas2.create_text(830,180,text='This page is under maintenance, sorry for the inconvenience!',font=('calibri',20),fill='black')
def home():
    global_zero()
    homepage()
    canvas2.create_text(830,80,text='Welcome to BetaHub',font=('calibri',40),fill='black')
def username_password_criteria(criteria,choice):
    if choice==1:
        for i in criteria:
            if i in ['','*','&','#','$','%','^','(',')']:
                return(1)
    else:
        for i in criteria:
            if i in ['','*','#','%','^','(',')']:
                return(1)
def homepage_layout():
    global root
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
    canvas2.create_rectangle(0,0,300,470,fill='cornflower blue')
    canvas2.create_rectangle(300,0,1340,470,fill='SteelBlue1')
def mainpage_layout():
    global root
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
    canvas2.create_rectangle(0,0,1340,470,fill='SteelBlue1')
def login():
    global name
    global password
    #load data from mysql-server for username and password
    data_base=data_base_load()
    #store userinput in variable to check in database
    name=name_login_entry.get()
    password=password_login_entry.get()

    username_login.delete(0,END)
    password_login.delete(0,END)

    if name in data_base.keys():
        #remove previous comment under login
        if data_base[name][1]==hash(password):
            #remove previous comment under Login
            home()
        else:
            canvas2.create_text(350,170,text="Incorrect password",font=("Times",15),fill='black')
    else:
        #remove previous comment under Login
        canvas2.create_text(350,170,text="Incorrect Username",font=("Times",15),fill='black')
def sign_up_verify(d,name,password,check):
        """ function to check the validity of the user name"""
        if name in d.keys():
            mainpage()
            #canvas2.create_text(955,200,text="                                               ",font=("Times",15),fill='black')
            canvas2.create_text(955,200,text="Username Taken",font=("Times",15),fill='black')
        else:
            canvas2.create_text(955,200,text="                                     ",font=("Times",15),fill='black')
            if password==check:
                db=pymysql.connect('localhost','nayan','1234','user_database')
                cursor=db.cursor()
                encoded=hash(password)
                cursor.execute('INSERT INTO data(username,password) VALUES(%s,%s)',(name,encoded))
                db.commit()
                temp=data_base_load()       #updating data_base with new signup
                cursor.execute('INSERT INTO game_record(id) VALUES(%s)',temp[name][0])
                db.commit()
                db.close()
                mainpage()
                #canvas2.create_text(955,200,text="                                                 ",font=("Times",15),fill='black')
                canvas2.create_text(955,200,text="Account Created",font=("Times",15),fill='black')
            else:
                mainpage()
                #canvas2.create_text(955,200,text="                                                   ",font=("Times",15),fill='black')
                canvas2.create_text(955,200,text="Password doesn't match",font=("Times",15),fill='black')
def signup():
    #load data from mysql-server to check existing username
    data_base=data_base_load()
    #username input from user
    name=name_signup_entry.get()
    #passing username to username_password_criteria to check its validity
    parameter=username_password_criteria(name,1)
    if parameter==1:
        mainpage()
        #canvas2.create_text(955,200,text="                                                     ",font=("Times",15),fill='black')
        canvas2.create_text(955,200,text="Invalid username criteria",font=("Times",15),fill='black')
    else:
        #password input from user
        password=password_signup_entry.get()
        #passing password to username_password_criteria to check its validity
        parameter=username_password_criteria(password,2)
        if parameter==1:
            mainpage()
            #canvas2.create_text(955,200,text="                                                    ",font=("Times",15),fill='black')
            canvas2.create_text(955,200,text="Invalid password criteria",font=("Times",15),fill='black')
        else:
            #password confirmation from user
            check=password_check_entry.get()
            #to store data or give warning that username is already taken
            sign_up_verify(data_base,name,password,check)
            username_signup.delete(0,END)
            password_signup.delete(0,END)
            password_check_signup.delete(0,END)
def clear():
    list = root.winfo_children()
    for item in list :
        if item.winfo_children() :
            list.extend(item.winfo_children())

    for item in list:
        item.grid_forget()
def homepage():

    #remove all the widgets from the window
    clear()
    #reload the layout
    homepage_layout()
    #create buttons for homepage menu
    #home=Button(text='1. Home             ',font=('Times',22,'bold'),fg='white',bg='navy',command=homepage)
    Home=Button(text='1. Home             ',font=('Times',22,'bold'),fg='white',bg='navy',command=home,width=13,height=1)
    profile=Button(text='2. Profile            ',font=('Times',22,'bold'),fg='white',bg='navy',command=Profile,width=13,height=1)
    bank=Button(text='3. Bank Balance',font=('Times',22,'bold'),fg='white',bg='navy',width=13,height=1,command=Bank)
    game=Button(text='4. Games            ',font=('Times',22,'bold'),fg='white',bg='navy',width=13,height=1,command=Game)
    calc=Button(text='5. Calculator      ',font=('Times',22,'bold'),fg='white',bg='navy',width=13,height=1,command=Calculator)
    settings=Button(text='6. Settings         ',font=('Times',22,'bold'),fg='white',bg='navy',width=13,height=1,command=lambda: Settings())
    logout=Button(text='7. Logout           ',command=Logout,font=('Times',22,'bold'),fg='white',bg='navy',width=13,height=1)
    #add widgets to homepage
    canvas2.create_window(30,80,window=Home,anchor=W)
    canvas2.create_window(30,130,window=profile,anchor=W)
    canvas2.create_window(30,180,window=bank,anchor=W)
    canvas2.create_window(30,230,window=game,anchor=W)
    canvas2.create_window(30,280,window=calc,anchor=W)
    canvas2.create_window(30,330,window=settings,anchor=W)
    canvas2.create_window(30,380,window=logout,anchor=W)
def mainpage():
    clear()
    mainpage_layout()
    #Adding Labels
    canvas2.create_text(200,80,text='Username:',font=("Times",20,'bold'),fill='black')
    canvas2.create_text(200,110,text='Password:',font=("Times",20,'bold'),fill='black')
    #Adding entry for username and password input for login
    #globalizing to use them in login() function
    global name_login_entry
    global password_login_entry
    global username_login
    global password_login
    name_login_entry=StringVar()
    password_login_entry=StringVar()
    username_login=Entry(textvariable=name_login_entry)
    password_login=Entry(textvariable=password_login_entry)
    #Adding login button
    login_button=Button(text='Login',command=login)
    #Adding widgets to canvas2 created in layout()
    canvas2.create_window(350,80,window=username_login)
    canvas2.create_window(350,110,window=password_login)
    canvas2.create_window(350,140,window=login_button)

    #adding Labels
    canvas2.create_text(805,80,text='Username:',font=("Times",20,'bold'),fill='black')
    canvas2.create_text(805,110,text='Password:',font=("Times",20,'bold'),fill='black')
    canvas2.create_text(755,140,text='Confirm Password:',font=("Times",20,'bold'),fill='black')
    #Adding entry for username and password input for signup
    #globalizing to use them in signup() function
    global name_signup_entry
    global password_signup_entry
    global password_check_entry
    global username_signup
    global password_signup
    global password_check_signup
    name_signup_entry=StringVar()
    password_signup_entry=StringVar()
    password_check_entry=StringVar()
    username_signup=Entry(textvariable=name_signup_entry)
    password_signup=Entry(textvariable=password_signup_entry)
    password_check_signup=Entry(textvariable=password_check_entry)
    #Adding signup button
    signup_button=Button(text='Sign Up',command=signup)
    #Adding widgets to canvas2 created in layout
    canvas2.create_window(955,80,window=username_signup)
    canvas2.create_window(955,110,window=password_signup)
    canvas2.create_window(955,140,window=password_check_signup)
    canvas2.create_window(955,170,window=signup_button)

root = Tk()
mainpage()
root.mainloop()
