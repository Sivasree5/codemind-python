n=int(input())
f=[2,3,5]
for i in f:
    while n%i==0:
        n=n//i
if n==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")