n=int(input())
for i in range (n):
    m=int(input())
    if str(m)==str(m)[::-1]:
        print("True")
    else:
        print("False")