list1=[[2,1],[2,1],[2,1]]
list2=[]
list3=[]
i=0
k=0
while i<len(list1):
    if i%2==0:
        list2+=list1[i]
        i+=1
    else:
        for j in (list1[i])[::-1]:
            print(j)
            list2.append(j)
        i+=1

while k<len(list2):
    if k%2==0:
        list3.append(list2[k])
    k+=1
         
        
        
print(list2)
print(list3)


