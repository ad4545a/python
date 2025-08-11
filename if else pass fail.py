math=int(input("enter the marks of the math:-  "))
physics=int(input("enter the marks of the physics:-  "))
chemistry=int(input("enter the marks of the chemistry:-  "))
total= ((math + physics + chemistry)/300)*100
print("the total percentage is:- ",total)
if(total < 40 or math< 33 or chemistry < 33 or physics < 33):
  print("fail")
else:
  print("pass")