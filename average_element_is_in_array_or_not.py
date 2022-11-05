n=int(input())
l=[int(x) for x in input().split()]
s=0
for i in l:
    s+=i
a=s//n
if a in l:
    print("True")
else:
    print("False")