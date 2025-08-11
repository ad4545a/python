n=int(input("enter the no of the terms of the list:- "))
list=[]
for i in range(1,n+1):
    n_i =int(input(f"enter the {i} element:- "))
    list.append(n_i)
list.sort()
print(list[1])