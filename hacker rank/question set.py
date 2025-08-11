new=set()
n=int(input(""))
l_new=[]
nn2=input("")
l_new=nn2.split( )
for i in range(n):
    new.add(l_new[i])
n1=int(input(""))
for i in range(n1):
    fun=input("")
    l_new2=fun.split( )
    if(len(l_new2)==1):
        if(l_new2[0]=="pop"):
            new.pop()
    elif(len(l_new2)==2):
        if(l_new2[0]=="remove"):
            new.remove(l_new2[1])
        elif(l_new2[0]=="discard"):
            new.discard(l_new2[1])
print(new)
