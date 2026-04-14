s="MMMXCI"
k=len(s)
t_val=0
total = 0
while k>0:
    i=s[k-1]
    #print(i)
    k-=1#k=9
    if i=="I":
        val=1
        total+=val
    elif i=="V":
        val=5
        if s[k-1]=="I" and k>0:
            pre_val=1
            t_val=val-pre_val
            total+=t_val
            k-=1#k=8
        else:
            total+=val
    elif i=="X":
        val=10
        if s[k-1]=="I" and k>0:
            pre_val=1
            t_val=val-pre_val
            total+=t_val
            k-=1
        else:
            total+=val
    elif i=="L":
        val=50
        if s[k-1]=="X" and k>0:
            pre_val=10
            t_val=val-pre_val
            total+=t_val
            k-=1
        else:
            total+=val
    elif i=="C":
        val=100
        if s[k-1]=="X" and k>0:
            pre_val=10
            t_val=val-pre_val
            total+=t_val
            k-=1
           
        else:
            total+=val
    elif i=="D":
        val=500
        if s[k-1]=="C" and k>0:
            pre_val=100
            t_val=val-pre_val
            total+=t_val
            k-=1
            print("t",total)
        else:
            total+=val
    elif i=="M":
        val=1000 
        if s[k-1]=="C" and k>0:
            pre_val=100
            t_val=val-pre_val
            total+=t_val
            k-=1
            print("l",total)
        else:
            total+=val
            print("t",total)
print(total)


