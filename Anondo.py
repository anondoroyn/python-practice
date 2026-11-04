x=int(input("Enter your number "))
y=int(input("Enther another number "))
print(x,"+",y,"=",x+y)
print(x,"%",y,"=",x%y)
print(x,"//",y,"=",x//y)


x=50
if x>=10:
     print(" x is greater then 10 ")
     a= 100+5
     a= a*10
     print(a)
print("abc")


number = int(input("Enter a number: "))
if number % 2== 0:
     print("Even number")
else:
     print(" Odd number")
     
     
age=int(input(" Even your age :"))
if age>=18:
    print("Your are eligible to vote")
else:
    print("Your are not eligible to vote")
marks=int(input("Enter your marks:"))
if marks>=40:
    print("pass")
else:
    print("fail")
marks = int(input("Enter your marks: "))


if  91<=marks <=100:
    print("Grade: Golden")
elif 80 <= marks <= 90:
    print("Grade: A+")
elif 70 <= marks <= 79:
    print("Grade: A")
elif 60 <= marks <= 69:
    print("Grade: B+")
elif 50 <= marks <=59:
    print("Grade: B")
elif 40 <= marks <= 49:
    print("Grade: C")
elif 30 <= marks <= 39:
    print("Grade: Fail")
else:
    print("Invalid marks")


a="5"
b=2
print(a*b)


i=10
j=1
while j<=i:
    if i%2==0:
        print(i)
    i=i-j


a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
d=int(input("Enter a number: "))
if a>b:
    if a>c:
         if a>d:
            print("a is greatest")
         else:
            print("d is greatest")
    else:
        print("c is greatest")
        if b>c:
            print("b is greatest")
        else:
            print("c is greatest")
else:
     if b>c:
          print("b is greatest")
     else:
          print("c is greatest")
     if c>d:
          print("d is greatest")
     else:
          print("c is greatest")


x=1
sum=0
while 10>=x:
    sum=sum+x
    print(x)
    x=x+1
print("Total sum=",sum)


x=1
sum=0
while 10>=x:
    if x % 2==0:
        print(x)
        x=x+1
print("Total sum=",x)


x=1
while 10>=x:
    if x==8:
        break
    print(x)
    x=x+1
else:
    print("Enter the loop")


salary=int(input("Input basic salary of an employee: "))
if salary <= 10000 :
   har = salary*0.20 
   da = salary *0.80
elif salary <= 20000 :
   har = salary*0.25
   da = salary*0.90
else:
    har = salary*0.30
    da = salary*0.95
gross_salary=salary+har+da
print("Gross salary = ",int(gross_salary))


unit=int(input("electricity unit: "))
if unit <= 50:
    amt=unit * 0.50
elif unit <= 150:
    amt = (50 + 0.50) + ((unit-50) * 0.75)
elif unit <= 250:
    amt= (50 + 0.50) + (100* 0.75)+((unit-150)*1.20)
else:
     (50 + 0.50) + (100* 0.75)+(100*1.20)((unit-250)*1.50)
surcharge = amt * 0.20
total= amt+ surcharge
surcharge = amt * 0.20
print(f"Electricity unit: {amt}, Surcharge: {surcharge}, Total: {total}")


x=int(input("Enter your number :"))
last=x%10
while x>=10:
    x=x//10
frist=x
print("first digit:",frist)
print("last digit:",last)

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