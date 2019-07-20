import os
import time
os.system('clear')
def bank_account(d,name):
	class BankAccount:

		balance=0.00
		def bank_balance(self):
			print('Rs',c.balance)
		def debit(self):
			print('Current balance: Rs',c.balance)
			if int(c.balance)<=0:
				print("lol")
			else:
				user_input=eval(input('Enter debit amount:'))
				if user_input>c.balance:
					print("Insufficient balance")
				else:
					c.balance=c.balance-user_input
					print('Remaining balance: Rs',c.balance)
		def credit(self):
			print('Current balance: Rs',c.balance)
			user_input=eval(input('Enter credit amount:'))
			c.balance=c.balance+user_input
			print("New balance: Rs",c.balance)


	c=BankAccount()
	os.system('clear')
	print("""========================================
	BetaHub Bank: Welcome """,name,"""
========================================""")
	while True:
		print("""Select your option:
	   1. balance
	   2. debit
	   3. credit
	   4. exit""")
		choice=input()
		if choice in ['1','balance']:

			c.bank_balance()
		elif choice in ['2','debit']:
			c.debit()
		elif choice in ['3','credit']:
			c.credit()
		elif choice in ['4','exit']:
			break
		else:
			print("Enter a valid option")

	print("Your transaction is completed")
	time.sleep(3)
