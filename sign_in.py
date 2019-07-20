import os
def sign_in(d):

        """function for sign in by checking hash value stored in dictionary"""

        for i in range(3):
            print("Enter your user name:")
            name=input()
            l=d.keys()              #change made
            if name not in l:
                    os.system('clear')
                    print("""User name not found. Enter registered user name
                            """)

            else:                           #add except statement
                count=1
                while True:
                        print("Enter your password:")
                        password=hash(input())
                        #encode_check=hashlib.sha256(b'password')
                        if  d[name][1]==password:
                                os.system('clear')
                                return(name)
                                break

                        else:
                                if count==3:
                                        os.system('clear')
                                        print("Max password attempts reached")
                                        return(0)
                                        break
                                else:
                                       # os.system('clear')
                                        print("Incorrect password")
                                        count=count+1
