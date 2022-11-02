n=int(input())
l=[int(x) for x in input().split()]
s=0
for i in range(0,len(l),2):
    s+=l[i]
print(s)