def password_check():
        """function to verify password"""
        if c==1:
            print("Enter new password:")
            password=input()
            print("Re-enter your password:")
            check=input()
        else:
            print("Enter password:")
            password=input()
            print("Re-enter your password:")
            check=input()

        if password==check:
                return(password)
        else:
                print("""Your password doesn't match. Re-enter your password:
                        """)
                password_check(c)
