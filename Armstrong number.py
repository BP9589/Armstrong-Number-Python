n=int(input("enter the number"))
s=0
m=n
while(n!=0):
    r=n%10
    s=s+(r*r*r)
    n=n//10
if(m==s):
    print("number is armstrog")
else:
    print("number is not armstrong")