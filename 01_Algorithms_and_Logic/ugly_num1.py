n=2123366400
#n=905391974
m=n
if n<=0:
    print(False)
while m>1:
    if m%2==0:
        m=m/2
    elif m%3==0:
        m=m/3
    elif m%5==0:
        m=m/5
    else:
        print(False)
        break
else:
    print("m",m)


