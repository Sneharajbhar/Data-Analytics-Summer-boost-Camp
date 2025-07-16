def sumOfNaturalNumber(num):
    sum = 0
    if num%2!=0: 
        for i in range(1,num+1):
           sum+=i # sum=sum+i compound operator 
        print(sum)
sumOfNaturalNumber(50)
