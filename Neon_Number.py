n=int(input())
m=n**2
s=0
for i in str(m):
    s+=int(i)
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")