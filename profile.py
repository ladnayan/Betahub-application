import os
import pymysql
import datetime

def profile(data_base,name):
    os.system('clear')
    db=pymysql.connect('localhost','nayan','1234','user_database')
    cursor=db.cursor()
    cursor.execute('select*from game_record where id=%s',data_base[name][0])
    r=(cursor.fetchall())
    db.close()
    while True:
        print("=====================================")
        print("               PROFILE               ")
        print("=====================================\n")
        print("Username: ",name)
        print("Application usage: ",str(datetime.timedelta(seconds=int(data_base[name][2]))))
        print("Games: Rock/Paper/Scissor")
        print("  won  : ",r[0][1])
        print("  lost : ",r[0][2])
        print("  Draw : ",r[0][3])
        print("  Total: ",r[0][4],"\n")

        print("\n Enter Q/q to exit to home page:")
        user_input=input()
        if user_input in ['q','Q']:
            break
