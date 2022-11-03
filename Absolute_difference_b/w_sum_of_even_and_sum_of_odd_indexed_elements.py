n=int(input())
l=[int(x) for x in input().split()]
s1=0
s2=0
for i in range(0,len(l),2):
    s1+=l[i]
for i in range(1,len(l),2):
    s2+=l[i]
print(abs(s1-s2))
