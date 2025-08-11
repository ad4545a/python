#write a progera to accpect marks of three subject from the the user calculate the total and avg.display pass or fail fi the avg is greater than equal to 40 display pass atherwise fail.
m1= int(input("enetr the marks of 1st sub:- "))
m2= int(input("enetr the marks of 2nd sub:- "))
m3= int(input("enetr the marks of 3rd sub:- "))
avg=(m1+m2+m3)/3
total=m1+m2+m3
print("total marks:- ",total)
print("avg of marks:- ",avg)
if avg<40:
    print("fail")
else:
    print("pass")