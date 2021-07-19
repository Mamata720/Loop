i=1
num=int(input("enter a number"))
while i< num:
    if num %3==0 and num%7==0:
        print("navgurukul")
    elif num%3==0:
        print("nav")
    elif num%7==0:
        print("gurukul")
    else:
        print(i)
    i=i+1