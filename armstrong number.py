n=int(input("enter a number"))
i=n
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if i==sum:
    print("number is armstrong")
else:
    print("number is not aemstrong")
