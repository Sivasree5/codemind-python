def prime(n):
    if n==1:
        return 0
    else:
        for i in range(2,n):
            if n%i==0:
                return 0
        return 1
n=int(input())
c=0
if prime(n):
    for i in str(n):
        if prime(int(i)):
            c+=1
if c==len(str(n)):
    print("Mega Prime")
else:
    print("Not Mega Prime")