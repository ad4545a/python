#write a proogrma to accpet from the user the triangle is possible or not
angle1=int(input("enter the 1st angle::- "))
angle2=int(input("enter the 2st angle::- "))
angle3=int(input("enter the 3st angle::- "))
total = angle1+angle2+angle3
if total==180 and angle3>0 and angle2>0 and angle1>0:
    print("triangle is possible")
else :
    print("triangle is not possible")