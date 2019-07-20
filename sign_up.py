import pymysql
import os
import time
from data_base_load import data_base_load
def sign_up(data_base,name,password):

    db=pymysql.connect('localhost','nayan','1234','user_database')
    cursor=db.cursor()
    encoded=hash(password)
    cursor.execute('INSERT INTO data(username,password) VALUES(%s,%s)',(name,encoded))
    db.commit()
    temp=data_base_load()       #updating data_base with new signup

    cursor.execute('INSERT INTO game_record(id) VALUES(%s)',temp[name][0])
    db.commit()
    db.close()

    print("\n Account successfully created \n re-directing to login page")
    time.sleep(2)
    os.system('clear')
    return(temp)
