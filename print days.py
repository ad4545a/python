n=int(input("enter the no between 1-7:- "))
dis={
    1: "sunday",2: "monday",3: "tuesday",4: "wednesday",5: "thursday",6: "friday",7: "saturday"
}
if(n>7 and n<=0):
    print("enter valid no")
else:
    c=dis.get(n)
    print(c)