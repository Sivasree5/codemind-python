p,r,t=map(int,input().split())
j=p*(pow((1+r/100),t))
print(format(j,".2f"))