"""Author	Nayan Lad"
   Date		01/06/2019
Program to create game of rock, paper, scissors"""

import os
import pymysql
import time
import random

uw=0				#No of user wins
cw=0				#No of computer wins
gd=0   				#No of games drawn
def rock_paper_scissor_game(user):
    def game(user,comp):
        global uw,cw,gd
        if choice==1:            #rock
            if (comp=='scissor'):
                uw=uw+1
            elif (comp=='paper'):
                cw=cw+1
            else:
                gd=gd+1

        if choice=3:          #scissor
            if (comp=='rock'):
                cw=cw+1
            elif (comp=='paper'):
                uw=uw+1
            else:
                gd=gd+1

        if choice=3:
            if (comp=='scissor'):
                cw=cw+1
            elif (comp=='rock'):
                uw=uw+1
            else:
                gd=gd+1

    list=['rock','paper','scissor']
    b=random.choice(list)
    game(user,comp)




    """
    tg=uw+cw+gd
    print("\n======================")
    print("        GAME STATS")
    print("========================\n")
    print("Games user won    = ",uw)
    print("Games computer won= ",cw)
    print("Games drawn       = ",gd)
    print("Total games played= ",tg)
    print(""" \n""")
    print("Re-directing to home page")
    time.sleep(5)
    db=pymysql.connect('localhost','nayan','1234','user_database')
    cursor=db.cursor()
    sql='select*from game_record where id=%s;'
    cursor.execute(sql,id)
    result=cursor.fetchall()
    l=[uw,cw,gd,tg]
    temp=[]
    j=1
    for i in l:
        if result[0][j]==None:
            if i not in [0]:
                temp.append(int(i))
                j=j+1
        else:
            n=int(i)+int(result[0][j])
            temp.append(n)
            j=j+1
    cursor.execute('UPDATE game_record SET won=%s WHERE id=%s',(temp[0],id))
    db.commit()
    cursor.execute('UPDATE game_record SET lost=%s WHERE id=%s',(temp[1],id))
    db.commit()
    cursor.execute('UPDATE game_record SET drawn=%s WHERE id=%s',(temp[2],id))
    db.commit()
    cursor.execute('UPDATE game_record SET total=%s WHERE id=%s',(temp[3],id))
    db.commit()
    db.close()"""
