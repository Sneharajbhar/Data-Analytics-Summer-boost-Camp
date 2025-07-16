'''# while Loop
num = int(input("Enter a Number:"))
i = 1
while i<=10:
    print(f"{num} x {i} = {num*i}")
    i+=1

# mini project using while loop
chance = 3
while (chance>0):
    password = (input("Enter The Password:"))
    if password == "Sneha036":
        print("Login")
        break
    else :
        chance-=1
        print("Your have ",chance,"chance left")
        if chance!= 0 :
            print("Wrong Password Try ")

# pass
count = 1
while count<=100:
        if count%7 == 0:
            print(count)
        else:
            pass
        count+=1

# table using for loop
num = int(input("Enter A Number:"))
for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

# password que using for loop
attempt = 3
for i in range(1,4):
    password = (input("Enter The Password:"))
    if password == "Sneha036":
        print("Login")
        break
    else :
        attempt-=1
        print("Your have ",attempt,"chance left")

# continue      
for i in range(1,6):
        if i == 3:
                continue
        print(i)
# continue and break
for i in range(1,11):
        if i == 5:
                continue
        elif i==8:
                break
        print(i)
# password que using break continue

attempt = 5
for i in range(1,6):
        password = (input("Enter The Password:"))
        if password == "Sneha036":
                print("Login")
                break
        elif password == "forget":
                attempt-=1
                print("This attempt has been skip",attempt)
                continue
        else :
                attempt-=1
                print("Your have ",attempt,"chance left")'
# string 
string = "Python for Programming"

for i in range (len(string)):
        if string[i]=='o':
                continue
        elif string[i]=='n':
                break
        else:
                print(string[i])
                
for i in range (4):
        print(i)'''


# Fuctions in python
# def keyword define
# fuction name
# parameter

'''def hello():
        print("Hello for function !!!")
hello()

def sum(a,b):
        return a+b
print(sum(23,89))

def reverse(string):

print(reverse("Sneha"))
#print("Hello,World!")

fact=1
num = int(input("Enter a Number:"))
if num>=0:
    if(num==0 or num==1):
        print("1")
    else:
        for i in range(1,num+1):
            fact*=i
        print(fact)
else:
    print("Invalid Number ")'''
'''flag = True
num = int(input("Enter a number:"))
for i in range(2,num//2):
    if(num/i==0):
        flag = False
        break
if flag==True:
    print("Number is prime")
else :
    print("Number is not prime")'''

n = int(input("Enter the number of terms: "))


a, b = 0, 1


print("Fibonacci Series:")
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(a)
else:
    print(a, b, end=" ")
    for _ in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c




        
    
    
        
