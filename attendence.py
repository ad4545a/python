n=input("enter the name of child:- ")
c=int(input("enter the no of online class:- "))
d=int(input("enter the no of online class held:- "))
l=(c/d)*100
if(l>=85):
    print(f'"{n} is allowed to give exam"')
else:
    print(f'"{n} is not allowed to give exam"')