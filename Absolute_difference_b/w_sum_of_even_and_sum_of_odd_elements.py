n=int(input())
l=[int(x) for x in input().split()]
s1=0
s2=0
for i in l:
    if i%2==0:
        s1+=i
    if i%2!=0:
        s2+=i
print(abs(s1-s2))
        