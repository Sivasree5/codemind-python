n=int(input())
l=[int(x) for x in input().split()]
s=0
for i in l:
    s+=i
a=s/n
print(format(a,'.2f'))
    