import math
n=int(input())
for i in range (n):
    m=int(input())
    s=math.sqrt(m)
    if int(s+0.5)**2==m:
        print("True")
    else:
        print("False")
    