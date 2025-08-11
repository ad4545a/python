n=int(input("enter the no of the terms of the list:- "))
list=[]
for i in range(1,n+1):
    list.append(i)
    i=i+1
sorted(list)
print(list[1])