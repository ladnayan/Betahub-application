import time
import os
import pymysql
from sign_in import sign_in
from bank_account import bank_account
from game_beta import user_game
from change_detail import change_detail
from profile import profile

def login(data_base):

    name=sign_in(data_base)
    id=data_base[name][0]

    if name==0:
        print(" ")
    else:
        start=time.time()
        while True:

           os.system('clear')
           print("\n===============================")
           print("    Welcome back: ",name)
           print("===============================\n")
           print("""Select from given options:
           1. Profile
           2. Bank Account
           3. Games
           4. Events
           5. Memories
           6. Settings
           7. Help & Support
           8. Log out""")

           choice=input()

           if choice in ['1','profile','Profile','PROFILE']:
               profile(data_base,name)

           elif choice in ['2','bankaccount','BankAccount','Bank Account','bank account','BANKACCOUNT']:
                bank_account(data_base,name)

           elif choice in ['3','games','Games','GAMES']:
                os.system('clear')
                user_game(data_base,id)

           elif choice in ['4','Events','events','EVENTS']:
                print('events')

           elif choice in ['5','memories','Memories','MEMORIES']:
                print('memories')

           elif choice in ['6','settings','Settings','SETTINGS']:
                name=change_detail(data_base,name)
                if name==0:
                    break

           elif choice in ['7','Help&Support','help&support','Help & Support','help&support']:
                print('help')

           elif choice in ['8','Log out','Logout','logout','LOGOUT','log out']:
                os.system('clear')
                stop=time.time()
                t=stop-start
                db=pymysql.connect('localhost','nayan','1234','user_database')
                cursor=db.cursor()
                check=data_base[name][2]

                if check==None:
                    data_base[name][2]=t
                    cursor.execute('update data set usage_time=%s where username=%s',(t,name))
                else:
                    total_usage=t+check
                    data_base[name][2]=total_usage
                    cursor.execute('UPDATE data SET usage_time=%s WHERE username=%s',(total_usage,name))

                db.commit()
                db.close()
                print('You have been successfully logged out')
                print('Login duration:',int(t),' seconds')
                break

           else:
                print("chose a valid option")
