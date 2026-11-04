a=int(input("Enter withdrawal amount:"))
balance = 10000
if a<=0:
    print("Invalid Amount")
elif a > balance:
    print("Insufficient Balance")
else:
    print("Withdrawal Successful")
    remaining= balance-a
    print("Remaining Balance:",remaining)