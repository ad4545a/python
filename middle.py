n1=int(input("enter the 1 number:- "))
n2=int(input("enter the 2 number:- "))
n3=int(input("enter the 3 number:- "))
if(n1>n2 and n1>n3):
    max=n1
    min=n3
    if(n2>n3):
        min=n3
        n=n2
    elif(n3>n2):
        min=n2
        n=n3
elif(n2>n1 and n2>n3):
    max=n2
    if(n1>n3):
        min=n3
        n=n1
    elif(n3>n1):
        min=n1
        n=n3
elif(n3>n1 and n3>n2):
    max=n3
    if(n2>n1):
        min=n1
        n=n2
    elif(n1>n2):
        min=n2
        n=n1
print("middle:- ",n)


