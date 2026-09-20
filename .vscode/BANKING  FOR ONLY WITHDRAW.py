import random
print("=====WELCOME TO THE ATM=====")
balance=random.randint(100,5000)
print(f"SEE THE BALANCE:{balance}")
amount=int(input("ENTER THE AMOUNT:"))
if amount>balance:
         print("YOU DONT HAVE ENOUGH MONEY")
elif amount>100:
     print("YOUR CASH IS PROCESSING")
     print("TAKE YOUR CASH")
else:
    print("YOU DON'T HAVE ENOUGH MONEY TO WITHDRAW")
remaining=balance-amount
print(f"REMAINING BALANCE :{remaining}")
print("THANK YOU FOR VISITING OUR BANK PLEASE COME AGAIN")

