import os
import pymysql
import time
from name_check import name_check
from password_check import password_check
def name_password_change(data_base,choice,name):


        count=1
        while True:
                print("Confirm your password")
                password=hash(input())
                #encode_check=hashlib.sha256(b'password')

                if  data_base[name][1]==password:
                        #os.system('clear')
                        if choice in ['1','username','USERNAME','Username']:
                                new_name=name_check(data_base,1)
                                db=pymysql.connect('localhost','nayan','1234','user_database')
                                cursor=db.cursor()

                                cursor.execute("UPDATE data SET username=%s WHERE data_id=%s",(new_name,data_base[name][0]))
                                db.commit()
                                db.close()
                                temp=data_base[name]
                                del data_base[name]
                                data_base[new_name]=temp
                                print("\nUsername changed successfully:")
                                time.sleep(2)
                                return(new_name)
                                break

                        else:
                                new_password=password_check(c=2)
                                encoded=hash(new_password)
                                db=pymysql.connect('localhost','nayan','1234','user_database')
                                cursor=db.cursor()
                                cursor.execute("UPDATE data SET password=%s WHERE username=%s",(encoded,name))
                                db.commit()
                                db.close()
                                data_base[name][1]=encoded
                                print("\nPassword changed successfully:")
                                time.sleep(2)
                                return(name)
                                break

                else:
                        if count==3:
                                os.system('clear')
                                print("Max password attempts reached")
                                break
                        else:
                                #os.system('clear')
                                print("Incorrect password")
                                count=count+1
