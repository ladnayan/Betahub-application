import os
import pymysql
import time

def delete_account(data_base,name):
    while True:
        print("""Account: """,name,'\n')
        print("""          Do you want to delete your account?
                  Y or N""")
        user_input=input()

        if user_input in ['n','N','NO','no']:
            break

        elif user_input in ['Y','y','yes','YES']:
            print("\n Confirm your password:")
            password=input()
            if data_base[name][1]==hash(password):
                db=pymysql.connect('localhost','nayan','1234','user_database')
                cursor=db.cursor()
                cursor.execute('DELETE from data where username=%s',(name))
                db.commit()
                cursor.execute('DELETE from game_record where id=%s',(data_base[name][0]))
                db.commit()
                db.close()
                print("Account deleted \n Re-directing to login page")
                time.sleep(2)
                os.system('clear')
                break
            else:
                print("Incorrect password")

        else:
            print("Enter valid option")
