num=int(input("enter a number"))
num1=int(input("enter a number"))
i=num
while i<=num1:
    j=0
    while j<=10:
        print(num,"*",j,"=",num*j)
        j=j+1
        
    print()
    num+=1
    i=i+1
