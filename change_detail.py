import os
from name_password_change import name_password_change
from delete_account import delete_account

def change_detail(data_base,name):
    """ to change account details"""
    os.system('clear')
    while True:

        print("""==========================
       Account Update:
 ==========================
    1. Username
    2. Password
    3. Delete Account
    4. Exit to home page""")

        choice=input()
        if choice in ['1','username','Username','USERNAME']:
            name=name_password_change(data_base,choice,name)
            return(name)
        elif choice in ['2','password','Password','PASSWORD']:
            name=name_password_change(data_base,choice,name)
            return(name)
        elif choice in ['3','delete','DELETE']:
            delete_account(data_base,name)
            return(0)
            break
        elif choice in ['4','exit','Exit','EXIT']:
            os.system('clear')
            return(name)
            break
        else:
            os.system('clear')
            print('Enter a valid option')
